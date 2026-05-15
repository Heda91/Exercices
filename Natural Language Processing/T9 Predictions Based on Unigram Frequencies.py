"""
On the old Nokia and Verizon phones, when the complete keyboard was absent, users were expected to use
their numeric keypad with just 9 keys to type in all 26 characters of the English alphabet.
The keys and the corresponding letters were:
- 2 abc
- 3 def
- 4 ghi
- 5 jkl
- 6 mno
- 7 pqrs
- 8 tuv
- 9 wxyz
If a person types in '2' he could mean either 'a' or 'b' or 'c'.
If a person types in 23 he could mean either [ad or ae or af or bd or be or bf or cd or ce or cf].
In this problem, we try to guess, that if the person keys in a particular sequence of numeric keys on the keypad,
what is the most likely word which he was trying to enter?

## An outline of steps for building a Unigram model

A dictionary of commonly used words be provided to you.
Apart from that you are also provided a large corpus of text. Using this corpus of text, you can compute
the frequency with which commonly used words (from the dictionary) occur in the corpus. i.e., you are computing
Unigram Frequencies, using the corpus. There might be words in the corpus which are missing in the dictionary:
these words can be ignored. But do not ignore words which are present in the dictionary and absent in the corpus.

## Predicting the word, given a series of numerals

After you read the dictionary and corpus and build the language model, you are given a number of numeric sequences
typed in by a phone user. You need to identify words from the dictionary which start with a character sequence
which could be represented by these numerals. Identify the top five candidates with the highest frequency,
and output them in one line, separated by semi-colons. If there are less than five possible candidates,
display them all. If there is no possible candidate, display: No Suggestions

Most likely word is the one which occurs max times in the given corpus, least likely is the one which occurs least times
in the given corpus (or, perhaps it is a word which exists only in the dictionary and did not occur at all in the corpus).

## Dictionary and Corpus File

For the purpose of building the word frequency and unigram model, you are provided with a file
"t9Dictionary.txt" and "t9TextCorpus.txt" which will be kept in the same folder as the one from which your program is being run.
- The first file t9Dictionary.txt, is the dictionary. First line contains N, N words follow each in a new line.
- The second file is the training corpus t9TextCorpus.txt of text. This ends with "END-OF-CORPUS" on a new line.

## Defining a word

A word is a sequence of characters (a-z, lowercase or uppercase; hyphen or apostrophe) which always starts and ends
with a letter (a-z, lowercase or uppercase). The regex used must be greedy.
"""
import sys, re
from collections import Counter

sys.stdin = open('T9 Predictions Based on Unigram Frequencies.txt')

# lien entre les lettres et les chiffres sur un clavier de nokia
LTR_TO_NBR = {'a': '2', 'b': '2', 'c': '2', 'd': '3', 'e': '3', 'f': '3', 'g': '4', 'h': '4', 'i': '4',
              'j': '5', 'k': '5', 'l': '5', 'm': '6', 'n': '6', 'o': '6', 'p': '7', 'q': '7', 'r': '7', 's': '7',
              't': '8', 'u': '8', 'v': '8', 'w': '9', 'x': '9', 'y': '9', 'z': '9', "'": "", '-': ''}


def tokenize(text: str) -> list[str]:
    """
    Formalise le texte et renvoie une liste de mot
    :param text: Une chaine de caractère
    :return: La liste des mots du texte formalisé
    """
    l = list()
    for t in text.lower().splitlines():
        t = re.sub(r"[^\w\s'-]", "", t)
        t = re.sub(r"(?:\A|\s)(?![a-z](?:[a-z'-]*[a-z])?(?=\Z|\s))\S+", "", t)
        l.extend(t.split())
    return l


def word_to_nbr(word: str) -> str:
    """
    Transforme un mot en suite de chiffre suivant un clavier de nokia
    :param word: Le mot à chiffrer
    :return: Une suite de chiifre
    """
    return ''.join([LTR_TO_NBR[w] for w in word])


data = str(sys.stdin.buffer.read(), 'utf-8').splitlines()[1:]
dictionary = Counter(open('t9Dictionary.txt', 'r').read().splitlines()[1:])
corpus = Counter(tokenize(open('t9TextCorpus.txt', 'r').read()))

# chiffrage de chaque mot du dictionnaire + ajout de la rareté du mot
nbr_to_word: dict[str, list[str]] = dict()
for w in dictionary.keys():
    if w in corpus.keys():
        dictionary[w] += corpus[w]  # ajoute le nb d'appartion dans le corpus
    nb = word_to_nbr(w)
    if nb in nbr_to_word:  # si un autre mot à le meme chiffrage (ex: 762538 = 'socket' et 'pocket')
        nbr_to_word[nb].append(w)
    else:
        nbr_to_word[nb] = [w]

result: list[str] = list()
for d in data:
    possible = [w for nb in nbr_to_word.keys() for w in nbr_to_word[nb] if
                nb.startswith(d)]  # cherche tous les mots du dictionnaire commancant par cette signature
    bests = sorted(possible, key=lambda x: (-dictionary[x], x))  # trie par le +grand (+petit negatif) puis alphabetique
    if len(bests) > 0:
        result.append(';'.join(bests[:5]))  # ajoute les 5(max) mots les plus probables
    else:
        result.append("No Suggestions")  # si aucun match
print(*result, sep='\n')
