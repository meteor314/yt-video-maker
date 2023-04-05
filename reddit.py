import requests
import json
from datetime import datetime

# list PublicFreakout videos of reddit that contain o video and a title of last 24 hours sorted by most upvoted


def reddit():
    URL = 'https://www.reddit.com/r/PublicFreakout/top.json?t=day&limit=30'
    try:
        response = requests.get(URL, headers={
                                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36'}
                                )

        response.raise_for_status()

        data = response.json()
        videos = [item for item in data['data']['children'] if item['data'].get(
            'media') and item['data']['media'].get('reddit_video')]

        result = []
        for item in videos:
            result.append({
                'title': item['data']['title'],
                'video': item['data']['media']['reddit_video']['fallback_url'],
                'upvote': item['data']['ups'],
                'downvote': item['data']['downs'],
                'duration': item['data']['media']['reddit_video']['duration'],
                'thumbnail': item['data']['thumbnail'],
                'post_link': 'https://www.reddit.com' + item['data']['permalink'],
                'posted_by': item['data']['author'],
                'audio': item['data']['media']['reddit_video']['fallback_url'].replace('DASH_480', 'DASH_audio')

            })

        with open(f"reddit.json", 'w') as f:
            json.dump(result, f, indent=4)

        print(
            f"Reddit data collected at {datetime.now().strftime('%H:%M:%S')}")
        print(f"Total videos: {len(result)}")

        return result
    except Exception as e:
        return {'message': str(e)}


reddit()
print('Done')
