FROM alpine:3.14
RUN apk update --no-cache 
RUN apk add --no-cache gcc musl-dev linux-headers postgresql-dev postgresql-client
RUN apk add --no-cache python3 && ln -sf python3 /usr/bin/python

RUN export PATH=/usr/lib/postgresql/X.Y/bin/:$PATH

RUN python3 -m ensurepip
RUN pip3 install --no-cache --upgrade pip setuptools Django psycopg