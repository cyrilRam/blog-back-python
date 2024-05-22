from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api import posts, category

app = FastAPI()

app.include_router(posts.router, prefix="/v1/posts", tags=["API posts"])
app.include_router(category.router, prefix="/v1/categories", tags=["API category"])

origin = ["http://localhost:4200"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origin,
    allow_methods=["*"],
    allow_headers=["*"],
)

if __name__ == "__main__":
    import uvicorn

    uvicorn.run("__main__:app", host="localhost", port=8000, reload=True)
