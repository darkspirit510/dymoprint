FROM python:buster

COPY . /dymoprint

WORKDIR /dymoprint
CMD python frontend.py
