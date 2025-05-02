from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Text
from app.db.database import Base
from sqlalchemy.sql import func


class InfoCard(Base):
    __tablename__ = "info_cards"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    content = Column(Text)
    parent_id = Column(Integer, ForeignKey("info_cards.id"), nullable=True)
    order = Column(Integer, default=0)
    type = Column(String)
    created_by_id = Column(Integer, ForeignKey("users.id"))
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
