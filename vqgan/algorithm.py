import os
import json
import argparse
import sys
import logging

log_format = "%(levelname)s %(asctime)s - %(message)s"

logging.basicConfig(
    stream=sys.stdout,
    filemode="w",
    format=log_format,
    level=logging.INFO,
)

logger = logging.getLogger()

default_config_path = os.path.join("configs", "docker.json")
default_custom_parameters_path = os.path.join(
    os.sep, "data", "transformations", "algorithm"
)

logging.info("Preparing argparse")

parser = argparse.ArgumentParser()
parser.add_argument("--local", type=bool, default=False, required=False)

parser.add_argument(
    "--config_path", type=str, default=default_config_path, required=False
)

parser.add_argument(
    "--custom_parameters_path",
    type=str,
    default=default_custom_parameters_path,
    required=False,
)

args = parser.parse_args()

config_path = args.config_path
custom_parameters_path = args.custom_parameters_path

logging.info("Completed parsing parameters")

logging.info("Reading file at path %s", custom_parameters_path)
with open(custom_parameters_path, "r") as f:
    custom_parameters = json.load(f)

logging.info("Writing config at path %s", config_path)
with open(config_path, "w") as outfile:
    json.dump(custom_parameters, outfile, indent=4)

logging.info("Finishing algorithm")
