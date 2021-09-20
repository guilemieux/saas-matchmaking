import asyncio
import json

import asyncpg
import heapq
import itertools
from datetime import datetime

from app.services.mcf_parser import mcf_parser, MatchCostFunctionTransformer


async def process_queue(conn_pool: asyncpg.pool, queue: dict):
    print(f'processing queue {queue}')
    parsed_function = mcf_parser.parse(queue.get('match_cost_function', 'avg(wait_time)'))

    async with conn_pool.acquire() as conn:
        row = await conn.fetch('SELECT * FROM player WHERE queue_id = $1', queue['id'])
    players = [dict(r) for r in row]
    for p in players:
        p['attributes'] = json.loads(p['attributes'])
    players_by_id = {p['id']: p for p in players}
    h = []
    for p1_id, p2_id in itertools.combinations(players_by_id, 2):
        print(f"queue {queue['id']}: {p1_id, p2_id}")
        p1_attributes = {
            **players_by_id[p1_id]['attributes'],
            'wait_time': (datetime.utcnow() - players_by_id[p1_id]['join_time']).total_seconds()
        }
        p2_attributes = {
            **players_by_id[p2_id]['attributes'],
            'wait_time': (datetime.utcnow() - players_by_id[p2_id]['join_time']).total_seconds()
        }
        attributes = {
            k: [p1_attributes[k], p2_attributes[k]]
            for k in p1_attributes.keys() & p2_attributes.keys()
        }
        print(f'attributes: {attributes}')
        t = MatchCostFunctionTransformer(attributes=attributes)
        cost = t.transform(parsed_function)
        heapq.heappush(h, (cost, (p1_id, p2_id)))
    print(h)


async def main():
    queue_last_processed_time_by_id: dict[int, datetime]
    conn_pool = await asyncpg.create_pool("postgresql://app:app@localhost:5432/elomatchmaking")
    while True:
        async with conn_pool.acquire() as conn:
            rows = await conn.fetch('SELECT * FROM queue')
        queues = [dict(r) for r in rows]

        await asyncio.gather(*[process_queue(conn_pool, q) for q in queues])

        await asyncio.sleep(5)


if __name__ == '__main__':
    asyncio.run(main())
