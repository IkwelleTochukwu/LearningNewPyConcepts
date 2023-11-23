"""Command line tool using the sys.argv"""

import sys


def greet(greeting, target):
    message = f'{greeting} {target}!'
    print(message)


# Check if the script is being run as the main program
if __name__ == '__main__':
    greeting = "Hello"
    target = "Tochukwu"

    if '--help' in sys.argv:
        # print usage pattern for running script
        help_message = f'Usage: python {sys.argv[0]} --name <NAME> --greeting <GREETING>'  # In windows cli
        print(help_message)
        sys.exit()

    if '--name' in sys.argv:
        # Get the position after the name flag
        name_index = sys.argv.index('--name') + 1
        if name_index < len(sys.argv):
            name = sys.argv[name_index]
        else:
            print('Error: Please provide a value for --name')
            sys.exit()

    if '--greeting' in sys.argv:
        # Get position after greeting flag
        greeting_index = sys.argv.index('--greeting') + 1
        if greeting_index < len(sys.argv):
            greeting = sys.argv[greeting_index]

    greet(greeting, name)
