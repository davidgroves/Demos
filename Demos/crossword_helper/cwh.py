#!/usr/bin/env python

import sys
import re

if __name__ == "__main__":
    expression = ("^" + sys.argv[1] + "$").replace("?", ".")
    with open("words.txt") as wordlist:
        for word in wordlist:
            if (re.search(expression, word)):
                print (word.strip())