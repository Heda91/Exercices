"""
## A Basic Spell Checker

This challenge will introduce you to the basics of Spell Checking. Right from what you type in a search box,
or the red squiggles you see as you enter text via your browser, or the articles you write using an online or
offline word processor; spell checking is an important tool on the PC and on the Internet.

## Most frequent spelling mistakes

People are prone to making spelling mistakes as they type in a hurry.
It has been observed that the most common spelling mistakes occur for the following reasons:
Deletion, Replacement, Transposition, Insertion. Assume only the letters a-z are involved.
- One character in the string gets deleted incorrectly.
Example: The user enters Ordnary instead of Ordinary (i.e. leaves out the i)
- One character in the string is incorrectly replaced by another one.
Example: The user enters Accedent instead of Accident.
- While typing hurriedly, the user ends up swapping one pair of consecutive characters.
Example: The user enters Noramlly instead of Normally.
- The user ends up inserting one extra character somewhere in the string.
Example: The user enters Heello instead of Hello.

So, generally, the correct string is just one step of one edit distance away from what the user erroneously types in.
Please take note, that in each of the four popular cases above,
the mistake occurs only at one particular character (or, pair of characters in case 3).
If a spell checker is able to detect these simple but common mistakes, it will be able to handle sixty to seventy percent
of all spelling mistakes which people make while typing text on their computers.

## What you need to do

You will be provided with a Corpus of text which you can read in as a file in your program.
Assume it is placed in the same folder as your program. Read in this text, and build up a dictionary of words
and the frequencies with which those words occur. Words are string of letters, and they might contain hyphens
and/or apostrophes. The end of the corpus file is marked by "END-OF-CORPUS"
Then, via the standard input, you will be provided with a set of (possibly) mistyped words.
Your program should recommend the likeliest known word from the dictionary you built up,
for each of those mistyped words. If the given word exists in your dictionary, output it as it is.
"""

import string, sys, re
from collections import Counter

sys.stdin = open('A Basic Spell Checker.txt')


def tokenize(*texts):
    return [re.sub(r"[^\w\s]", " ", re.sub(r"[,.;']", "", t)).lower().split() for t in texts]


res = list()
data = str(sys.stdin.buffer.read(), 'utf-8').splitlines()
vocab = Counter(tokenize(open('corpus.txt', 'r').read())[0])
for word in data[1:]:
    word = word.lower()
    if word in vocab:
        res.append(word)
    else:
        deletion = [word[0:i] + l + word[i:len(word)] for i in range(len(word) + 1) for l in string.ascii_lowercase]
        replacement = [word[0:i] + l + word[i + 1:len(word)] for i in range(len(word)) for l in
                       string.ascii_lowercase]
        transposition = [word[0:i] + word[i + 1] + word[i] + word[i + 2:len(word)] for i in range(len(word) - 1)]
        insertion = [word[0:i] + word[i + 1:len(word)] for i in range(len(word))]
        possible = deletion + replacement + transposition + insertion
        possible = [(word, vocab[word]) for word in possible if word in vocab]
        if len(possible) > 0:
            res.append(min(possible, key=lambda x: (-x[1], x))[0])
        else:
            res.append(word)

# print(*res, sep='\n')
answer = ['bberant', 'bberation', 'bbrieviated', 'bbriviated', 'bbriviation', 'bscess', 'bgration', 'berrent',
          'bilites', 'bility', 'bility', 'bit of', 'bnormalites', 'london', 'bortificant', 'breviate', 'breviation',
          'rbitrary', 'bsence', 'sense', 'bsorbancy', 'bsorbant', 'bsorbsion', 'bsorption', 'bsorption', 'bsolute',
          'bundance', 'bundacies', 'bundancies', 'bundance', 'bundant', 'bundant', 'butt', 'cademy', 'cademic',
          'ccadamy', 'academy', 'ccelerate', 'ccelleration', 'ccession', 'cceptable', 'ccessible', 'ccused', 'ccesory',
          'ccidentally', 'ccidentally', 'ccidently', 'cclimitization', 'ccomadate', 'ccomadation', 'ccommodate',
          'ccommodation', 'ccompanying', 'ccompanied', 'ccordeon', 'ccordian', 'ccording', 'ccoustic', 'ccreditate',
          'ccros', 'across', 'ccused', 'cademic', 'certain', 'less', 'chieve', 'chieved', 'chievement', 'cheives',
          'cheiving', 'cheivment', 'chievement', 'hive', 'chimed', 'coward', 'colade', 'ccomplish', 'ccomplished',
          'complishment', 'cording', 'ccordingly', 'cquaintance', 'cquiantence', 'cquiantences', 'cquisition',
          'cquired', 'ctivities', 'ctual', 'ccuracy', 'custom', 'custommed', 'ctually', 'd nauseum', 'doption',
          'daptions', 'ddional', 'ddionally', 'dditinally', 'dditional', 'ddition', 'admission', 'admitted', 'adopt',
          'adopted', 'ddoptive', 'ddress', 'ddresable', 'ddressing', 'ddition', 'dequate', 'dear', 'dhearence',
          'ddition', 'dditional', 'amendment', 'dministration', 'dminstrate', 'dministration', 'dministrative',
          'dministrator', 'dmissability', 'dmissable', 'dmitted', 'dmitting', 'dmit', 'in', 'dolescent', 'cquire',
          'cquiring', 'does', 'dresable', 'dressing', 'dress', 'dressable', 'dressing', 'dvantageous', 'dvertisement',
          'oject', 'korret', 'unfortuntely', 'extraordinarily', 'goo', 'lakcsmith', 'outright', 'uniformity', 'vekste',
          'interest', 'ancing', 'stir', 'surprising', 'intelligent', 'wisom', 'trot', 'historic', 'ocurrane', 'mjor',
          'perplexe', 'equilirium', 'witthol']

diff = [i for i in range(len(res)) if res[i] != answer[i]]
print(diff, len(diff))
print(
    '\n'.join([f'{data[i + 1]} ({i}) -> {res[i]} ({vocab[res[i]]}) - {answer[i]} ({vocab[answer[i]]})' for i in diff]))
