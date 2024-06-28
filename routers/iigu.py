import json

from fastapi import APIRouter, UploadFile, Depends

from sqlalchemy.orm import Session

# user imports
from database import crud
from database.database import SessionLocal, engine

from models.schedule import Base
from schemas.schedule import WeekScheduleAddSchema


from schedulizer.excell_scrapper.iigu_scrapper import IIGUExcellScrapper
from schedulizer.schedulizer import Schedulizer


Base.metadata.create_all(bind=engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


institute = 'iigu'

router = APIRouter(tags=['IIGU'], prefix=f'/{institute}')


@router.get('/{group}')
async def group_schedule(group: str, db: Session = Depends(get_db)):
    return crud.get_group_schedule(db=db, group=group)


@router.post('/upload/{course}')
async def file_upload(course: int,
                      file: UploadFile,
                      db: Session = Depends(get_db)) -> dict:
    scrapper = IIGUExcellScrapper(file.file)
    groups = scrapper.get_group_names()
    for group in groups:
        scrapper.group_name = group
        week_schedule = Schedulizer(scrapper).get_week_schedule()

        schedule = WeekScheduleAddSchema(
            schedule=json.dumps(week_schedule),
            group=group.capitalize(),
            course=course,
            institute=institute)

        crud.add_schedule(db=db, schedule=schedule)
    return {'msg': 'Success!'}
