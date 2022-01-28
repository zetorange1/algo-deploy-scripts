import os
import json
import argparse
import sys
import logging
import subprocess
import shutil
import glob
import time
import base64

log_format = "%(levelname)s %(asctime)s - %(message)s"

logging.basicConfig(
    stream=sys.stdout,
    filemode="w",
    format=log_format,
    level=logging.INFO,
)

logger = logging.getLogger()

BASE_DIR = os.path.join(os.sep, "app", "VQGAN-CLIP-Docker")
default_config_path = os.path.join(BASE_DIR, "configs", "local.json")

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


def get_base64_encoded_image(image_path):
    with open(image_path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode("utf-8")


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

if not os.path.exists(os.path.join(BASE_DIR, "outputs")):
    os.makedirs(os.path.join(BASE_DIR, "outputs"))

output_subprocess = open(BASE_DIR + "/outputs/subprocess.txt", "w")
subprocess.run(
    ["python", "-m", "scripts.generate", "-c", config_path],
    stdout=output_subprocess,
    cwd="./VQGAN-CLIP-Docker",
)
logging.info("Completed subprocess in %ss", time.time() - start_time)

logging.info("Generating output")

output_dir = os.path.join(os.sep, "data", "outputs")

if not os.path.exists(output_dir):
    os.makedirs(output_dir)

result_file = glob.glob(BASE_DIR + "/outputs/*.png")[0]

encoded_image = get_base64_encoded_image(result_file)

compute_job_result_path = os.path.join(output_dir, "result")

with open(compute_job_result_path, "w") as f:
    f.write(encoded_image)

# shutil.copyfile(result_file,)

logging.info("Finishing algorithm")
