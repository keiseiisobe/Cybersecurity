FROM python:3

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

RUN useradd -m stockholm
WORKDIR /home/stockholm

COPY ./infection ./infection

USER stockholm
