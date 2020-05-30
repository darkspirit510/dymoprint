FROM python:buster

RUN apt update && \
    apt install printer-driver-dymo -y

COPY . /dymoprint

WORKDIR /dymoprint

RUN pip install -r requirements.txt

CMD python frontend.py
