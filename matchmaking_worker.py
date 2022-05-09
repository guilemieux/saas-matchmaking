import asyncio
from typing import Iterable

import asyncpg
import itertools
import networkx as nx
from datetime import datetime

from sqlalchemy import select
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker

from app.models import Queue, Player, Match
from app.services.mcf_parser import mcf_parser, MatchCostFunctionTransformer

CONN_POOL: asyncpg.Pool

ENGINE = create_async_engine('postgresql+asyncpg://app:app@localhost:5432/elomatchmaking')
ASYNC_SESSION: sessionmaker = sessionmaker(ENGINE, expire_on_commit=False, class_=AsyncSession)


async def main():
    while True:
        async with ASYNC_SESSION() as session:
            queues = await session.execute(select(Queue))

        await asyncio.gather(*(process_queue(q) for q in queues.scalars()))

        await asyncio.sleep(5)


async def process_queue(queue: Queue):
    print(f'processing queue {queue.id}')

    async with ASYNC_SESSION() as session:
        players = await get_players_waiting_in_queue(queue, session)
        players_by_player_id: dict[int, Player] = {p.id: p for p in players}
        player_graph = get_cost_of_player_pairs(players, queue.match_cost_function, queue.max_match_cost)
        player_matching: set[tuple[int, int]] = nx.max_weight_matching(player_graph)
        for p1_id, p2_id in player_matching:
            match = Match(creation_time=datetime.now())
            p1, p2 = players_by_player_id[p1_id], players_by_player_id[p2_id]
            p1.match = p2.match = match
            p1.status = p2.status = 'MATCHED'
            print(f'Matching: {p1.name} {p1.id} with {p2.name} {p2.id}')

        await session.commit()


async def get_players_waiting_in_queue(queue: Queue, session) -> list[Player]:
    """Returns all players waiting in a given queue."""
    players = (await session.execute(
        select(Player)
        .filter(Player.queue_id == queue.id)
        .filter(Player.status == 'WAITING')
    )).scalars().all()

    for p in players:
        p.attributes['wait_time'] = (datetime.utcnow() - p.join_time).total_seconds()

    return players


def get_cost_of_player_pairs(players: Iterable[Player], cost_function: str, max_cost: float) -> nx.Graph:
    """Returns a heap containing the cost of paring two players together for each pair of players."""
    player_graph = nx.Graph()
    player_graph.add_nodes_from(p.id for p in players)

    parsed_function = mcf_parser.parse(cost_function)
    for p1, p2 in itertools.combinations(players, 2):
        attributes = {
            k: [p1.attributes[k], p2.attributes[k]]
            for k in p1.attributes.keys() & p2.attributes.keys()
        }
        t = MatchCostFunctionTransformer(attributes=attributes)
        cost = t.transform(parsed_function)
        if cost <= max_cost:
            weight = 1 / cost if cost > 0 else 10e12
            player_graph.add_edge(p1.id, p2.id, weight=weight)

    return player_graph


if __name__ == '__main__':
    asyncio.run(main())
