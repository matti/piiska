FROM python:3

RUN pip3 install locust

WORKDIR /app
COPY app .

ENTRYPOINT [ "/app/entrypoint.sh" ]
