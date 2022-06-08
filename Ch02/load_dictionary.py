"""Load a text file as a list"""

import sys

def load(filename):
    """Takes a filename and returns text in list of lowercase strings"""
    try:
        with open(filename,"r") as file:
            text = file.read().strip().split("\n")
            text = [word.lower() for word in text]
            return text

    except IOError as e:
        print("{}\nError opening {}. Terminating program.".format(e, filename),
              file=sys.stderr)
        sys.exit(1)
