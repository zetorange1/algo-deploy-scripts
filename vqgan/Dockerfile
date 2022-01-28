FROM pytorch/pytorch:1.9.0-cuda11.1-cudnn8-runtime

ENV DEVICE=cuda 

WORKDIR /app

COPY ./VQGAN-CLIP-Docker /app/VQGAN-CLIP-Docker

COPY ./content/models /app/VQGAN-CLIP-Docker/models
# COPY ./content/configs /configs
# COPY ./content/core /app/core
# COPY ./content/scripts /app/scripts

# COPY ./requirements.txt /requirements.txt
RUN python -m pip install -r /app/VQGAN-CLIP-Docker/requirements.txt

COPY algorithm.py /app/algorithm.py
