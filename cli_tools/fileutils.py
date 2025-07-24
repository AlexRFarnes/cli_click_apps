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


@click.command()
@click.argument("inputs", type=click.File("r"), nargs=-1)
@click.argument("output", type=click.File("w"))
def concat(inputs: typing.Collection[typing.IO], output: typing.IO):
    """Concatenates the content of one or more files into an output file."""
    for f in inputs:
        for line in f:
            output.write(line)
        click.echo(f"{f.name} written to {output.name}")
