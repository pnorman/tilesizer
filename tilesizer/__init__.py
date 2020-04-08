import click
from fs import open_fs
import sys


@click.command()
@click.option('-s', "--suffix")
@click.argument('location')
def cli(suffix, location):
    tilefs = open_fs(location)
    weights = 0
    sizes = 0
    for line in sys.stdin.readlines():
        (filepath, weight) = line.strip().split(' ', 2)
        if suffix is not None:
            filepath += suffix
        weight = float(weight)
        weights += weight
        sizes += tilefs.getinfo(filepath, namespaces=['details']).size * weight

    print(sizes/weights)
