from sqlalchemy import String,  Integer
from sqlalchemy.orm import Mapped, mapped_column, relationship
from typing import List
from infrastructure.database.db_gateway import Base

class Role(Base):
    __tablename__ = "roles"

    role_id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    role_name: Mapped[str] = mapped_column(String(50), unique=True, nullable=False)
    role_description: Mapped[str | None] = mapped_column(String(255), nullable=True)

    #Связь между таблицами
    users: Mapped[List["UserRoleRelation"]] = relationship(
        back_populates="role", cascade="all, delete-orphan"
    )