import spotipy
import spotipy.util as util
from pprint import pprint

def connect(username, scope, client_id, client_secret, redirect_uri):
    token = util.prompt_for_user_token(username, scope, client_id, client_secret, redirect_uri)
    spotify = spotipy.Spotify(auth=token)
    return spotify

def print_curr_playing(spotify):
    curr_playing = spotify.currently_playing()

    if curr_playing:
        print(f"{curr_playing['item']['name']} by {curr_playing['item']['artists'][0]['name']} is currently playing.")
    else:
        print("There is no music playing")

def get_artist_top_songs(spotify, artist_name):
    search = spotify.search(artist_name, limit=1, type="artist")
    uri = search["artists"]["items"][0]['uri']
    artist = spotify.artist(uri)
    artist_top_tracks = spotify.artist_top_tracks(uri)

    print(f"Artist: {artist['name']}\n")
    i = 1
    for song in artist_top_tracks["tracks"]:
        print(f"{i}: {song['name']} from the {song['album']['album_type']} {song['album']['name']}")
        i+=1
    print()