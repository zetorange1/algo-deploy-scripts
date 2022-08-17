# Publish the algorithm NFT token
from config import web3_wallet, ocean, config
from ocean_lib.aquarius import Aquarius
from datetime import datetime
from ocean_lib.structures.file_objects import UrlFile
import json
from ocean_lib.utils.utilities import create_checksum
from ocean_lib.data_provider.data_encryptor import DataEncryptor

plublish_new = True

ALGO_date_created = datetime.now().strftime("%Y-%m-%dT%H:%M:%SZ")

ALGO_metadata = {
    "created": ALGO_date_created,
    "updated": ALGO_date_created,
    "description": "gpr",
    "name": "gpr",
    "type": "algorithm",
    "author": "Dataunion",
    "license": "MIT",
    "algorithm": {
        "language": "python",
        "format": "docker-image",
        "version": "0.1",
        "container": {
            "entrypoint": "python3 $ALGO",
            "image": "oceanprotocol/algo_dockers",
            "tag": "python-branin",
            "checksum": "sha256:8221d20c1c16491d7d56b9657ea09082c0ee4a8ab1a6621fa720da58b09580e4",
        },
    },
}

# ocean.py offers multiple file types, but a simple url file should be enough for this example

ALGO_url_file = UrlFile(
    url="https://<username>:<password>@couchdb.dev.dataunion.app/algorithm-scripts/884dc2d583fccfb58ac3306fdd000462/algorithm.py"
)

ALGO_files = [ALGO_url_file]

if plublish_new:
    ALGO_nft_token = ocean.create_data_nft("NFTToken1", "NFT1", web3_wallet)
    print(f"ALGO_nft_token address = '{ALGO_nft_token.address}'")

    # Publish the datatoken
    ALGO_datatoken = ALGO_nft_token.create_datatoken(
        "ALGO 1", "A1", from_wallet=web3_wallet, template_index=1, datatoken_cap=1000
    )
    print(f"ALGO_datatoken address = '{ALGO_datatoken.address}'")

    ALGO_asset = ocean.assets.create(
        metadata=ALGO_metadata,
        publisher_wallet=web3_wallet,
        files=ALGO_files,
        data_nft_address=ALGO_nft_token.address,
        deployed_datatokens=[ALGO_datatoken],
    )
    print(ALGO_asset.as_dictionary())
    print(f"ALGO_asset did = '{ALGO_asset.did}'")

else:
    ALGO_nft_token = ocean.get_nft_token("0x4528D9C107250850a8DdC8123f8B5fbc24511034")
    ALGO_datatoken = ocean.get_datatoken("0xAbE5914F2c21C850B71abC7f8738f95405e6Da0d")
    algo_did = "did:op:688d1834ef6a9db56303657aaf6eb9dcc2c4af2192d04dfec3ec857afee19ab9"
    aquarius = Aquarius.get_instance(config.metadata_cache_uri)

    # Replace this
    asset = aquarius.wait_for_asset(algo_did)

    asset_dict = asset.as_dictionary()

    # Update the ddo
    asset_dict["metadata"] = ALGO_metadata

    _, proof = aquarius.validate_asset(asset)
    print(_, proof)

    ddo_string = json.dumps(asset_dict, separators=(",", ":"))
    ddo_bytes = ddo_string.encode("utf-8")
    ddo_hash = create_checksum(ddo_string)

    # Encrypt the updated ddo
    encrypt_response = DataEncryptor.encrypt(
        objects_to_encrypt=ddo_string, provider_uri=config.provider_url
    )
    document = encrypt_response.text

    # TODO: explain this
    flags = bytes([2])

    dataNFT = ocean.get_nft_token(asset_dict["nftAddress"])

    dataNFT.set_metadata(
        metadata_state=0,
        metadata_decryptor_url=config.provider_url,
        metadata_decryptor_address=web3_wallet.address,
        flags=flags,
        data=document,
        data_hash=ddo_hash,
        metadata_proofs=[],
        from_wallet=web3_wallet,
    )
    # ocean.assets.update(asset, web3_wallet, config.provider_url)
    # Fetch the asset on chain
    asset = aquarius.wait_for_asset(algo_did)
    updated_ddo = asset.as_dictionary()

    print("===========================")
    print("Updated asset_dict")
    print(asset_dict)
    print("===========================")
