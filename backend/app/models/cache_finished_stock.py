from sqlalchemy import Column, Integer, DateTime, JSON, func
from app.db.database import Base


class CacheFinishedStock(Base):
    __tablename__ = "cache_finished_stock"

    id = Column(Integer, primary_key=True, index=True)
    data_json = Column(JSON, nullable=False)
    updated_at = Column(DateTime(timezone=True), server_default=func.now(),
                        onupdate=func.now(), nullable=False)
