from .common import ytm


def get_recommendations(video_id: str, lim: int = 50) -> list:
    tracks = ytm.get_watch_playlist(video_id, limit=lim)
    playlist_id = tracks['playlistId']
    return [
        {
            'id': track['videoId'],
            'title': track['title'],
            'length': track['length'],
            'thumbnail':{
                'mini': track['thumbnail'][0]['url'],
                'large': track['thumbnail'][-1]['url']
            },
            'artists': [artist['name'] for artist in track['artists']],
            'link': f'https://music.youtube.com/watch?v={track["videoId"]}&list={playlist_id}'
        }
        for track in tracks['tracks']
    ]

if __name__ == '__main__':
    import json
    json.dump(get_recommendations('HndZrAOzd9E'), open('watch_playlist.json', 'w'), indent=4)