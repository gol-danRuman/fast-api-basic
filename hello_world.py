from fastapi import FastAPI
from router import web_chat_router, nepse_router
app = FastAPI()
app.include_router(web_chat_router.router)
app.include_router(nepse_router.router)
@app.get("/")
async def root():
    return {"message" : "Hello world"}

@app.get("/items/{item_id}")
async def read_item(item_id):
    return {"item_id": item_id}