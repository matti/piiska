FROM alpine:3.11

ENV __REFRESH=2

RUN apk add --no-cache \
  ca-certificates \
  bash curl nano \
  python3 git g++

RUN apk add --no-cache --virtual .build-deps \
  build-base python3-dev linux-headers libffi-dev \
  && pip3 install -e git://github.com/locustio/locust.git@master#egg=locustio \
  && pip3 install geventhttpclient \
  && apk del .build-deps

WORKDIR /app
COPY app .

ENTRYPOINT [ "/app/entrypoint.sh" ]
