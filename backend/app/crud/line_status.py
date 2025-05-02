from datetime import datetime, timedelta, timezone

from sqlalchemy.orm import Session
from sqlalchemy import func

from app.models.cache_line_status import CacheLineStatus


def get_or_update_line_status(db: Session, fetch_callback):
    cached = db.query(CacheLineStatus).first()
    if cached and cached.updated_at > datetime.now(timezone.utc) - timedelta(minutes=15):
        return cached
    new_data = fetch_callback()
    if cached:
        cached.data_json = new_data
        cached.updated_at = func.now()
    else:
        cached = CacheLineStatus(data_json=new_data)
        db.add(cached)
    db.commit()
    db.refresh(cached)
    return cached
