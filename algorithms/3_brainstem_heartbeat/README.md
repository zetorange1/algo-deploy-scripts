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
docker tag 3_brainstem_heartbeat_algorithm:0.0.1 registry.dataunion.app/3_brainstem_heartbeat_algorithm:0.0.1

docker image push registry.dataunion.app/3_brainstem_heartbeat_algorithm:0.0.1
```

### Run using kubectl

```bash
kubectl run 3_brainstem_heartbeat_algorithm -i --tty --rm \
--image=registry.dataunion.app/3_brainstem_heartbeat_algorithm:0.0.1 \
--image-pull-policy=Always \
--overrides='{ "apiVersion": "v1", "spec": {"imagePullSecrets": [{"name": "regcred"}]} }' \
-n ocean-compute \
-- bash
```

## Published DIDs

[Published Algorithm asset on Ocean market](https://market.oceanprotocol.com/asset/did:op:28cd29ea5d184487d1aafd646add16b7d049472dfb2967bea139aabefa4c695f)

[Published dataset asset on Ocean market](https://market.oceanprotocol.com/asset/did:op:0c3e0df7c620a79c1c9d77ce705f5e4500f1aa2e1d5a56e958c5f0952dbcdcd8)
