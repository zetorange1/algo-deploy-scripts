import os
from sys import path
import time
import json
import logging
import sys
from typing import List
from io import StringIO
import zipfile

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
    if os.path.exists(custom_path):
        with open(custom_path, "r") as file:
            return json.load(file)
    else:
        logging.info(f"No such file: {custom_path}")


def get_input_and_calculate_result():
    dids = os.getenv("DIDS", None)

    if not dids:
        print("No DIDs found in environment. Aborting.")
        return

    dids = json.loads(dids)
    result = {}
    inputs = []
    number_of_lines = 0
    for did in dids:
        filename = os.path.join(
            os.sep, "data", "inputs", did, "0"
        )  # 0 for metadata service

        logging.info(f"Reading asset file {filename}.")

    try:
        with zipfile.ZipFile(filename) as zf:
            for file in zf.namelist():
                logging.info(f"Reading file in zip [{file}].")
                inputs.append(file)

                with zf.open(file) as f:
                    if file == "data.json":
                        data = f.read()
                        json_data = json.loads(data)

                    else:
                        count = 0
                        for line in f:
                            count += 1
                        number_of_lines += count
    except zipfile.BadZipFile as error:
        logging.error("Error reading zipfile [%s]", file, exc_info=error)
        sys.exit(-1)

    result["number_of_files"] = len(inputs)
    result["number_of_lines"] = number_of_lines
    return result


logging.info(f"Reading algorithm input")

algo_input = read_algorithm_custom_input()

logging.info(f"Reading input data")

result = get_input_and_calculate_result()

logging.info(f"Finished reading input data and calculating result")

output_dir = os.path.join(os.sep, "data", "outputs")

if not os.path.exists(output_dir):
    os.makedirs(output_dir)

compute_job_result_path = os.path.join(output_dir, "result")

with open(compute_job_result_path, "w") as f:
    algo_job_result = {"result": result, "algo_input": algo_input}
    f.write(json.dumps(algo_job_result))

logging.info(f"Algo input: {algo_input}")


logging.info("Finishing algorithm")
