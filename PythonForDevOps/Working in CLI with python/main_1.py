"""command line tool using argparse"""

import argparse

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Print your input to the screen")
    """Add arguments to the code"""
    parser.add_argument('message',  # Positional arguments
                        help='A message to print out')
    parser.add_argument('--twice', '-t',  # Optional arguments
                        help='Do it twice',
                        action='store_true')
    args = parser.parse_args()  # Use the parser to parse the arguments
    print(args.message)
    if args.twice:  # When you run it with the --twice flag,
        # the input message prints twice
        print(args.message)
