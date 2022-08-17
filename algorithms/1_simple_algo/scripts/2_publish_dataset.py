# Publish the datatoken
from config import web3_wallet, ocean, config
from ocean_lib.aquarius import Aquarius

data_nft = ocean.create_data_nft(
    name="NFTToken1",
    symbol="NFT1",
    from_wallet=web3_wallet,
    # Optional parameters
    token_uri="https://example.com",
    template_index=1,
    transferable=True,
    owner=web3_wallet.address,
)

data_nft_address = data_nft.address

data_nft = ocean.get_nft_token(data_nft_address)
DATA_datatoken = data_nft.create_datatoken("DATA 1", "D1", from_wallet=web3_wallet)
print(f"DATA_datatoken address = '{DATA_datatoken.address}'")

# Specify metadata and services, using the Branin test dataset
DATA_date_created = "2022-08-17T10:55:11Z"
DATA_metadata = {
    "created": DATA_date_created,
    "updated": DATA_date_created,
    "description": "Sample dataset",
    "name": "Sample dataset",
    "type": "dataset",
    "author": "Dataunion.app",
    "license": "MIT",
}

# ocean.py offers multiple file types, but a simple url file should be enough for this example
from ocean_lib.structures.file_objects import UrlFile

DATA_url_file = UrlFile(url="https://crab.dev.dataunion.app")

DATA_files = [DATA_url_file]

# Set the compute values for compute service
DATA_compute_values = {
    "allowRawAlgorithm": False,
    "allowNetworkAccess": True,
    "publisherTrustedAlgorithms": [],
    "publisherTrustedAlgorithmPublishers": [],
}

# Create the Service
from ocean_lib.services.service import Service

DATA_compute_service = Service(
    service_id="2",
    service_type="compute",
    service_endpoint=ocean.config.provider_url,
    datatoken=DATA_datatoken.address,
    files=DATA_files,
    timeout=3600,
    compute_values=DATA_compute_values,
)

# Publish asset with compute service on-chain.
DATA_asset = ocean.assets.create(
    metadata=DATA_metadata,
    publisher_wallet=web3_wallet,
    files=DATA_files,
    services=[DATA_compute_service],
    data_nft_address=data_nft.address,
    deployed_datatokens=[DATA_datatoken],
)

print(f"DATA_asset did = '{DATA_asset.did}'")

# did:op:9f5591a01c122b6d3bcd61b80216bb539aac6882372e2c95de895cdebeaa1466
