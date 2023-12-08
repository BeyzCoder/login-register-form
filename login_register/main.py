from fastapi import FastAPI, status
from fastapi.responses import JSONResponse
from routes import login

from database.config import engine
from database.models import user_accounts

import asyncio
import uvicorn

# Create the tables column for the database
user_accounts.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(login.router, prefix="/account")

@app.get("/")
async def root() -> JSONResponse:
    data = { "Message" : "This is the root path" }
    return JSONResponse(content=data, status_code=status.HTTP_200_OK, media_type="application/json")

async def main() -> None:
    await uvicorn.run("main:app", host="0.0.0.0", port=80, reload=True)

if __name__ == "__main__":
    asyncio.run(main())