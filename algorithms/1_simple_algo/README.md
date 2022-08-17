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