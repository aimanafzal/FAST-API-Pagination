from fastapi import APIRouter
from fastapi import FastAPI

root_router = APIRouter()


@root_router.get("/")
def read_root():
    return {"About": "API_Generator API"}


@root_router.get("/healthz")
def get_healthz():
    """To check the service health"""
    return {"status": "ok"}


app = FastAPI("A Simple Pagination", debug=True)


@app.get(path="/api/hello", name="hello endpoint")
async def hello():
    return {"exercise": "pagination"}
