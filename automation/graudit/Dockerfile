FROM alpine:latest

# Install packages
RUN apk add --no-cache git bash grep

WORKDIR /opt
RUN git clone --depth=1 https://github.com/wireghoul/graudit

WORKDIR /opt/graudit
SHELL ["/bin/bash"]
ENTRYPOINT ["/opt/graudit/graudit"]