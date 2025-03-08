import click


@click.group()
@click.version_option()
def cli():
    "A personal app to help me manage my playlists and other things on Spotify."


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
