import numpy as np
import sys, re, math

sys.stdin = open('Stitch the Torn Wiki.txt')

data = str(sys.stdin.buffer.read(), 'utf-8').splitlines()
N = int(data[0])
A = data[1:N + 1]  # débuts
B = data[N + 2:]  # fins


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
print('\n'.join((matches + 1).astype(str)))
