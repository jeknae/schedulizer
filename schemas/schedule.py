from pydantic import BaseModel


class WeekScheduleAddSchema(BaseModel):
    schedule: str
    group: str
    course: int
    institute: str
