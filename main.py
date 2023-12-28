from fastapi import FastAPI
from router import web_chat_router

from fastapi import FastAPI, Depends
from typing_extensions import Annotated
from functools import lru_cache
from config import Settings
from db.session import engine
from db.base_class import Base
from fastapi.middleware.cors import CORSMiddleware


@lru_cache
def get_settings():
    return Settings()


settings = get_settings()

def create_tables():
    Base.metadata.create_all(bind=engine)


def start_application():
    app = FastAPI(title=settings.PROJECT_NAME, version=settings.PROJECT_VERSION)
    origins = [
        "http://localhost",
        "http://localhost:3000",
    ]
    app.add_middleware(
        CORSMiddleware,
        allow_origins=origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
    create_tables()
    return app


app = start_application()
app.include_router(web_chat_router.router)
# app.include_router(nepse_router.router)





@app.get("/config/")
def read_config(settings: Annotated[Settings, Depends(get_settings)]):
    return {"DB_URL": settings.DB_URL, "Debug Mode": settings.DEBUG}


@app.get("/")
async def root():
    return {"message": "Hello world", "DB_URL": settings.DB_URL, "Debug Mode": settings.DEBUG}


@app.get("/items/{item_id}")
async def read_item(item_id):
    return {"item_id": item_id}
