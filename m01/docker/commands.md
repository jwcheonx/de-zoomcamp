```sh
docker image build \
  --tag test:polars \
  .
docker container run --rm -it \
  test:polars \
  2025-01-02 hello
```
