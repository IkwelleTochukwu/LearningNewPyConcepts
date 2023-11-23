"""Command line tool using the sys.argv"""

import sys

# Check if the script is being run as the main program
if __name__ == '__main__':
    print(f"The first argument is: '{sys.argv[0]}'")
    print(f"The second argument is: '{sys.argv[1]}'")
    print(f"The third argument is: '{sys.argv[2]}'")
    print(f"The fourth argument is: '{sys.argv[3]}'")


