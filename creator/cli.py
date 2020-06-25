
import click
from . import libs


@click.group()
def cli():
    pass


@click.command()
@click.option('--count', default=1, help='Number of greetings.')
@click.option('--name', prompt='Your name',
              help='The person to greet.')
def hello(count, name):
    """Simple program that greets NAME for a total of COUNT times."""
    for x in range(count):
        click.echo('Hello %s!' % name)


@click.command()
@click.option('--package_name', default='', help='package name')
def create_package(package_name):
    """create python package command

    Args:
        package_name (str): name of package
    """
    if package_name == '':
        raise Exception('empty package name.')
    libs.create_package(package_name=package_name)


cli.add_command(hello)
cli.add_command(create_package)
