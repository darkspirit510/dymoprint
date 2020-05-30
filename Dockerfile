FROM python:buster

RUN apt update && \
    apt install printer-driver-dymo -y

COPY . /dymoprint

WORKDIR /dymoprint
CMD python frontend.py
