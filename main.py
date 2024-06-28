from fastapi import FastAPI
from routers import iigu


app = FastAPI()
app.include_router(iigu.router)
