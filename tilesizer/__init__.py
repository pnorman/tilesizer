import click
from fs import open_fs
from fs.errors import ResourceNotFound
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
        try:
            weight = float(weight)
            sizes += tilefs.getinfo(filepath, namespaces=['details']).size * weight
            weights += weight
        except ResourceNotFound:
            pass
    print(sizes/weights)
