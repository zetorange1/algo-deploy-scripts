from config import web3_wallet, ocean, config, web3_wallet2
from ocean_lib.aquarius import Aquarius

# Local
# dataset_did = "did:op:33e68473055b7f84be2d4f6baea2bf58bb97e87ab683f67571e237c7baae3fe4"
# algo_did = "did:op:656b3ab786fc76255988d8c106c7df6db8af9fada6a5b5f9989377da05f8827a"

# Mumbai
dataset_did = "did:op:788b00d5e066255fa7aca69919a28727abe63e6a8d286e69a008fe3af7372413"
algo_did = "did:op:21b72442f37169bb3f0446a86ff31693cb23294b546e4d4c43b2a908aa7f164d"

# Dataunion test algo
dataset_did = "did:op:9f5591a01c122b6d3bcd61b80216bb539aac6882372e2c95de895cdebeaa1466"
algo_did = "did:op:fb8d24aff3cdf29dc9fbd15d31a27cb0e06de7f345cd8543fc67269f612c0c3e"

aquarius = Aquarius.get_instance(config.metadata_cache_uri)

DATA_asset = aquarius.wait_for_asset(dataset_did)
ALGO_asset = aquarius.wait_for_asset(algo_did)

# Convenience variables
DATA_did = DATA_asset.did
ALGO_did = ALGO_asset.did

# Operate on updated and indexed assets
DATA_asset = ocean.assets.resolve(DATA_did)
ALGO_asset = ocean.assets.resolve(ALGO_did)

compute_service = DATA_asset.services[0]
algo_service = ALGO_asset.services[0]
free_c2d_env = ocean.compute.get_free_c2d_environment(compute_service.service_endpoint)

from datetime import datetime, timedelta
from ocean_lib.models.compute_input import ComputeInput

DATA_compute_input = ComputeInput(DATA_asset, compute_service)
ALGO_compute_input = ComputeInput(ALGO_asset, algo_service)

# Pay for dataset and algo for 1 day
datasets, algorithm = ocean.assets.pay_for_compute_service(
    datasets=[DATA_compute_input],
    algorithm_data=ALGO_compute_input,
    consume_market_order_fee_address=web3_wallet2.address,
    wallet=web3_wallet2,
    compute_environment=free_c2d_env["id"],
    valid_until=int((datetime.utcnow() + timedelta(days=1)).timestamp()),
    consumer_address=free_c2d_env["consumerAddress"],
)
assert datasets, "pay for dataset unsuccessful"
assert algorithm, "pay for algorithm unsuccessful"

# Start compute job
job_id = ocean.compute.start(
    consumer_wallet=web3_wallet2,
    dataset=datasets[0],
    compute_environment=free_c2d_env["id"],
    algorithm=algorithm,
    algorithm_algocustomdata={
        "my_input": 123
    }
)
print(f"Started compute job with id: {job_id}")
