"""Use sys to write a script that prints command line only when
run from the command line."""

import sys

if __name__ == "__main__":
    if len(sys.argv) > 1:
        print("command line")
    else:
        print("This code is not running from the command line")