# VQGAN

## Build

```
git submodule update --init --recursive

docker run --rm -it -v $PWD/data:/data -v $PWD/test_data/data:/app/VQGAN-CLIP-Docker/data -v $PWD/test_data/models:/app/VQGAN-CLIP-Docker/models -v $PWD/test_data/outputs:/app/VQGAN-CLIP-Docker/outputs --gpus all --entrypoint "bash" temp

python3 -m scripts.generate -c ./configs/local.json

```

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

docker run --rm -it -v $PWD/data:/data --gpus all --entrypoint "python" registry.dataunion.app/dataunion-vqgan:latest "/app/algorithm.py"

kubectl delete pod my-algo

kubectl run my-algo -i --tty --rm --image=registry.dataunion.app/dataunion-vqgan:latest --image-pull-policy=Never  -- bash

```

```bash

mkdir -p /data/transformations; mkdir -p /outputs; mkdir -p /data/inputs; mkdir -p /data/outputs

echo "{\"id\":\"TdQovMPnnWPtvKE\",\"parameters\":{\"prompts\":[\"small | blue | claw\"]}}
" > /data/transformations/algorithm
```