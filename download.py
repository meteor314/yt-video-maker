# Libraries
import os
import json
import requests
import datetime
import re
import subprocess


def download():
    folder_path = "videos"
    # Create a folder with current date
    date = datetime.datetime.now().strftime('%Y-%m-%d')
    # Create a folder with current date in videos folder
    os.makedirs(f"{folder_path}/{date}", exist_ok=True)

    # Download all videos from reddit.json video links in videos folder with current date

    with open('reddit.json', 'r') as f:
        data = json.load(f)

    # Download all videos from reddit.json video links in videos folder with current date
    for item in data:
        video_url = item['video']
        audio_url = item['audio']
        response = requests.get(video_url, stream=True)
        file_name = re.sub(r'[<>:\"\'/\\\|\?\*\[\] ]+', '_',
                           item['title']) + '.mp4'
        try:
            # download video in video/date folder with youtube-dl
            subprocess.call(
                f"youtube-dl -f bestvideo+bestaudio --merge-output-format mp4 {video_url} -o {folder_path}/{date}/{file_name}", shell=True)
            # write file name in video.txt
            with open(f"{folder_path}/{date}/video.txt", 'a') as f:
                f.write(f"file {file_name}\n")
            print(f"Downloaded {file_name}")

        except Exception as e:
            print(f"Error downloading {file_name}: {e}")
