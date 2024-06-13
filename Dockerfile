FROM ubuntu:22.04

USER root

RUN apt-get update

RUN apt install wget -y
RUN wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
RUN apt install ./google-chrome-stable_current_amd64.deb -y

RUN apt-get install apt-utils python3.10 python3-pip -y
RUN ln /usr/bin/python3 /usr/bin/python
RUN python -m pip install --upgrade pip setuptools wheel

RUN mkdir project
WORKDIR project

COPY UkrNet ./UkrNet
COPY requirements.txt .

RUN pip install --upgrade -r requirements.txt

RUN useradd -m tester
RUN usermod -aG sudo tester
RUN su - tester

USER tester
