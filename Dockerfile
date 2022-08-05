# docker/backend/Dockerfile

FROM python:3.8-alpine
ENV PYTHONUNBUFFERED 1

WORKDIR /app
ADD ./ /app

RUN pip install --upgrade pip


RUN apk update \
    && apk add --no-cache gcc musl-dev python3-dev\
    && apk add --virtual build-deps gcc python3-dev musl-dev \
    && apk add jpeg-dev zlib-dev libjpeg \
    && pip install Pillow \
    && apk del build-deps

RUN pip install --no-deps ruamel.yaml.clib

RUN pip install -r requirements.txt