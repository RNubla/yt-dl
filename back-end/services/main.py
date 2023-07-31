from typing import Union
from fastapi.middleware.cors import CORSMiddleware


from download.app import download_video
from models.video import Video

from fastapi import FastAPI

app = FastAPI()

origins = ["localhost:3000"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}


@app.post("/video/")
async def get_info(video: Video):
    # if download_video(video) is None:
    #     raise HTTPException(status_code=404, detail="Video unavailable")
    return download_video(video)
