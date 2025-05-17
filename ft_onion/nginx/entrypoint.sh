#! /bin/bash

service ssh start
/usr/sbin/sshd -f /etc/ssh/sshd_config
echo "Starting nginx server."
nginx

sleep infinity
