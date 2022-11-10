import os
from sys import path
import time
import json
import logging
import sys
from typing import List
from io import StringIO

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
        print(f"No such file: {custom_path}")


def get_input():
    dids = os.getenv("DIDS", None)

    if not dids:
        print("No DIDs found in environment. Aborting.")
        return

    dids = json.loads(dids)

    inputs = []
    for did in dids:
        filename = f"data/inputs/{did}/0"  # 0 for metadata service
        logging.info(f"Reading asset file {filename}.")

        with open(filename) as datafile:
            res = json.load(datafile)
            inputs.append(res["result"])
    return inputs


def calculate_average_value(inputs: List[dict]) -> dict:

    number_of_beats = 0
    sum_of_beats = 0
    average_beats = 0

    for i in inputs:
        for j in i:
            if "hbr_rr" in j["file_type"]:
                raw = j["raw"]
                lines = raw.split("\n")
                for line in lines:
                    cols = line.split()
                    if len(cols) == 3 or len(cols) == 4:
                        try:
                            sum_of_beats += int(cols[2])
                            number_of_beats += 1
                        except:
                            pass
    average_beats = (sum_of_beats + 0.0) / number_of_beats

    logging.info("Number of heartbeats %s", number_of_beats)
    logging.info("Sum of heartbeats %s", sum_of_beats)
    logging.info("Average heartbeat %s", average_beats)

    return {
        "number_of_beats": number_of_beats,
        "sum_of_beats": sum_of_beats,
        "average_beats": average_beats,
    }


algo_input = read_algorithm_custom_input()
inputs = get_input()
result = calculate_average_value(inputs)

output_dir = os.path.join(os.sep, "data", "outputs")

if not os.path.exists(output_dir):
    os.makedirs(output_dir)

compute_job_result_path = os.path.join(output_dir, "result")

with open(compute_job_result_path, "w") as f:
    algo_job_result = {"result": result, "algo_input": algo_input}
    f.write(json.dumps(algo_job_result))

logging.info(f"Algo input: {algo_input}")

logging.info(f"Reading input files")

logging.info(f"Number of input files [{len(inputs)}]")

logging.info("Finishing algorithm")
