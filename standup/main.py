"""main.py"""

import click


@click.group()
def cli():
    click.echo("standup cli")


@cli.command()
def yesterday():
    click.echo('what did you do yesterday?')


@cli.command()
def today():
    click.echo('what are you doing today?')


@cli.command()
def blocker():
    click.echo('blockers?')


if __name__ == '__main__':
    cli()
