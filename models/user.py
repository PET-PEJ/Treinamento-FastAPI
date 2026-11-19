from database.base import Base
from sqlalchemy import Integer, CHAR, TEXT, VARCHAR, TIMESTAMP, func
from sqlalchemy.orm import Mapped, mapped_column
from datetime import datetime

class User(Base):
    __tablename__ = "usuarios"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True, autoincrement=True)
    name: Mapped[str] = mapped_column(CHAR(100), index=True)
    email: Mapped[str] = mapped_column(VARCHAR(150), unique=True, index=True)
    password_hash: Mapped[str] = mapped_column(TEXT)
    accronym: Mapped[str] = mapped_column(CHAR(3), unique=True, index=True)
    created_at: Mapped[datetime] = mapped_column(TIMESTAMP, default=func.now())