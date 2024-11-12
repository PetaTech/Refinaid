# -*- coding: utf-8 -*-
'''
Create Date: 2023/09/08
Author: @1chooo (Hugo ChunHo Lin)
Version: v0.1.1
'''

import os
from pathlib import Path

import uvicorn
from app.utils.build_playground import build_and_mount_playground
from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles

app = FastAPI(
    title="SIMPLE AI",
    description="Bridging the Gap with AI For Everyone",
    version="Refinaid-v0.1.4-beta",
    docs_url="/docs",
)

os.makedirs("static", exist_ok=True)
app.mount(
    "/static", 
    StaticFiles(directory="static"), 
    name="static",
)

app = build_and_mount_playground(
    app,
    "plum",
    "favicon.ico",
    "/plum",
)

app = build_and_mount_playground(
    app,
    "classifier",
    "favicon.ico",
    "/classifier",
)

@app.get("/")
def hello_world() -> dict[str, str]:
    return {"message": "Hello, Simple AI"}

@app.get('/favicon.ico', include_in_schema=False)
async def favicon() -> FileResponse:
    return FileResponse(Path('static') / 'favicon.ico',)

def main() -> None:
    uvicorn.run(
        "app.main:app",
        host="0.0.0.0",
        port=8080,
        reload=True,
    )

if __name__ == '__main__':
    main()
