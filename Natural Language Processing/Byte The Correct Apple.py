"""
The word "Apple" could generally refer to one of these two:
(a) Apple Inc., the great Computer giant.
(b) Apple, the fruit

You are provided a text file, with a number of lines.
Each line contains either a sentence or a paragraph or a text snippet which could either be related to Apple,
the computer company, or the apple, the fruit.
Your task is to perform disambiguation between these two groups and identify which one is being referred to.
It is possible that the plural or the possessive form of Apple might exist in some of the tests (apples, Apple's).

## Training Data
You are provided with two text files, which contain near-complete text from the Wikipedia
for Apple Inc. as well as apple the fruit.
Also, you can assume that these two text files are available in the directory where your program is run,
and their names are "apple-computers.txt" and "apple-fruit.txt".
"""
import sys, re, math
import numpy as np

sys.stdin = open('Byte The Correct Apple.txt')

data = str(sys.stdin.buffer.read(), 'utf-8').splitlines()
A = data[1:]
B = [open('apple-computers.txt', 'r', encoding='utf-8').read(), open('apple-fruit.txt', 'r', encoding='utf-8').read()]


def vector_tf_idf(*texts: str):
    texts = [re.sub(r"[^\w\s]|'s", " ", re.sub(r"[,.;]", "", t)).lower().split() for t in texts]
    words = sorted(set(sum(texts, [])))
    vector = np.empty((len(texts), len(words)), dtype=float)
    for i, t in enumerate(texts):
        vector[i] = [t.count(w) / len(t) for w in words]
    for i in range(len(words)):
        vector[:, i] *= math.log(len(texts) / np.count_nonzero(vector[:, i]).astype(int))
    return vector


def cosin_sim_matrix(XA, XB):
    XA = XA / np.linalg.norm(XA, axis=1, keepdims=True)
    XB = XB / np.linalg.norm(XB, axis=1, keepdims=True)
    return np.dot(XA, XB.T)


X = vector_tf_idf(*A + B)
XA = X[:len(A)]
XB = X[len(A):]
sim_matrix = cosin_sim_matrix(XA, XB)

matches = np.argmax(sim_matrix, axis=1)
# ----- verification
result = ['computer-company' if n == 0 else 'fruit' for n in matches]
answer = ['computer-company', 'fruit', 'fruit', 'computer-company', 'fruit', 'computer-company', 'computer-company',
          'fruit', 'fruit', 'computer-company', 'fruit', 'computer-company', 'computer-company', 'fruit',
          'computer-company', 'fruit', 'fruit', 'fruit', 'fruit', 'computer-company', 'fruit', 'computer-company',
          'computer-company', 'computer-company', 'fruit', 'computer-company', 'fruit', 'computer-company', 'fruit',
          'fruit', 'fruit', 'fruit', 'computer-company', 'fruit', 'computer-company', 'fruit', 'computer-company',
          'fruit', 'computer-company', 'fruit', 'fruit', 'fruit', 'fruit', 'fruit', 'computer-company',
          'computer-company', 'computer-company', 'computer-company', 'fruit', 'computer-company', 'computer-company',
          'computer-company', 'computer-company', 'fruit', 'computer-company', 'fruit', 'computer-company',
          'computer-company', 'computer-company', 'fruit', 'fruit', 'fruit', 'computer-company', 'fruit',
          'computer-company', 'fruit', 'fruit', 'computer-company', 'fruit', 'computer-company', 'fruit', 'fruit',
          'fruit', 'fruit', 'computer-company', 'fruit', 'computer-company', 'fruit', 'computer-company',
          'computer-company', 'computer-company', 'computer-company', 'fruit', 'fruit', 'computer-company',
          'computer-company', 'computer-company', 'fruit', 'fruit', 'computer-company', 'fruit', 'fruit', 'fruit',
          'computer-company', 'computer-company', 'computer-company', 'fruit', 'computer-company', 'computer-company',
          'computer-company']
diff = [i for i in range(len(result)) if result[i] != answer[i]]
print(diff, len(diff))
print('\n'.join([f'{answer[i]} - {A[i]}' for i in diff]))
