# authenticate.py

import click


@click.command()
def auth():
    """Provides user authentication"""
    username = click.prompt(text="Username")
    password = click.prompt(text="Password", hide_input=True, confirmation_prompt=True)

    if click.confirm(text="Are you an admin?"):
        admin_id = click.prompt(text="Admin ID", type=int, prompt_suffix=">")
        click.echo(f"Loggin in admin {username} (ID={admin_id})")
    else:
        click.echo(f"Logging in {username}")
