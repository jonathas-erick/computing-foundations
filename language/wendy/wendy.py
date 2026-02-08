#!/usr/bin/env python3
import sys
from lexer import tokenize
from interpreter import run

def main():
    filename = sys.argv[1]
    code = open(filename).read()
    tokens = tokenize(code)
    run(tokens)

if __name__ == "__main__":
    main()
