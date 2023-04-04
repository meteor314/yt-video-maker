import requests
import json
from datetime import datetime

# list PublicFreakout videos of reddit that contain o video and a title of last 24 hours sorted by most upvoted


def reddit():
    try:
        response = requests.get(
            'https://www.reddit.com/r/PublicFreakout/top.json?t=day&limit=30')

        response.raise_for_status()

        data = response.json()
        videos = [item for item in data['data']['children'] if item['data'].get(
            'media') and item['data']['media'].get('reddit_video')]

        result = []
        for item in videos:
            result.append({
                'title': item['data']['title'],
                'video': item['data']['media']['reddit_video']['fallback_url'],
                'url': item['data']['url'],
                'totalVotes': item['data']['ups'],
                'postedBy': item['data']['author'],
                'date': datetime.fromtimestamp(item['data']['created_utc']).strftime('%Y-%m-%d %H:%M:%S')
            })

        # write data to file
        with open('reddit.json', 'w') as f:
            json.dump(result, f)

        return result
    except Exception as e:
        return {'message': str(e)}


if __name__ == '__main__':
    result = reddit()
    print(result)
