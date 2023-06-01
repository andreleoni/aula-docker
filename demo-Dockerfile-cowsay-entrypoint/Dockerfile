FROM ubuntu:18.04

MAINTAINER Andre Leoni <andreluizleoni@gmail.com>

RUN apt-get update && apt-get install -y cowsay

COPY entrypoint.sh /

ENTRYPOINT ["/entrypoint.sh"]
