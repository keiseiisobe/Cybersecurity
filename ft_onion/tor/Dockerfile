FROM debian:bullseye-slim
RUN apt update && \
    apt install -y tor systemctl
COPY torrc /etc/tor/torrc
COPY --chown=debian-tor --chmod=700 entrypoint.sh ./entrypoint.sh
USER debian-tor
ENTRYPOINT ["./entrypoint.sh"]
CMD ["tor"]
