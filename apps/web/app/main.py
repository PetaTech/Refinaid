import uvicorn
from fastapi import FastAPI


app = FastAPI()


@app.get("/")
def hello_world() -> dict[str, str]:
    return {"message": "Hello, Refinaid"}


if __name__ == "__main__":
    uvicorn.run(
        "app.main:app",
        host="0.0.0.0",
        port=8080,
        reload=True,
    )
