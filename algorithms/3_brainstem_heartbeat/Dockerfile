FROM oceanprotocol/algo_dockers:python-branin

WORKDIR /app

RUN pip install wheel

COPY ./requirements.txt /app/requirements.txt

RUN python -m pip install -r /app/requirements.txt

COPY algorithm.py /app/algorithm.py
