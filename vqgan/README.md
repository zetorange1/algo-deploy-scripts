# VQGAN

## Setup

```bash
git submodule update --init --recursive
```
## Docker container

### Build

```bash
docker build . -t registry.dataunion.app/vqgan-imagenet:0.0.1
```
### Push

```bash
docker image push registry.dataunion.app/vqgan-imagenet:0.0.1
```

## Run using docker

```bash

# With models
docker run --rm -it -v $PWD/data:/data -v $PWD/test_data/data:/app/VQGAN-CLIP-Docker/data -v $PWD/test_data/models:/app/VQGAN-CLIP-Docker/models -v $PWD/test_data/outputs:/app/VQGAN-CLIP-Docker/outputs --gpus all --entrypoint "bash" temp

# With already added model
docker run --rm -it -v $PWD/data:/data -v $PWD/test_data/data:/app/VQGAN-CLIP-Docker/data -v $PWD/test_data/outputs:/app/VQGAN-CLIP-Docker/outputs --gpus all --entrypoint "bash" registry.dataunion.app/vqgan-imagenet:0.0.1

# Direct algo
docker run --rm -it -v $PWD/data:/data --gpus all --entrypoint "python" registry.dataunion.app/vqgan-imagenet:0.0.1 "/app/algorithm.py"
```

# Run using kubectl
kubectl run my-algo -i --tty --rm --image=registry.dataunion.app/vqgan-imagenet:0.0.1 --image-pull-policy=Never  -- bash

kubectl run my-algo -i --tty --rm \
--image=registry.dataunion.app/vqgan-imagenet:0.0.1 \
--image-pull-policy=Always \
--overrides='{ "apiVersion": "v1", "spec": {"imagePullSecrets": [{"name": "regcred"}]} }' \
-n ocean-compute \
-- bash
```

## Commands in prompt for testing
```bash

mkdir -p /data/transformations; mkdir -p /outputs; mkdir -p /data/inputs; mkdir -p /data/outputs

echo "{\"id\":\"TdQovMPnnWPtvKE\",\"parameters\":{\"prompts\":[\"small | blue | claw\"]}}
" > /data/transformations/algorithm

python3 -m scripts.generate -c ./configs/local.json
```

## Copy files
```bash
mkdir content
sudo cp -r ~/git/VQGAN-CLIP-Docker/models/ content/
sudo cp -r ~/git/VQGAN-CLIP-Docker/configs/ content/
sudo cp -r ~/git/VQGAN-CLIP-Docker/core/ content/
sudo chmod +r -R content/
```

Check size

```bash
sudo du -hc --max-depth=1 content
```

### Run locally

```bash
kubectl delete pod my-algo
```
