help:
	@echo "Command List:"
	@echo ""
	@echo "server:        run ftp server."
	@echo "server-down:   stop ftp server."
	@echo "client:        run ftp client container."
	@echo "client-build:  build ftp client image."
	@echo "spoofer:       run spoofer container."
	@echo "spoofer-build: build spoofer image."
	@echo "info:          print MAC address and IP adress of each containers."

server:
	docker run --rm -d --name ftpd_server \
	-p 21:21 -p 30000-30009:30000-30009 \
	-e FTP_USER_NAME=ftp_client -e FTP_USER_PASS=mypass -e FTP_USER_HOME=/home/ftp_client \
	-v ./data:/home/ftp_client/ \
	stilliard/pure-ftpd

server-down:
	docker stop ftpd_server

client:
	docker run --rm -it --name ftp_client \
	-v ./ftp_client/data:/home/ubuntu/ \
	ftp_client /bin/bash

client-build:
	docker build -t ftp_client ./ftp_client

spoofer:
	docker run --rm -it --name spoofer \
	-v ./spoofer/scripts:/home/inquisitor/ \
	spoofer /bin/bash

spoofer-build:
	docker build -t spoofer ./spoofer

info:
	docker network inspect bridge | jq -r '.[0].Containers[] | "\(.Name): MAC=\(.MacAddress), IP=\(.IPv4Address)"'

.PHONY: help server server-down client client-build spoofer spoofer-build info
