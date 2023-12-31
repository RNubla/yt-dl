from fastapi import HTTPException
from models.video import Video, VideoInfo

from automapper import mapper
import yt_dlp


class Logger:
    def debug(self, msg):
        # For compatibility with youtube-dl, both debug and info are passed into debug
        # You can distinguish them by the prefix '[debug] '
        if msg.startswith("[debug] "):
            pass
        else:
            self.info(msg)

    def info(self, msg):
        pass

    def warning(self, msg):
        pass

    def error(self, msg):
        print(f"MSG {msg}")
        # raise HTTPException(status_code=404, detail=f"{msg}")


def video_info(video: Video) -> VideoInfo | Exception | None:
    """This function will fetch info about the video. It will use an automapper to map properties from the yt_dlp api to the model we specified"""
    info = None
    ydl_opts = {
        "logger": Logger(),
        # "format": "m4a/bestaudio/best",
        # ℹ️ See help(yt_dlp.postprocessor) for a list of available Postprocessors and their arguments
        # "postprocessors": [
        #     {  # Extract audio using ffmpeg
        #         "key": "FFmpegExtractAudio",
        #         "preferredcodec": "m4a",
        #     }
        # ],
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        try:
            info = ydl.extract_info(video.link, download=False)
        except:
            raise HTTPException(status_code=404)
            # return HTTPException(status_code=404)
        info = mapper.to(VideoInfo).map(info)
    return info


def download_audio(videoId: str):
    print(f"videoId {videoId}")
    url: str = f"https://www.youtube.com/watch?v={videoId}"
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
        error_code = ydl.download([url])
        print(f"error_code {error_code}")
        return error_code
