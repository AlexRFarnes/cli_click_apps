# fileutils.py

import typing

import click


@click.command()
@click.argument("fo", type=click.File(mode="a"))
def note(fo: typing.IO):
    """Write notes input to given file"""
    click.echo("Enter lines of text below and CTRL+C to exit.")
    try:
        while True:
            value = click.prompt(text="", prompt_suffix=">")
            fo.write(f"{value}\n")

    except click.Abort:
        click.echo(f"\nOutput written to file {fo.name}")
