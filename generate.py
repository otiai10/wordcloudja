#!/usr/bin/env python
"""
This document is based on https://github.com/amueller/word_cloud/blob/main/examples/simple.py
https://github.com/amueller/word_cloud
See https://github.com/amueller/word_cloud/blob/main/LICENSE
"""

import os

from os import path
from wordcloud import WordCloud

# Read the whole text.
text = open(path.join('/data', 'constitution.txt')).read()

# Generate a word cloud image
wordcloud = WordCloud().generate(text)

# lower max_font_size
wordcloud = WordCloud(max_font_size=40).generate(text)

# The pil way (if you don't have matplotlib)
image = wordcloud.to_image()
image.save('/data/output.png')
