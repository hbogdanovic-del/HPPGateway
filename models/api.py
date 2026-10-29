from .base import Base
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, ForeignKey, DateTime

class API(Base):
    __tablename__ = "api"
    id: Mapped[int] = mapped_column(primary_key=True)
    nom : Mapped[str] = mapped_column(String(255))
    created_at : Mapped[DateTime] = mapped_column(DateTime(timezone=True))
    base_uri : Mapped[str] = mapped_column(String(1024))
    id_tenant : Mapped[int] = mapped_column(ForeignKey("tenant.id"))
    
