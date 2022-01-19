# VQGAN

# Docker container

## Build

```bash
docker build . -t registry.dataunion.app/dataunion-vqgan:latest
```
## Push

```bash
docker image push registry.dataunion.app/dataunion-vqgan:latest
```

## Run locally

```bash
docker run --rm -it --entrypoint "python" registry.dataunion.app/dataunion-vqgan /app/algorithm.py
```