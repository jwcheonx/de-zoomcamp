import os.path
import subprocess

import polars as pl

URL = "https://d37ci6vzurychx.cloudfront.net/trip-data/yellow_tripdata_2021-01.parquet"
FILENAME = os.path.basename(URL)

print(f"Downloading {FILENAME} ...")
subprocess.run(["wget", "-qO", FILENAME, URL], check=True)

# print(pl.read_parquet_schema(FILENAME))

print("Writing to database ...")
df = pl.read_parquet(FILENAME)
df.write_database(
    table_name="yellow_taxi_trips",
    connection="postgresql://postgres:secret@127.0.0.1:5432/ny_taxi",
    if_table_exists="replace",
    engine="sqlalchemy",
)

print("Data ingestion complete.")
