import os
from sys import path
import time
import json
import logging
import sys

log_format = "%(levelname)s %(asctime)s - %(message)s"

logging.basicConfig(
    stream=sys.stdout,
    filemode="w",
    format=log_format,
    level=logging.INFO,
)

logger = logging.getLogger()

input_dir = os.path.join(os.sep, "data", "inputs")
output_dir = os.path.join(os.sep, "data", "outputs")

if not os.path.exists(output_dir):
    os.makedirs(output_dir)

with open(os.path.join(output_dir, "result"), "w") as f:
    f.write(f"Running algo for DIDs: {os.getenv('DIDS', None)}.\n")


def read_algorithm_custom_input():
    custom_path = os.path.join(os.sep, "data", "inputs", "algoCustomData.json")

    dids = os.getenv("DIDS", None)
    dids = json.loads(dids)
    for did in dids:
        custom_path = f"data/inputs/{did}/0"
        break

    if os.path.exists(custom_path):
        with open(custom_path, "r") as file:
            return json.load(file)
    else:
        logging.info(f"No such file: {custom_path}")


algo_input = read_algorithm_custom_input()


output_dir = os.path.join(os.sep, "data", "outputs")

if not os.path.exists(output_dir):
    os.makedirs(output_dir)

compute_job_result_path = os.path.join(output_dir, "result")

with open(compute_job_result_path, "w") as f:
    f.write(json.dumps(algo_input))

logging.info(f"Algo input: {algo_input}")
logging.info("Finishing algorithm")
