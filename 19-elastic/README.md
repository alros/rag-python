# Using Elasticsearch to store embeddings

Based on
- [this tutorial](https://www.elastic.co/search-labs/tutorials/install-elasticsearch/docker) from Elasticsearch
- [this paper](https://arxiv.org/pdf/2401.18059.pdf) about recursive retrieval
- [my smarter ingest process](../14-smarter-ingest/README.md) to handle books in PDF

The implementation creates two levels of documents in Elasticsearch:

- summary: summary of a blocks of chunks.
- chunks: the collection of all the chunks.
  - all the chunks refer to their summary.

The search works on two levels:

- match of top_k summaries.
- match of top_k chunks with parent in the first set.

