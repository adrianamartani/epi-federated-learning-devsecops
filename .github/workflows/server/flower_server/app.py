import flwr as fl
from flwr.server.strategy import FedAvg
import numpy as np
import torch
import os
import boto3

NUM_ROUNDS = int(os.getenv("NUM_ROUNDS", "3"))

def fit_config(server_round: int):
    return {"epochs": 1, "batch_size": 32}

strategy = FedAvg(
    fraction_fit=1.0,
    fraction_eval=0.0,
    min_fit_clients=1,
    min_available_clients=1,
    on_fit_config_fn=fit_config,
)

def save_dummy_global(round_num: int):
    # cria um arquivo dummy do "modelo"
    fn = f"global_round_{round_num}.pt"
    torch.save({"dummy": np.random.randn(10)}, fn)
    # tenta subir para MinIO se variáveis estiverem definidas
    minio_url = os.getenv("MINIO_URL", "http://minio:9000")
    minio_user = os.getenv("MINIO_USER", "minio")
    minio_pass = os.getenv("MINIO_PASS", "minio123")
    try:
        s3 = boto3.client("s3", endpoint_url=minio_url,
                          aws_access_key_id=minio_user,
                          aws_secret_access_key=minio_pass)
        bucket = "models"
        # cria bucket se não existir
        try:
            s3.head_bucket(Bucket=bucket)
        except:
            s3.create_bucket(Bucket=bucket)
        s3.upload_file(fn, bucket, fn)
        print(f"Uploaded {fn} to MinIO/{bucket}")
    except Exception as e:
        print("MinIO upload skipped or failed:", e)

if __name__ == "__main__":
    # start flower server in a blocking way but we will "simulate" rounds
    # We run fl.server.start_server - Flower will call strategy. We'll also save dummy global after server stops.
    print("Starting Flower server on 0.0.0.0:8080")
    fl.server.start_server(server_address="0.0.0.0:8080", strategy=strategy, config={"num_rounds": NUM_ROUNDS})
    # after server finishes (or in a real hook), save a dummy model for demo:
    save_dummy_global(NUM_ROUNDS)
