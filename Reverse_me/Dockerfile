FROM ubuntu:questing

RUN apt-get -y update && \
	DEBIAN_FRONTEND=noninteractive apt-get install -y   \
	build-essential                                     \
	file						    \
	gdb

RUN dpkg --add-architecture i386 && \
    apt update && \
    apt install -y libc6:i386

