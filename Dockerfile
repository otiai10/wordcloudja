FROM python:3.8

RUN pip install --upgrade pip
RUN pip install wordcloud

ADD ./generate.py /
