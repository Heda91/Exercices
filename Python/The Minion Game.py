"""
Kevin and Stuart want to play the 'The Minion Game'.

## Game Rules

Both players are given the same string, S.
Both players have to make substrings using the letters of the string S.
Stuart has to make words starting with consonants.
Kevin has to make words starting with vowels.
The game ends when both players have made all possible substrings.

## Scoring

A player gets +1 point for each occurrence of the substring in the string S.

## For Example:

String S = "BANANA"
Kevin's vowel beginning word = "ANA"
Here, "ANA" occurs twice in "BANANA". Hence, Kevin will get 2 Points.
"""

import sys

sys.stdin = open("The Minion Game.txt")  # to delete

data = sys.stdin.buffer.read().splitlines()
s = str(data[0], 'utf-8')


def minion_game(string: str):
    VOWELS = {'A', 'E', 'I', 'O', 'U'}
    vowels_pts, consonants_pts = 0, 0
    for i, char in enumerate(string):
        if char in VOWELS:
            vowels_pts += len(string) - i
        else:
            consonants_pts += len(string) - i
    if vowels_pts > consonants_pts:
        print("Kevin", vowels_pts)
    elif vowels_pts < consonants_pts:
        print("Stuart", consonants_pts)
    else:
        print("Draw")


minion_game(s)
