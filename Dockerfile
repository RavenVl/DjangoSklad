FROM python:3.12-alpine
RUN apk add postgresql-client build-base postgresql-dev
COPY requirements.txt /requirements.txt
RUN pip install -r /requirements.txt
COPY app /app
WORKDIR /app
EXPOSE 8080




RUN adduser --disabled-password serviceuser
USER serviceuser
