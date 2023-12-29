import os

from fastapi import FastAPI
from router import web_chat_router

from fastapi import FastAPI, Depends
from typing_extensions import Annotated
from functools import lru_cache
from config import FactoryConfig, GlobalConfig
from db.session import create_tables
from db.base_class import Base
from fastapi.middleware.cors import CORSMiddleware

from dotenv import find_dotenv, load_dotenv
import os
from pydantic import BaseModel

import sys, uvicorn
import argparse





def start_application(settings):
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
    create_tables(settings)
    return app


# app.include_router(nepse_router.router)


def main(args):

    env = args.env
    print(env)

    load_dotenv(f"{env}.env")
    print(os.getenv("DB_URL"))
    @lru_cache
    def get_settings():
        return FactoryConfig(env_state=env)()

    settings = get_settings()
    print(settings)
    app = start_application(settings)
    app.include_router(web_chat_router.router)

    @app.get("/config/")
    def read_config(settings: Annotated[FactoryConfig, Depends(get_settings)]):
        return {"DB_URL": settings}

    @app.get("/")
    async def root():
        return {"message": "Hello world", "DB_URL": settings.DB_URL, "Debug Mode": settings.DEBUG}

    @app.get("/items/{item_id}")
    async def read_item(item_id):
        return {"item_id": item_id}

    uvicorn.run(app, port=8000, host='0.0.0.0')


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--env',
                        action='store',
                        dest='env')
    return parser.parse_args()


if __name__ == "__main__":
    parsed = parse_args()
    main(args=parsed)
