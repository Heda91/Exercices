"""
An Introduction to Sentence Segmentation

Sentence segmentation, means, to split a given paragraph of text into sentences, by identifying the sentence boundaries.
In many cases, a full stop is all that is required to identify the end of a sentence, but the task is not all that simple.

This is an open ended challenge to which there are no perfect solutions. Try to break up given paragraphs into text into individual sentences.
Even if you don't manage to segment the text perfectly, the more sentences you identify and display correctly, the more you will score.

1. Abbreviations: {Dr. W. Watson is amazing.} In this case, the first and second "." occurs after Dr (Doctor) and W (initial in the person's name)
and should not be confused as the end of the sentence.
2. Sentences enclosed in quotes: {"What good are they? They're led about just for show!" remarked another.} All of this, should be identified as just one sentence.
3. Questions and exclamations: {Who is it?} -This is a question. This should be identified as a sentence. {I am tired!}: Something which has been exclaimed.
This should also be identified as a sentence.
"""

import sys
import re

sys.stdin = open("From Paragraphs to Sentences.txt")  # to delete

data = sys.stdin.buffer.read().splitlines()
paragraph = str(data[0], 'utf-8')
sentences = re.split('([.?!](?=(?:[^"]*"[^"]*")*[^"]*$))\s+', paragraph)
sentences = [sentences[i - 1] + sentences[i] for i in range(1, len(sentences), 2)]
print('\n'.join(sentences))
