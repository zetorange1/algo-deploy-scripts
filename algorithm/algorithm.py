import os
from sys import path
import time
import json

input_dir = os.path.join(os.sep, "data", "inputs")
output_dir = os.path.join(os.sep, "data", "outputs")

if not os.path.exists(output_dir):
    os.makedirs(output_dir)

with open(os.path.join(output_dir, "result"), "w") as f:
    f.write(f"Running algo for DIDs: {os.getenv('DIDS', None)}.\n")


def get_job_details():
    """Reads in metadata information about assets used by the algo"""
    job = dict()
    job["dids"] = json.loads(os.getenv("DIDS", None))
    job["metadata"] = dict()
    job["files"] = dict()
    job["algo"] = dict()
    job["secret"] = os.getenv("secret", None)
    algo_did = os.getenv("TRANSFORMATION_DID", None)
    if job["dids"] is not None:
        for did in job["dids"]:
            # get the ddo from disk
            filename = "/data/ddos/" + did
            with open(filename) as json_file:
                ddo = json.load(json_file)
                # search for metadata service
                for service in ddo["service"]:
                    if service["type"] == "metadata":
                        job["files"][did] = list()
                        index = 0
                        for file in service["attributes"]["main"]["files"]:
                            job["files"][did].append(
                                "/data/inputs/" + did + "/" + str(index)
                            )
                            index = index + 1
    if algo_did is not None:
        job["algo"]["did"] = algo_did
        job["algo"]["ddo_path"] = "/data/ddos/" + algo_did
    return job


def read_algorithm_custom_input():
    custom_path = os.path.join(os.sep, "data", "transformations", "algorithm")
    if os.path.exists(custom_path):
        with open(custom_path, "r") as file:
            return json.load(file)
    else:
        print(f"No such file: {custom_path}")


# Dummy sleep
print("Geting job details")
job_detials = get_job_details()

algorithm_did = os.getenv("TRANSFORMATION_DID", None)
print(f"Algorithm did {algorithm_did}")


algo_input = read_algorithm_custom_input()

print(f"Algo input: {algo_input}")
print("Finishing algorithm")
