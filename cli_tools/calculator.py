# calculator.py

import click


@click.command()
@click.argument("xs", type=int, nargs=-1)
@click.option("-v", "--verbose", help="Show additional output", count=True)
def add(xs, verbose):
    """Adds numbers."""
    if verbose > 1:
        steps = []
        result = 0
        for x in xs:
            steps.append(x)
            result += x
            click.echo(f"{' + '.join(str(s) for s in steps)} = {sum(steps)}")
    elif verbose == 1:
        click.echo(f"{' + '.join(str(x) for x in xs)} = {sum(xs)}")
    else:
        click.echo(sum(xs))


@click.command()
@click.argument("xs", type=int, nargs=-1)
@click.option("-vv", "--verbose", help="Show additional output", is_flag=True)
def subtract(xs, verbose):
    """Subtracts numbers."""
    xs = [xs[0]] + [-x for x in xs[1:]]
    if verbose:
        click.echo(f"{xs[0]} {' '.join(str(x) for x in xs[1:])} = {sum(xs)}")
    click.echo(sum(xs))
