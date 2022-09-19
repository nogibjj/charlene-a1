#!/usr/bin/env python

import click
from dblib.querydb import querydb

#build a click group
@click.group()
def cli():
    """A simple CLI to query a SQL database"""

#build a click command
@cli.command()
@click.option("--query",
    default="SELECT player, win_loss_pct,mp_per_g, fg3a_per_g FROM default.nba_dataset ORDER BY win_loss_pct DESC LIMIT 5",
    help="SQL query to execute")
def cli_query(query):
    """Execute a SQL query"""
    querydb(query)

#run the CLI
if __name__ == "__main__":
    cli()