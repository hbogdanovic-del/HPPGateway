from .base import Base
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, ForeignKey, DateTime, Boolean, Integer

class APIKey(Base):
    __tablename__ = "api_key"
    id: Mapped[int] = mapped_column(primary_key=True)
    scopes: Mapped[str] = mapped_column(String(255))
    last_used: Mapped[DateTime] = mapped_column(DateTime(timezone=True))
    created_at: Mapped[DateTime] = mapped_column(DateTime(timezone=True))
    created_by: Mapped[int] = mapped_column(ForeignKey("user.id"))
    revoked: Mapped[bool] = mapped_column(Boolean())
    pepper_version: Mapped[int] = mapped_column(Integer())
    id_user: Mapped[int] = mapped_column(ForeignKey("user.id"))
    id_tenant: Mapped[int] = mapped_column(ForeignKey("tenant.id"))
    id_api: Mapped[int] = mapped_column(ForeignKey("api.id"))
