from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.sql import func
from database.database import Base


class ScheduleModel(Base):
    __tablename__ = "schedule"

    id = Column(Integer, primary_key=True)
    schedule = Column(String)
    group = Column(String)
    course = Column(Integer)
    institute = Column(String)
    upload_date = Column(DateTime(timezone=True), server_default=func.now())

