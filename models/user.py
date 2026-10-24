from .decalreDB import Base
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, ForeignKey, DateTime
from .tenant import Tenant

class User(Base):
    __tablename__ = "user"
    id: Mapped[int] = mapped_column(primary_key=True)
    nom: Mapped[str] = mapped_column(String(32))
    prenom: Mapped[str] = mapped_column(String(32))
    created_at: Mapped[DateTime] = mapped_column(DateTime(timezone=True))
    id_tenant: Mapped[int] = mapped_column(ForeignKey("tenant.id"))
