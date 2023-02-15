# A simple algorithm that return the input parameters in result

## Build container

```bash
docker build . -t 3_brainstem_heartbeat_algorithm
```

## Run container (test)

```bash
docker run -v $PWD/data:/data/ -e DIDS='["dummy_data"]' --entrypoint "python3" 3_brainstem_heartbeat_algorithm "/app/algorithm.py"
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

## Published DIDs

[Published Dataset DID on Ocean market](https://market.oceanprotocol.com/asset/did:op:067589c6fbb7e74ceff72ad2309774ae8fea85d15f5c23dbc8aa95d90c685a55)
