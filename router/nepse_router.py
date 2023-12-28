from fastapi import APIRouter, WebSocket
from nepse_api import main as nepse_service
from typing import Annotated, Union
import asyncio

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
    prefix="/nepse",
    tags=["nepse"],
    responses={404: {"description": "Not found"}},
)


@router.get("/{company_symbol}")
async def get_company_high_price(company_symbol: str):
    print(company_symbol)
    loop = asyncio.get_event_loop()
    loop.run_until_complete(nepse_service.get_high_price(company_symbol))
    # return await nepse_service.get_high_price(company_symbol)

@router.get("/")
async def get_nepse():
    return {"message": "Hello from nepse api"}
