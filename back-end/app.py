from fastapi import HTTPException
from models.video import Video, VideoInfo
import yt_dlp
from automapper import mapper


def download_video(video: Video) -> VideoInfo | Exception:
    """This function will fetch info about the video. It will use an automapper to map properties from the yt_dlp api to the model we specified"""
    info = None
    ydl_opts = {
        "format": "m4a/bestaudio/best",
        # ℹ️ See help(yt_dlp.postprocessor) for a list of available Postprocessors and their arguments
        "postprocessors": [
            {  # Extract audio using ffmpeg
                "key": "FFmpegExtractAudio",
                "preferredcodec": "m4a",
            }
        ],
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        try:
            info = ydl.extract_info(video.link, download=False)
        except:
            print(f"information not loaded {info}")
            raise HTTPException(status_code=404, detail="Video unavailable")
        info = mapper.to(VideoInfo).map(info)
    return info
