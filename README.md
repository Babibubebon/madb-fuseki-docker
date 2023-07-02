# MADB-Fuseki-Docker

## Build

```sh
python create_void.py YYYYMMDD > void.trig
docker build -t babibubebon/madb-fuseki .
```

## Run

```sh
docker run --rm -it -p 3030:3030 babibubebon/madb-fuseki
```

<http://localhost:3030>