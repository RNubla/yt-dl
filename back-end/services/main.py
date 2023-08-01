from typing import Union
from fastapi.middleware.cors import CORSMiddleware
from download.app import video_info, download_audio

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
    return video_info(video)


@app.post("/video/{id}")
def dl_audio(id: str):
    download_audio(id)
    return {"id": id}
    # return download_audio(id)
