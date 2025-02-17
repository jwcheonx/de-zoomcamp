import argparse
import os.path
import subprocess

import polars as pl


def main(params: argparse.Namespace) -> None:
    filename = os.path.basename(params.url)

    print(f"Downloading {filename} ...")
    subprocess.run(["wget", "-qO", filename, params.url], check=True)

    # print(pl.read_parquet_schema(filename))

    print("Writing to database ...")
    df = pl.read_parquet(filename)
    df.write_database(
        table_name=params.table_name,
        connection=f"postgresql://{params.user}:{params.password}@{params.server}:{params.port}/{params.database}",
        if_table_exists="replace",
        engine="sqlalchemy",
    )

    print("Data ingestion complete.")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    parser.add_argument("--url", required=True)
    parser.add_argument("--pass", required=True, dest="password")
    parser.add_argument("--database", required=True)
    parser.add_argument("--table_name", required=True)

    parser.add_argument("--user", default="postgres")
    parser.add_argument("--server", default="127.0.0.1")
    parser.add_argument("--port", type=int, default=5432)

    main(parser.parse_args())
