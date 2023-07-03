import sys
from datetime import datetime


def create_void_description(version: str) -> str:
    issued = datetime.strptime(version, "%Y%m%d").strftime("%Y-%m-%d")

    data_dump_statements = ""
    with open(f"./versions/{version}.txt") as f:
        urls = f.read().splitlines()
        for url in urls:
            data_dump_statements += f"        void:dataDump <{url}> ;\n"

    return f"""
@prefix dcterms: <http://purl.org/dc/terms/> .
@prefix void: <http://rdfs.org/ns/void#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

<http://localhost:3030/madb/void/>
{{
    <http://localhost:3030/madb/#dataset> a void:Dataset ;
        dcterms:title "メディア芸術データベース ({issued}版)"@ja, "Media Arts Database (ver.{issued})"@en ;
        dcterms:license <https://mediaarts-db.bunka.go.jp/user_terms> ;
        dcterms:issued "{issued}"^^xsd:date ;
        void:uriSpace "https://mediaarts-db.bunka.go.jp/id/" ;
        void:sparqlEndpoint <http://localhost:3030/madb/sparql> ;
        {data_dump_statements.strip()}
        .
}}
""".strip()


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Please specify date.", file=sys.stderr)
        exit(1)

    print(create_void_description(sys.argv[1]))
