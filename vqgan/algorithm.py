import os
import json
import argparse
import sys
import logging
import subprocess
import shutil
import glob
import time

log_format = "%(levelname)s %(asctime)s - %(message)s"

logging.basicConfig(
    stream=sys.stdout,
    filemode="w",
    format=log_format,
    level=logging.INFO,
)

logger = logging.getLogger()

default_config_path = os.path.join(os.sep, "configs", "docker.json")
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

current_config = json.load(open(config_path, "r"))

with open(config_path, "w") as outfile:
    current_config["prompts"] = custom_parameters["parameters"]["prompts"]
    json.dump(current_config, outfile, indent=4)

logging.info("Starting subprocess")
start_time = time.time()

if not os.path.exists(os.path.join(os.sep, "outputs")):
    os.makedirs(os.path.join(os.sep, "outputs"))

output_subprocess = open("/outputs/subprocess.txt", "w")
subprocess.run(
    ["python", "-m", "scripts.generate", "-c", "/configs/docker.json"],
    stdout=output_subprocess,
)
logging.info("Completed subprocess in %ss", time.time() - start_time)

logging.info("Generating output")

output_dir = os.path.join(os.sep, "data", "outputs")

if not os.path.exists(output_dir):
    os.makedirs(output_dir)

result_file = glob.glob("/outputs/*.png")[0]
shutil.copyfile(result_file, os.path.join(output_dir, "result"))

logging.info("Finishing algorithm")
