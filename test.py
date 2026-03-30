import sys, re

sys.stdin = open("test.txt")  # to delete

data = str(sys.stdin.buffer.read(), 'utf-8').splitlines()
for d in data[1:]:
    print(re.compile(d))
