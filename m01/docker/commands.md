```sh
docker image build \
  --tag test:polars \
  .
docker container run --rm -it \
  test:polars \
  2025-01-02 hello
```

```sh
docker container run -d \
  --name db-ny-taxi \
  --env POSTGRES_PASSWORD=secret \
  --env POSTGRES_DB=ny_taxi \
  --mount type=volume,source=ny-taxi-pg-data,target=/var/lib/postgresql/data \
  --publish 127.0.0.1:5432:5432 \
  postgres:17.2-alpine3.21

docker image build \
  --tag jwcheonx/ny-taxi-data-ingestor:0.1.0 \
  .
docker container run --rm -it \
  --network container:db-ny-taxi \
  jwcheonx/ny-taxi-data-ingestor:0.1.0 \
  --url https://d37ci6vzurychx.cloudfront.net/trip-data/yellow_tripdata_2021-01.parquet \
  --pass secret \
  --database ny_taxi \
  --table_name yellow_taxi_trips

# sudo apt-get install libpq-dev
uvx pgcli \
  --host 127.0.0.1 \
  --port 5432 \
  --username postgres \
  ny_taxi
```

```sh
docker compose \
  # --profile tools \
  up -d

docker compose run --build --rm \
  ingest-data
```
