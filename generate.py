#!/usr/bin/env python
"""
This document is based on https://github.com/amueller/word_cloud/blob/main/examples/simple.py
https://github.com/amueller/word_cloud
See https://github.com/amueller/word_cloud/blob/main/LICENSE
"""

import os
import sys
from os import path
from wordcloud import WordCloud
import MeCab

a = sys.argv[1]
text = open(a).read()

tagger = MeCab.Tagger()
node = tagger.parseToNode(text)

# 名詞のみ取り出す
word_list = []
while node:
    word_type = node.feature.split(',')[0]
    if word_type in ["名詞"]:
        word_list.append(node.surface)
    node = node.next

# 一本のインプットにする
words = ' '.join(word_list)
# print(words)

font_path = '/usr/share/fonts/opentype/ipafont-gothic/ipagp.ttf'
# Generate a word cloud image
wordcloud = WordCloud(
    width=800,
    height=900,
    font_path=font_path,
).generate(words)

# lower max_font_size
# wordcloud = WordCloud(max_font_size=40).generate(text)

# The pil way (if you don't have matplotlib)
image = wordcloud.to_image()
output = path.join(a + '.png')
image.save(output)

print(output)