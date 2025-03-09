from pathlib import Path
from pprint import pformat
import spotipy
import yaml
from dotenv import load_dotenv
from spotipy.oauth2 import SpotifyOAuth
import click
from platformdirs import user_data_dir

SPOTIFY_OAUTH_SCOPES = (
    "user-library-modify",
    "user-library-read",
    "playlist-read-private",
    "playlist-read-collaborative",
    "playlist-modify-private",
    "playlist-modify-public",
    "ugc-image-upload",
)


class Spotify:
    
    def connect(self):
        self._client = spotipy.Spotify(
        auth_manager=SpotifyOAuth(
            scope=",".join(SPOTIFY_OAUTH_SCOPES), redirect_uri="http://localhost:26984"
        )
    )
        
    def get_playlists(self):
        current_user_playlists = []
        if (current_user := self._client.me()) is not None:
            fetched_playlists = self._client.current_user_playlists()

            while fetched_playlists:
                for playlist in fetched_playlists["items"]:
                    if playlist["owner"]["id"] == current_user["id"]:
                        current_user_playlists.append(playlist)

                fetched_playlists = self._client.next(fetched_playlists) if fetched_playlists["next"] else None

        keep_keys = [
            "id",
            "name",
            "description",
            "public",
        ]

        current_user_playlists = [
            {
                k: pl[k]
                for k
                in pl.keys()
                if k in keep_keys
            }
            for pl
            in current_user_playlists
        ]

            
        return current_user_playlists
        
    


def login():
    "Login to Spotify account"
    Spotify().connect()

def download():
    "Download playlists from Spotify"

    spotify = Spotify()
    spotify.connect()
    playlists = spotify.get_playlists()

    
    out_dir = Path(user_data_dir('music-manager', ensure_exists=True))
    out_path = out_dir / "playlist-db.yaml"


    out_path.write_text(yaml.dump(playlists))


def upload():
    "Upload playlists to Spotify"
