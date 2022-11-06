#!/usr/bin/env python

import click
from query_demo import query_db

# build a click group
@click.group()
def cli():
    """A simple CLI get the average rating for a given writer/director"""


# build a click command
@cli.command()
@click.option(
    "--person",
    default="Francis Ford Coppola",
    help="Person involved in film (writer/director)",
)
@click.option(
    "--role",
    default="directors",
    help="Role of person (writer/director)",
)
def cli_rating(person, role):
    """Execute prediction"""
    rating = query_db(role, person)
    print(rating)


# run the CLI
if __name__ == "__main__":
    cli()