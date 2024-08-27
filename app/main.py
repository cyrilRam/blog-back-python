from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from starlette.middleware.base import BaseHTTPMiddleware

from app.api import posts, category
from app.utils.middleware import custom_middleware

app = FastAPI()
app.add_middleware(BaseHTTPMiddleware, dispatch=custom_middleware)

app.include_router(posts.router, prefix="/v1/posts", tags=["API posts"])
app.include_router(category.router, prefix="/v1/categories", tags=["API category"])

origin = ["http://localhost:4200"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origin,
    allow_methods=["*"],
    allow_headers=["*"],
)
#test

if __name__ == "__main__":
    import uvicorn

    uvicorn.run("__main__:app", host="localhost", port=8080, log_level="critical", reload=True)
