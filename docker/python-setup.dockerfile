FROM alpine:3.14
RUN apk update --no-cache 
RUN apk add --no-cache gcc musl-dev linux-headers
RUN apk add --no-cache python3 && ln -sf python3 /usr/bin/python
RUN python3 -m ensurepip
RUN pip3 install --no-cache --upgrade pip setuptools Django