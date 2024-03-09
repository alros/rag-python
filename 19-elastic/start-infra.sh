#!/bin/zsh

# start elasticsearch
docker run -p 9200:9200 -d --name elasticsearch \
  -e "discovery.type=single-node" \
  -e "xpack.security.enabled=false" \
  -e "xpack.security.http.ssl.enabled=false" \
  -e "xpack.license.self_generated.type=trial" \
  docker.elastic.co/elasticsearch/elasticsearch:8.11.0

# start nlm-ingestor
docker pull ghcr.io/nlmatics/nlm-ingestor:latest
docker run -p 5010:5001 ghcr.io/nlmatics/nlm-ingestor:latest