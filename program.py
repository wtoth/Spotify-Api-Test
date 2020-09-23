import os
from api import connect, print_curr_playing, get_artist_top_songs
from pprint import pprint
import spotipy
import spotipy.util as util
from spotipy.oauth2 import SpotifyClientCredentials

os.environ["SPOTIPY_CLIENT_ID"] = '<client_id>'
os.environ["SPOTIPY_CLIENT_SECRET"] = '<client_secret>'

username = "<username>"
scope = "user-read-currently-playing"
redirect_uri = "http://localhost:5000/callback/"

def main():
    spotify = connect(username, scope, os.getenv("CLIENT_ID"), os.getenv("CLIENT_SECRET"), redirect_uri)

    artist_name = input("What Artist do you want to search for? ")
    get_artist_top_songs(spotify, artist_name)
    print_curr_playing(spotify)


if __name__ == "__main__":
    main()