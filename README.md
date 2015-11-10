A solver in Python for the *Bridges* puzzle found in the **i** newspaper

How to play
===========

Each instance of the puzzle features a grid populated by islands, and the aim is
to join the islands with bridges to create one interconnected group. Bridges can
run vertically or horizontally on the grid (but cannot intersect), with at most
two bridges between any pair of islands.  Islands are denoted by circles on the
grid, containing a number that specifies how many bridges must terminate on that
island.

File formats
============

Puzzles
-------

Puzzle files are in plaintext, with a single line for each row of the grid.
Islands are represented by a single digit, specifying the number of bridges
terminating there (at most 8, as per the rules of the game). Empty spaces on
the board are represented by the space character.

Solutions
---------

Solution files extend the puzzle file format with the addition of bridges,
represented by the following Unicode characters:

 * Horizontal bridge — ‘`─`’ (U+2500, ‘box drawings light horizontal’)
 * Vertical bridge — ‘`│`’ (U+2502, ‘box drawings light vertical’)
 * Horizontal double bridge — ‘`═`’ (U+2550, ‘box drawings double horizontal’)
 * Vertical double bridge — ‘`║`’ (U+2551, ‘box drawings double vertical’)
