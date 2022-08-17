FROM ubuntu:20.04

ENV DEBIAN_FRONTEND=noninteractive
RUN apt-get update \
    && apt-get install -y curl software-properties-common libcairo2-dev libjpeg-dev libgif-dev \
    && add-apt-repository -y ppa:deadsnakes/ppa \
    && apt-get install -y python3.10 python3.10-distutils python3.10-dev\
    && apt-get install -y build-essential libssl-dev libffi-dev libxml2-dev libxslt1-dev zlib1g-dev \
    && curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py \
    && python3.10 get-pip.py \
    && rm get-pip.py

RUN echo 'alias python="python3.10"' >> ~/.bashrc && echo 'alias python3="python3.10"' >> ~/.bashrc
RUN echo 'alias pip3="pip3.10"' >> ~/.bashrc && echo 'alias pip="pip3.10"' >> ~/.bashrc

RUN apt-get update && apt-get install vim -y && apt-get install less -y

WORKDIR /app

RUN pip install wheel

COPY ./requirements.txt /app/requirements.txt

RUN python3.10 -m pip install -r /app/requirements.txt

COPY algorithm.py /app/algorithm.py
