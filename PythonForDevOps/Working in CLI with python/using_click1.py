"""Simple click example"""

import click


@click.command()
@click.option('--greeting', default='Kedu', help='How do you want to greet?')
@click.option('--name', default='Tochukwu', help='Who do you want to greet?')
def greet(greeting, name):
    print(f'{greeting}, {name}')


if __name__ == '__main__':
    greet()
