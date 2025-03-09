import click
from dotenv import load_dotenv

import music_manager


@click.group()
@click.version_option()
def cli():
    "A personal app to help me manage my playlists and other things on Spotify."
    load_dotenv()


@cli.group()
def spotify():
    "Interact with spotify"


@spotify.command(name="login")
def spotify_login():
    "Login to Spotify account"
    music_manager.spotify.login()
    click.echo("Spotify login successful!")

@spotify.command(name="download")
def spotify_download():
    music_manager.spotify.download()




@cli.command(name="command")
@click.argument("example")
@click.option(
    "-o",
    "--option",
    help="An example option",
)
def first_command(example, option):
    "Command description goes here"
    click.echo("Here is some output")
