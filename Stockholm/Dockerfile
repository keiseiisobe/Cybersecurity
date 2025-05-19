FROM python:3

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

RUN useradd -m stockholm
WORKDIR /home/stockholm

COPY --chown=stockholm --chmod=700 stockholm ./stockholm
COPY --chown=stockholm infection ./infection

USER stockholm
