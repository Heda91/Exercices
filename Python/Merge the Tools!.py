"""
Consider the following:

A string, s, of length n where s=c0c1...cn-1.
An integer, k, where k is a factor of n.
We can split s into {n/k} substrings where each subtring, {ti}, consists of a contiguous block of k characters in s.
Then, use each ti to create string {ui} such that:
- The characters in {ui} are a subsequence of the characters in {ti}.
- Any repeat occurrence of a character is removed from the string such that each character in {ui} occurs exactly once.
In other words, if the character at some index j in {ti} occurs at a previous index <j in {ti}, then do not include the character in string .
Given s and k, print {n/k} lines where each line i denotes string {ui}.

## Example
s = "AAABCADDE"
k = 3
There are three substrings of length 3 to consider: 'AAA', 'BCA' and 'DDE'.
The first substring is all 'A' characters, so {u1 = "A"}.
The second substring has all distinct characters, so {u2 = "BCA"}.
The third substring has 2 different characters, so {u3 = "DE"}.

Note that a subsequence maintains the original order of characters encountered.
The order of characters in each subsequence shown is important.
"""

import sys

sys.stdin = open("Merge the Tools!.txt")  # to delete

data = sys.stdin.buffer.read().splitlines()
s = str(data[0], 'utf-8')
k = int(data[1])


def merge_the_tools(s: str, k: int) -> None:
    t = [s[i:i + k] for i in range(0, len(s), k)]
    u = list()
    for t_i in t:
        u_i = str()
        for c in t_i:
            if c not in u_i:
                u_i += c
        u.append(u_i)
    print('\n'.join(u))


merge_the_tools(s, k)
