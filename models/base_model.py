#!/usr/bin/python3

from uuid import uuid4
from datetime import datetime
class BaseModel:
    id = str(uuid.uuid4)
    created_at = now.datetime
    updated_at = now.datetime

    def __str__(self):
        return [class.__name__] (self.id) <self.__dict__>