# fileutils.py

import typing

import click
import requests


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


@click.command()
@click.argument("inputs", nargs=-1)
def download(inputs):
    """Download web resources from (url, filename) input paris.
    Example:
        download http://xyz.com/p1.txt,page1.txt http://xyz.com/p2.txt,page2.txt

        This fetches web resources by url and saves them locally to a filename.
    """
    with click.progressbar(
        length=len(inputs),
        show_eta=False,
        item_show_func=lambda fname: f"Downloading {fname}",
    ) as bar:
        for idx, item in enumerate(inputs, start=1):
            url, file_name = item.split(",")
            resp = requests.get(url)
            with open(file_name, "w") as fo:
                fo.write(resp.text)
            bar.update(idx, file_name)

    click.echo("Download complete.")
