from app.models import Match
from app.services._base_service import BaseService


class MatchService(BaseService[Match]):
    __entity_type__ = Match
