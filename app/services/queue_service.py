from app.models import Queue
from app.services._base_service import BaseService


class QueueService(BaseService[Queue]):
    __entity_type__ = Queue
