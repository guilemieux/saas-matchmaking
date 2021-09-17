from app import models
from app import schemas
from app.services._base_service import BaseService


class PlayerService(BaseService[models.Player]):
    __entity_type__ = models.Player

    def _convert_schema_to_db_model(self, player: schemas.PlayerCreate) -> models.Player:
        return models.Player(
            name=player.name,
            queue_id=player.queue_id,
            status='WAITING',
            attributes=player.attributes
        )
