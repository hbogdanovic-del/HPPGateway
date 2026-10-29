import datetime as dt
from .base import Base
from sqlalchemy.orm import Mapped, mapped_column, relationship, Session
from sqlalchemy import String, ForeignKey, DateTime, create_engine, func

class Tenant(Base):
    __tablename__ = "tenant"
    id: Mapped[int] = mapped_column(primary_key=True)
    nom: Mapped[str] = mapped_column(String(32))
    mail: Mapped[str] = mapped_column(String(254))
    created_at: Mapped[DateTime] = mapped_column(DateTime(timezone=True),server_default=func.now())

    def __repr__(self):
        return f"Tenant<{self.id}> : {self.nom}, {self.mail}, {self.created_at}"
