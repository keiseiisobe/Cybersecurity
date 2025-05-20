#! /bin/bash

ftp ftpd_server 21 << EOF
ftp_client
mypass
get bocchan.txt
put hamlet.txt
EOF

sleep infinity
