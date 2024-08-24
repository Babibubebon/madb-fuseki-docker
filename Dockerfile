ARG FUSEKI_TAG=5.1.0

FROM secoresearch/fuseki:${FUSEKI_TAG}

LABEL org.opencontainers.image.source=https://github.com/Babibubebon/madb-fuseki-docker
LABEL org.opencontainers.image.description="A SPARQL server for Media Arts Database"

ARG DATASET_VERSION=latest

ADD assembler.ttl $ASSEMBLER

WORKDIR /tmp
ADD versions/${DATASET_VERSION}.txt files.txt
ADD void.trig /tmp/
RUN wget -nv -i files.txt \
    && find . -name '*.zip' | xargs -n1 unzip -j || true \
    && ${TDB2TDBLOADER} --loader=parallel *.ttl *.trig \
    && ${TEXTINDEXER} \
    && ${TDB2TDBSTATS} > /tmp/stats.opt \
	&& mv /tmp/stats.opt ${FUSEKI_BASE}/databases/tdb2/Data-0001/ \
    && rm *.zip *.ttl

WORKDIR ${FUSEKI_HOME}

ENV QUERY_TIMEOUT=-1
