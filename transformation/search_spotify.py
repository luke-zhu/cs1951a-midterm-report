import spotipy
from spotipy import oauth2
import json

client_id = 'c8b71a74043047c3b020dec821679d66'
client_secret = 'ce38452a2a134b88a68b0d07006e7212'

prefix_url = 'https://api.spotify.com/v1/'

client_credentials_manager = oauth2.SpotifyClientCredentials(client_id, client_secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

def get_artist(record):
    r = sp.search(q='artist:' + record['artist'], type='artist')
    if r['artists']['items']:
        artist = r['artists']['items'][0]
        # print(artist['genres'])
        return artist

if __name__ == '__main__':
    with open('../year-end_data.json', 'r') as f:
        data = json.load(f)

    data.sort(key=lambda record: record['year'])
    print(data)
    artists = []
    year = 1959

    for record in data:
        if year != record['year']:
            with open('../spotify_data-' + str(year) + '.json', 'w') as g:
                json.dump(artists, g)
            
            year = record['year']
            artists = []

        artists.append(get_artist(record))

    with open('../spotify_data-' + str(year) + '.json', 'w') as g:
                json.dump(artists, g)