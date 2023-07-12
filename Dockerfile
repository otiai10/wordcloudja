FROM python:3.8

RUN apt-get update -qq
RUN apt-get install -y \
    mecab \
    libmecab-dev \
    mecab-ipadic-utf8 \
    xz-utils \
    git \
    make \
    curl \
    file

RUN pip install --upgrade pip
RUN pip install \
    wordcloud \
    mecab-python3

RUN git clone --depth 1 https://github.com/neologd/mecab-ipadic-neologd.git
RUN ./mecab-ipadic-neologd/bin/install-mecab-ipadic-neologd -n

ADD ./generate.py /
