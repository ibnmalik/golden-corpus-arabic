#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import sys
import json
import io

# Make it work for Python 2+3 and with Unicode
try:
    to_unicode = unicode
except NameError:
    to_unicode = str


WORDS, STEMS, ROOTS = sys.argv[1:] or ("core/words.txt","core/stems.txt", "core/roots.txt")

w = open(WORDS)
r = open(ROOTS)
s = open(STEMS)

word = w.readline()
root=  r.readline()
stem = s.readline()
golden_corpus = []
word_stem_root = {}
while (word and stem and root):
    word_stem_root["root"] = root[:-1].decode("utf-8")
    word_stem_root["stem"] = stem[:-1].decode("utf-8")
    word_stem_root["word"] = word[:-1].decode("utf-8")
    word = w.readline()
    root=  r.readline()
    stem = s.readline()
    golden_corpus.append(word_stem_root)
    word_stem_root = {}

# Write JSON file
with io.open('build/golden_corpus_arabic.json', 'w', encoding='utf8') as outfile:
    str_ = json.dumps(golden_corpus,
                      indent=4, sort_keys=True,
                      separators=(',', ': '), ensure_ascii=False)
    outfile.write(to_unicode(str_))
