
from fastapi import FastAPI
from router import web_chat_router, nepse_router


from fastapi import FastAPI, Depends
from typing_extensions import Annotated
from functools import lru_cache
from config import Settings

app = FastAPI()
app.include_router(web_chat_router.router)
app.include_router(nepse_router.router)



@lru_cache
def get_settings():
    return Settings()

settings = get_settings()


@app.get("/config/")
def read_config(settings: Annotated[Settings, Depends(get_settings)]):
    return {"DB_URL": settings.DB_URL, "Debug Mode": settings.DEBUG}

@app.get("/")
async def root():
    return {"message" : "Hello world", "DB_URL": settings.DB_URL, "Debug Mode": settings.DEBUG}

@app.get("/items/{item_id}")
async def read_item(item_id):
    return {"item_id": item_id}