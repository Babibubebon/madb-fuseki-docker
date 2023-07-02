# MADB-Fuseki-Docker

[メディア芸術データベース](https://mediaarts-db.bunka.go.jp/)のデータセットをロードした[Apache Jena Fuseki](https://jena.apache.org/documentation/fuseki2/index.html)によるSPARQLサーバです。

以下で公開されているRDFデータセットを各バージョン毎にロード済みのDockerイメージを提供します。

- GitHub: https://github.com/mediaarts-db/dataset
- MADB Lab: https://mediag.bunka.go.jp/madb_lab/lod/download/

## Usage

```sh
docker run --rm -it -p 3030:3030 babibubebon/madb-fuseki:{version}
```

`{version}` には利用したいデータセットのバージョンを `YYYYMMDD` 形式で指定します。
利用可能な `{version}` は、 `versions/*.txt` をご確認ください。

起動後、以下のURLにアクセスして利用します。

- 管理画面: <http://localhost:3030>
  - 起動時に表示されるadminパスワードを入力します。
- SPARQLエンドポイント: <http://localhost:3030/madb/sparql>

## Build

```sh
python create_void.py YYYYMMDD > void.trig
docker build -t babibubebon/madb-fuseki .
```

## License

本リポジトリに含まれるリソースは、MIT Licenseで提供されます。

Dockerイメージ内に含まれるデータセットは、[メディア芸術データベース 利用規約](https://mediaarts-db.bunka.go.jp/user_terms)に従って、メディア芸術データベース（ベータ版）データセットを加工して生成したものです。
