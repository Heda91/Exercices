"""
A newly opened multinational brand has decided to base their company logo on the three most common characters in the company name.
They are now trying out various combinations of company names and logos based on this condition. Given a string s,
which is the company name in lowercase letters, your task is to find the top three most common characters in the string.

Print the three most common characters along with their occurrence count.
Sort in descending order of occurrence count.
If the occurrence count is the same, sort the characters in alphabetical order.
For example, according to the conditions described above,

google would have it's logo with the letters g,o,e.
"""
import sys

sys.stdin = open("Company Logo.txt")  # to delete

data = sys.stdin.buffer.read().splitlines()
s = str(data[0], 'utf-8')
letters = set(s)
occurences = sorted([[l, s.count(l)] for l in letters], key=lambda x: (1 / x[1], x[0]), reverse=False)
print(occurences[0][0], occurences[0][1])
print(occurences[1][0], occurences[1][1])
print(occurences[2][0], occurences[2][1])
