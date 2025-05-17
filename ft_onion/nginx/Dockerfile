FROM debian:bullseye-slim
EXPOSE 80
EXPOSE 4242
RUN apt update && \
    apt install -y nginx openssh-server
COPY nginx.conf /etc/nginx/nginx.conf
COPY sshd_config /etc/ssh/sshd_config
COPY --chmod=700 entrypoint.sh ./entrypoint.sh
COPY html/index.html /usr/share/nginx/html/index.html

RUN addgroup sshgroup && \
    useradd -g sshgroup sshuser && \
    mkdir -p /home/sshuser/.ssh
COPY secrets/id_rsa.pub /home/sshuser/.ssh/authorized_keys
RUN  chown -R sshuser:sshgroup /home/sshuser
    
ENTRYPOINT ["./entrypoint.sh"]