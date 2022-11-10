# algo-deploy-scripts

Scripts to deploy algorithms and logic to be part of our setup

```bash
docker run --name jupyter -p 8888:8888 --user root -e GRANT_SUDO=yes -e JUPYTER_ENABLE_LAB=yes -v ${PWD}:/home/jovyan/work --network=host jupyter/minimal-notebook:python-3.8.8
```

```bash
sudo apt-get update
sudo apt-get install gcc curl -y
pip install wheel ocean-lib numpy matplotlib python-dotenv
```

## Docker container

## Build

```bash
docker build . -t registry.dataunion.app/dataunion-algo:latest
```

## Push

```bash
docker image push registry.dataunion.app/dataunion-algo:latest
```

## Run locally

```bash
docker run --rm -it --entrypoint "python" registry.dataunion.app/dataunion-algo /app/algorithm.py
```

## Deploy scripts

```bash
pip install ocean-lib python-dotenv
```
