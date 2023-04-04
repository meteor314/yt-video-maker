# Libraries
import os
import json
import requests
import datetime
import re
import subprocess
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
    response = requests.get(video_url, stream=True)
    file_name = re.sub(r'[<>:\"/\\\|\?\*\[\]]+', '_', item['title']) + '.mp4'
    try:
        # download video in video/date folder
        with open(f"{folder_path}/{date}/{file_name}", 'wb') as f:
            for chunk in response.iter_content(chunk_size=1024 * 1024):
                if chunk:
                    f.write(chunk)
        # check if video has audio
        audio_codec = subprocess.check_output(["ffprobe", "-v", "error", "-select_streams", "a:0", "-show_entries", "stream=codec_name",
                                              "-of", "default=noprint_wrappers=1:nokey=1", f"{folder_path}/{date}/{file_name}"]).decode("utf-8").strip()
        if not audio_codec:
            # remove video file if it has no audio
            os.remove(f"{folder_path}/{date}/{file_name}")
            print(f"Skipped {file_name} (no audio)")
            continue
        # write file name in video.txt
        with open(f"{folder_path}/{date}/video.txt", 'a') as f:
            f.write(f"file {file_name}\n")
        print(f"Downloaded {file_name}")

    except Exception as e:
        print(f"Error downloading {file_name}: {e}")
