from fastapi import APIRouter, WebSocket
from web_chat import main as web_chat_service
from typing import Annotated, Union

from fastapi import (
    Cookie,
    Depends,
    FastAPI,
    Query,
    WebSocket,
    WebSocketException,
    status,
)

router = APIRouter(
    prefix="/chat",
    tags=["chat"],
    responses={404: {"description": "Not found"}},
)


@router.get("/")
async def start_chat():
    return await web_chat_service.get()


@router.websocket("/{item_id}/ws")
async def connect_websocket(
        websocket: WebSocket,
    ):
    return await web_chat_service.websocket_endpoint(websocket)


@router.get("/users/{username}", tags=["users"])
async def read_user(username: str):
    return {"username": username}