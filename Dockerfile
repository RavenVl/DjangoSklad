FROM python:3.12-alpine
COPY requirements.txt /requirements.txt
COPY app /app
WORKDIR /app
EXPOSE 8080

RUN pip install -r /requirements.txt
RUN adduser --disabled-password serviceuser
USER serviceuser
