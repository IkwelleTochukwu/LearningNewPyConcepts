"""
Simple fire example
"""
import fire


def greet(greeting='Hello', name='Tochukwu'):
    print(f'{greeting}, {name}')


def goodbye(say='Bye', name='Tochukwu'):
    print(f'{say}, {name}')


if __name__ == '__main__':
    # fire.Fire(greet)
    fire.Fire()  # expose multiple methods automatically by invoking fire with no arguments
