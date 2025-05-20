FROM python:3

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

RUN useradd -m inquisitor
WORKDIR /home/inquisitor

COPY --chown=inquisitor --chmod=700 inquisitor ./inquisitor

USER inquisitor
