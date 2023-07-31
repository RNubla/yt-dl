from typing import List
from pydantic import BaseModel


class Video(BaseModel):
    link: str


class RequestedFormat(BaseModel):
    filesize: int
    format_id: str
    format_note: str
    fps: int | None
    url: str
    ext: str
    resolution: str
    video_ext: str
    audio_ext: str


class Thumbnail(BaseModel):
    url: str
    preference: int
    id: int


class VideoInfo(BaseModel):
    id: str
    title: str
    # thumbnails: List[Thumbnail]
    thumbnail: str
    description: str
    channel_id: str
    channel_url: str
    # categories: List[str]
    # tags: List[str]
    channel: str
    # url: str
    # audio_ext: str
    format: str
    requested_formats: List[RequestedFormat]
