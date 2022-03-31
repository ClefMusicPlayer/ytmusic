from pytube import YouTube
import os

import json
DOWNLOAD_PATH = json.load(open("runconfig.json"))["DOWNLOADS_PATH"]

def download_audio(video_id, download_path):
    outname = f"{download_path}/{video_id}.mp3"
    if os.path.exists(outname):
        return f"{video_id}.mp3"
    yt = YouTube(f"https://www.youtube.com/watch?v={video_id}")
    out = yt.streams.filter(only_audio=True).first().download(download_path)
    os.rename(out, outname)
    return f"{video_id}.mp3"

if __name__ == "__main__":
    download("oakNKCwMoSo", DOWNLOAD_PATH)