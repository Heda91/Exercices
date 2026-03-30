"""
Given a large chunk of text, identify the most frequently occurring trigram in it.
If there are multiple trigrams with the same frequency, then print the one which occurred first.

Assume that trigrams are groups of three consecutive words in the same sentence which are separated by nothing but a single space and are case insensitive.
The size of the input will be less than 10 kilobytes.
"""
import sys

sys.stdin = open("The Trigram.txt")  # to delete

data = sys.stdin.buffer.read().splitlines()
sentences = list(map(lambda x: str(x, 'utf-8').lower().split(), data))
trigrame = {}
for sentence in sentences:
    for i in range(2, len(sentence)):
        tri = ' '.join(sentence[i - 2:i + 1])
        if tri in trigrame:
            trigrame[tri] += 1
        else:
            trigrame[tri] = 1
print(max(trigrame, key=trigrame.get))
