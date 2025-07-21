# greeter.py

import click


@click.command()
@click.argument("first_name")
@click.argument("last_name")
def greet(first_name, last_name):
    """Displays a greeting message to the user."""
    click.echo(f"Hello {first_name} {last_name}")
