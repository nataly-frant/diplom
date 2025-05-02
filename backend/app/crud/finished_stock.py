from datetime import datetime, timedelta, timezone

from sqlalchemy import func
from sqlalchemy.orm import Session

from app.models.cache_finished_stock import CacheFinishedStock


def get_or_update(db: Session, fetch_callback):
    cached = db.query(CacheFinishedStock).first()
    if cached and cached.updated_at > datetime.now(timezone.utc) - timedelta(minutes=15):
        return cached
    new_data = fetch_callback()
    if cached:
        cached.data_json = new_data
        cached.updated_at = func.now()
    else:
        cached = CacheFinishedStock(data_json=new_data)
        db.add(cached)
    db.commit()
    db.refresh(cached)
    return cached
