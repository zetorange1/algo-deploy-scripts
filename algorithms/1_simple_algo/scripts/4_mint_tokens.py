from config import web3_wallet, ocean, config, web3_wallet2
from ocean_lib.aquarius import Aquarius
from ocean_lib.web3_internal.wallet import Wallet
import os

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
asset_dataset = aquarius.wait_for_asset(dataset_did)
asset_algo = aquarius.wait_for_asset(algo_did)

# Alice mints DATA datatokens and ALGO datatokens to Bob.
# Alternatively, Bob might have bought these in a market.
DATA_datatoken = ocean.get_datatoken(asset_dataset.datatokens[0]["address"])
ALGO_datatoken = ocean.get_datatoken(asset_algo.datatokens[0]["address"])

DATA_datatoken.mint(web3_wallet2.address, ocean.to_wei(5), web3_wallet)
ALGO_datatoken.mint(web3_wallet2.address, ocean.to_wei(5), web3_wallet)
