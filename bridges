#!/usr/bin/env python3

import sys

def main():
    if len(sys.argv) <= 1:
        sys.exit('No puzzles to solve')
    else:
        try:
            with open(sys.argv[1], encoding='utf-8') as puzzle_file:
                pass

        except FileNotFoundError as e:
            sys.exit('Could not find the puzzle file ‘{}’'.format(sys.argv[1]))

        except IOError as e:
            sys.exit('Error reading the puzzle file ‘{}’'.format(sys.argv[1]))


if __name__ == '__main__':
    main()
