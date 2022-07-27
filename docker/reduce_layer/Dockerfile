# docker build -t devopscube/optimize:4.0 --no-cache -f Dockerfile .
FROM ubuntu:latest
ENV DEBIAN_FRONTEND=noninteractive
# By default, Ubuntu installs recommended but not suggested packages. With --no-install-recommends, only the main dependencies (packages in the Depends field) are installed.
RUN apt-get update -y && apt-get upgrade -y && apt-get install --no-install-recommends vim net-tools dnsutils -y
