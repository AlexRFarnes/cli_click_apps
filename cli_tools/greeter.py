# greeter.py

import click


@click.command()
@click.argument("name")
@click.option(
    "--lang",
    help="Specify language English (en) or Spanish (es)",
    default="en",
    type=click.Choice(["en", "es"]),
)
@click.option("--say-it", type=int, default=1, help="Number of times to say greeting")
def greet(name, lang, say_it):
    """Displays a greeting message to the user."""
    greetings = "Hello" if lang == "en" else "Hola"
    for _ in range(say_it):
        click.secho(f"{greetings} {name}", fg=(51, 0, 102), bg=(204, 153, 255))
