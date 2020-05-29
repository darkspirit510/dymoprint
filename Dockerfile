FROM python:slim-buster

COPY . /dymoprint

CMD python /dymoprint/frontend
