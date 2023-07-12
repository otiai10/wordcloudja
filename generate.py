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

# Read the whole text.
a = sys.argv[1]
# text = open(path.join('/data', a)).read()
text = open(a).read()

# Generate a word cloud image
wordcloud = WordCloud().generate(text)

# lower max_font_size
wordcloud = WordCloud(max_font_size=40).generate(text)

# The pil way (if you don't have matplotlib)
image = wordcloud.to_image()
output = path.join(a + '.png')
image.save(output)

print(output)
