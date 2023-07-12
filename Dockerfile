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
    file \
    sudo \
    fonts-ipafont-gothic

RUN pip install --upgrade pip
RUN pip install \
    wordcloud \
    mecab-python3 \
    unidic-lite

RUN git clone --depth 1 https://github.com/neologd/mecab-ipadic-neologd.git
RUN yes yes | ./mecab-ipadic-neologd/bin/install-mecab-ipadic-neologd -n -a

ADD ./generate.py /
