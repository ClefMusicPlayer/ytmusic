from .common import ytm 


def get_search_results(query: str, lim: int = 50) -> list:
    return [
        {
            'id': result['videoId'],
            'title': result['title'],
            'length': result['duration'],
            'thumbnail':{
                'mini': result['thumbnails'][0]['url'],
                'large': result['thumbnails'][-1]['url']
            },
            'artists': [artist['name'] for artist in result['artists']],
            'link': f'https://music.youtube.com/watch?v={result["videoId"]}'
        }
        for result in ytm.search(query, limit=lim, filter='songs')
    ]

if __name__ == '__main__':
    import json
    json.dump(get_search_results('mudal nee mudivum nee', lim=10), open('search_results.json', 'w'), indent=4)