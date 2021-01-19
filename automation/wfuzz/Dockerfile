FROM alpine:latest

# Install packages
RUN apk add --no-cache python3 python3-dev py3-pip libcurl

# Needed for pycurl
ENV PYCURL_SSL_LIBRARY=openssl

# Install packages only needed for building, install and clean on a single layer
RUN apk add --no-cache --virtual .build-dependencies build-base curl-dev \
    && pip install pycurl \
    && apk del .build-dependencies

RUN pip3 install wfuzz

ENTRYPOINT ["wfuzz"]