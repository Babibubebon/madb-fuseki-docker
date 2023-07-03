# MADB-Fuseki-Docker

Docker Hub: [babibubebon/madb-fuseki](https://hub.docker.com/r/babibubebon/madb-fuseki)

[メディア芸術データベース](https://mediaarts-db.bunka.go.jp/)のデータセットをロードした[Apache Jena Fuseki](https://jena.apache.org/documentation/fuseki2/index.html)によるSPARQLサーバです。

以下で公開されているRDFデータセットを各バージョン毎にロード済みのDockerイメージを提供します。

- GitHub: <https://github.com/mediaarts-db/dataset>
- MADB Lab: <https://mediag.bunka.go.jp/madb_lab/lod/download/>

## Usage

```sh
docker run --rm -p 3030:3030 babibubebon/madb-fuseki:{version}
```

タグ `{version}` には、利用したいデータセットのバージョンを `YYYYMMDD` 形式で指定します。便宜上、データセットの公開日をバージョンとして扱っています。

利用可能な `{version}` は、 [`versions/*.txt`](./versions/) をご確認ください。

起動後、以下のURLにアクセスして利用します。

- 管理画面: <http://localhost:3030>
  - 起動時に表示されるadminパスワードを入力します。
- SPARQLエンドポイント: <http://localhost:3030/madb/sparql>

### データセットのバージョンの識別

`<http://localhost:3030/madb/void/>` という名前付きグラフ内でデータセットのメタデータを記述しています。データセットを表すURIは `<http://localhost:3030/madb/#dataset>` としています。

例えば、以下のようなクエリで確認することができます。

```sparql
SELECT *
WHERE {
  GRAPH <http://localhost:3030/madb/void/> {
    <http://localhost:3030/madb/#dataset> ?p ?o .
  }
}
```

### 全文検索

[Luceneによる全文検索インデックス](https://jena.apache.org/documentation/query/text-query.html)が構築済みですので、SPARQLクエリで全文検索できます。

```sparql
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX schema: <https://schema.org/>
PREFIX text: <http://jena.apache.org/text#>

SELECT ?公開年 (COUNT(DISTINCT ?マンガ単行本) AS ?合計数) (SAMPLE(?マンガ単行本) AS ?マンガ単行本の例)
WHERE { 
  ?マンガ単行本 text:query '"異世界" OR "転生"' .
  ?マンガ単行本 schema:genre "マンガ単行本";
          schema:datePublished ?公開年月日 .
  BIND (SUBSTR(?公開年月日, 1, 4) AS ?公開年)
}
GROUP BY ?公開年
ORDER BY DESC(?公開年)
```

## Build

```sh
VERSION=YYYYMMDD
python create_void.py ${VERSION} > void.trig
docker build --build-arg DATASET_VERSION=${VERSION} -t babibubebon/madb-fuseki:${VERSION} .
```

## License

本リポジトリに含まれるリソースは、MIT Licenseで提供されます。

Dockerイメージ内に含まれるTDB2のデータベースファイルとして格納されたデータセットは、[メディア芸術データベース 利用規約](https://mediaarts-db.bunka.go.jp/user_terms)に従って、メディア芸術データベース（ベータ版）データセットを加工して生成したものです。
