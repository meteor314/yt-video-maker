# Reddit Video Collector 🔍🎥

<div align="center">
    <img src="https://i.imgur.com/pAiDEYr.png" height="96px" weight='48px'>

[![Python](https://img.shields.io/badge/python-v3.6+-blue.svg)](https://www.python.org/)
[![FFmpeg](https://img.shields.io/badge/FFmpeg-v4.4-blue)](https://ffmpeg.org/)
[![Reddit](https://img.shields.io/badge/Reddit-API-orange)](https://www.reddit.com/dev/api/)
[![YouTube](https://img.shields.io/badge/YouTube-API-red)](https://developers.google.com/youtube/v3)

</div>

This script collects data from the PublicFreakout subreddit of Reddit. Specifically, it retrieves information about the top videos that were posted in the last 24 hours and contain video content. The videos are sorted by most upvoted.

## Dependencies

- requests
- json
- datetime
- [ffmpeg](https://ffmpeg.org/download.html)

## Customization

To get video from another subreddit, change `URL` to the subreddit you want to get videos from. For example, to get videos from r/entitledparents, change the URL to `https://www.reddit.com/r/entitledparents/top.json?sort=top&t=day&limit=100`

## Disclaimer

This script is intended for educational and non-commercial use only. The authors of this script are not responsible for any misuse or illegal use of this script. The authors do not encourage or condone any activity that violates the terms of service of Reddit. By using this script, you agree to comply with the terms of service of Reddit.

## Usage

- Install dependencies by running

```python
pip install -r requirements.txt
```

- Run the script by typing

```python
python reddit.py
```

- The script will retrieve information about the top PublicFreakout videos from Reddit and store it in a JSON file called `reddit.json`
- The script will print the time the data was collected and the total number of videos collected
- If any error occurs during the process, the script will return an error message.

## To-Do

- [ ] Add functionality to automatically post all collected videos to YouTube with a timeline and description for each video. You will need to have a YouTube account, create a new project in the [Google Developers Console](https://console.developers.google.com), and obtain a `client_secret.json` file to authenticate with YouTube's API.
- [ ] Customize the description of the videos to include information from the original Reddit post, such as the title, upvotes, and post link.
- [x] Use `ffmpeg` to download and convert the video format to comply with YouTube's upload requirements.
- [ ] Schedule the script to run automatically on a regular basis using a task scheduler, such as [cron](https://en.wikipedia.org/wiki/Cron) (on Linux/Mac) or [Task Scheduler](https://docs.microsoft.com/en-us/windows/win32/taskschd/task-scheduler-start-page) (on Windows).

## License

This script is licensed under the [MIT License](https://opensource.org/licenses/MIT).
