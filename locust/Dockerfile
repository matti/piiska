FROM alpine:3.11

ENV __REFRESH=2

RUN apk add --no-cache \
  ca-certificates \
  bash curl nano redis \
  python3 git g++ \
  && pip3 install --upgrade pip \
  && apk add --no-cache --virtual .build-deps \
  build-base python3-dev linux-headers libffi-dev libxml2-dev libxslt-dev \
  && pip3 install -e git://github.com/locustio/locust.git@master#egg=locustio \
  && pip3 install geventhttpclient \
  && pip3 install bs4 \
  && pip3 install lxml \
  && pip3 install redis \
  && apk del .build-deps

WORKDIR /app
COPY app .

ENTRYPOINT [ "/app/entrypoint.sh" ]
