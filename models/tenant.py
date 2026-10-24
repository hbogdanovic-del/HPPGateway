from .decalreDB import Base
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, ForeignKey, DateTime

class Tenant(Base):
    __tablename__ = "tenant"
    id: Mapped[int] = mapped_column(primary_key=True)
    nom: Mapped[str] = mapped_column(String(32))
    mail: Mapped[str] = mapped_column(String(254))
    created_at: Mapped[DateTime] = mapped_column(DateTime(timezone=True))
