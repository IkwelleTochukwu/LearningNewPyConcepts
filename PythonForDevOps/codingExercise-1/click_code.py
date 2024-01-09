"""Use click to create a command-line tool that takes a name
as an argument and prints it if it does not begin with a p.
"""
import click


@click.command()
@click.argument('name', type=str)
def show_name(name):
    if name.lower().startswith('p'):
        pass
    else:
        click.echo(name)


if __name__ == "__main__":
    show_name()
