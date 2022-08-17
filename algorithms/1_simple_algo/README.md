# A simple algorithm that return the input parameters in result

## Build container

```bash
docker build . -t 1_simple_algorithm
```

## Run container (test)

```bash
docker run -v $PWD/data:/data/ --entrypoint "python3.10" 1_simple_algorithm "/app/algorithm.py"
```

### Tag and Push

```bash
docker tag 1_simple_algorithm:0.0.1 registry.dataunion.app/1_simple_algorithm:0.0.1

docker image push registry.dataunion.app/1_simple_algorithm:0.0.1
```

### Run using kubectl

```bash
kubectl run 1-simple-algorithm -i --tty --rm \
--image=registry.dataunion.app/1_simple_algorithm:0.0.1 \
--image-pull-policy=Always \
--overrides='{ "apiVersion": "v1", "spec": {"imagePullSecrets": [{"name": "regcred"}]} }' \
-n ocean-compute \
-- bash
```

## Published DIDs:

```
dataset_did = "did:op:9f5591a01c122b6d3bcd61b80216bb539aac6882372e2c95de895cdebeaa1466"
algo_did = "did:op:fb8d24aff3cdf29dc9fbd15d31a27cb0e06de7f345cd8543fc67269f612c0c3e"
```