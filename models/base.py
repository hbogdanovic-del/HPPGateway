from sqlalchemy.orm import DeclarativeBase

class Base(DeclarativeBase):
    pass

from .user import User
from .api import API
from .tenant import Tenant
from .apiKey import APIKey
