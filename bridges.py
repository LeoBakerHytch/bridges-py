#!/usr/bin/env python3

import sys
import bridges.io

def main():
    if len(sys.argv) <= 1:
        sys.exit('No puzzles to solve')

    else:
        puzzle = bridges.io.load_puzzle(sys.argv[1])

if __name__ == '__main__':
    main()
