from pydantic import BaseModel


class Video(BaseModel):
    link: str


class VideoInfo(BaseModel):
    id: str
    title: str
