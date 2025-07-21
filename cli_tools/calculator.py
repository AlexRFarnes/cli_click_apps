# calculator.py

import click


@click.command()
@click.argument("xs", type=int, nargs=-1)
def add(xs):
    """Adds numbers."""
    click.echo(sum(xs))


@click.command()
@click.argument("xs", type=int, nargs=-1)
def subtract(xs):
    """Subtracts numbers."""
    xs = [xs[0]] + [-x for x in xs[1:]]
    click.echo(sum(xs))
