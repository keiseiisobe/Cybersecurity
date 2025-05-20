FROM ubuntu:latest
RUN apt update && \
    apt install -y ftp
COPY --chmod=700 ./docker-entrypoint.sh /docker-entrypoint.sh
WORKDIR /home/ubuntu
ENTRYPOINT ["/docker-entrypoint.sh"]
