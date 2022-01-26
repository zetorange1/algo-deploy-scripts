# VQGAN

## Copy files

```bash
mkdir content
sudo cp -r ~/git/VQGAN-CLIP-Docker/models/ content/
sudo cp -r ~/git/VQGAN-CLIP-Docker/scripts/ content/
sudo cp -r ~/git/VQGAN-CLIP-Docker/configs/ content/
sudo cp -r ~/git/VQGAN-CLIP-Docker/core/ content/
sudo chmod +r -R content/
```
Check size

```bash
sudo du -hc --max-depth=1 content
```

## Docker container

### Build

```bash
docker build . -t registry.dataunion.app/dataunion-vqgan:latest
```
### Push

```bash
docker image push registry.dataunion.app/dataunion-vqgan:latest
```

### Run locally

```bash
docker run --rm -it -v $PWD/data:/data --gpus all --entrypoint "bash" registry.dataunion.app/dataunion-vqgan

docker run --rm -it -v $PWD/data:/data --gpus all --entrypoint "python /app/algorithm.py" registry.dataunion.app/dataunion-vqgan ""
```