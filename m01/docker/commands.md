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

uv run ingest_data.py

# sudo apt-get install libpq-dev
uvx pgcli \
  --host 127.0.0.1 \
  --port 5432 \
  --username postgres \
  ny_taxi
```
