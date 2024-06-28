import json
from sqlalchemy.orm import Session

from models.schedule import ScheduleModel
from schemas.schedule import WeekScheduleAddSchema


def get_group_schedule(db: Session, group: str) -> dict:
    group_schedule = db.query(ScheduleModel).filter(ScheduleModel.group == group)
    ordered = group_schedule.order_by(ScheduleModel.upload_date.desc()).first()
    schedule = ordered.schedule
    return json.loads(schedule)


def add_schedule(db: Session, schedule: WeekScheduleAddSchema) -> ScheduleModel:
    db_schedule = ScheduleModel(**schedule.model_dump())
    db.add(db_schedule)
    db.commit()
    db.refresh(db_schedule)
    return db_schedule
