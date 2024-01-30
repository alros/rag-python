# Generate the bio of a fictional character

Run `ollama serve` first, then update the script with prompts.

Put the output in `datasets/bio` to build knowledge and repeat the cycle.

The raw output of the last iteration:

```text
DEBUG:llama_index.readers.file.base:> [SimpleDirectoryReader] Total files added: 8
> [SimpleDirectoryReader] Total files added: 8
DEBUG:urllib3.connectionpool:Starting new HTTPS connection (1): huggingface.co:443
Starting new HTTPS connection (1): huggingface.co:443
DEBUG:urllib3.connectionpool:https://huggingface.co:443 "HEAD /BAAI/bge-small-en/resolve/main/config.json HTTP/1.1" 200 0
https://huggingface.co:443 "HEAD /BAAI/bge-small-en/resolve/main/config.json HTTP/1.1" 200 0
DEBUG:urllib3.connectionpool:https://huggingface.co:443 "HEAD /BAAI/bge-small-en/resolve/main/tokenizer_config.json HTTP/1.1" 200 0
https://huggingface.co:443 "HEAD /BAAI/bge-small-en/resolve/main/tokenizer_config.json HTTP/1.1" 200 0
INFO:chromadb.telemetry.product.posthog:Anonymized telemetry enabled. See                     https://docs.trychroma.com/telemetry for more information.
Anonymized telemetry enabled. See                     https://docs.trychroma.com/telemetry for more information.
DEBUG:chromadb.config:Starting component System
Starting component System
DEBUG:chromadb.config:Starting component Posthog
Starting component Posthog
DEBUG:chromadb.config:Starting component OpenTelemetryClient
Starting component OpenTelemetryClient
DEBUG:chromadb.config:Starting component SimpleAssignmentPolicy
Starting component SimpleAssignmentPolicy
DEBUG:chromadb.config:Starting component SqliteDB
Starting component SqliteDB
DEBUG:chromadb.config:Starting component LocalSegmentManager
Starting component LocalSegmentManager
DEBUG:chromadb.config:Starting component SegmentAPI
Starting component SegmentAPI
DEBUG:llama_index.node_parser.node_utils:> Adding chunk: Born on a crisp autumn day in 1926, in the anci...
> Adding chunk: Born on a crisp autumn day in 1926, in the anci...
DEBUG:llama_index.node_parser.node_utils:> Adding chunk: In the heart of Rome, nestled in the ancient an...
> Adding chunk: In the heart of Rome, nestled in the ancient an...
DEBUG:llama_index.node_parser.node_utils:> Adding chunk: Once a cool, rainy autumn day, Lucrezia found h...
> Adding chunk: Once a cool, rainy autumn day, Lucrezia found h...
DEBUG:llama_index.node_parser.node_utils:> Adding chunk: List of the Etruscan artifacts discovered by Lu...
> Adding chunk: List of the Etruscan artifacts discovered by Lu...
DEBUG:llama_index.node_parser.node_utils:> Adding chunk: Lucrezia's home in Trastevere is a cherished sa...
> Adding chunk: Lucrezia's home in Trastevere is a cherished sa...
DEBUG:llama_index.node_parser.node_utils:> Adding chunk: In her twilight years, Lucrezia found herself s...
> Adding chunk: In her twilight years, Lucrezia found herself s...
DEBUG:llama_index.node_parser.node_utils:> Adding chunk: Lucrezia's dedication to preserving heritage is...
> Adding chunk: Lucrezia's dedication to preserving heritage is...
DEBUG:llama_index.node_parser.node_utils:> Adding chunk: List of the Roman mosaics discovered by Lucrezi...
> Adding chunk: List of the Roman mosaics discovered by Lucrezi...
DEBUG:urllib3.connectionpool:Starting new HTTPS connection (1): app.posthog.com:443
Starting new HTTPS connection (1): app.posthog.com:443
DEBUG:chromadb.config:Starting component PersistentLocalHnswSegment
Starting component PersistentLocalHnswSegment
**********
Trace: index_construction
    |_node_parsing ->  0.004813 seconds
      |_chunking ->  0.000568 seconds
      |_chunking ->  0.000573 seconds
      |_chunking ->  0.000444 seconds
      |_chunking ->  0.000455 seconds
      |_chunking ->  0.000281 seconds
      |_chunking ->  0.000344 seconds
      |_chunking ->  0.000174 seconds
      |_chunking ->  0.000364 seconds
    |_embedding ->  0.507487 seconds
**********
DEBUG:urllib3.connectionpool:https://app.posthog.com:443 "POST /batch/ HTTP/1.1" 200 None
https://app.posthog.com:443 "POST /batch/ HTTP/1.1" 200 None
DEBUG:llama_index.vector_stores.chroma:> Top 1 nodes:
> Top 1 nodes:
DEBUG:llama_index.vector_stores.chroma:> [Node 5d3dd235-80c0-46e7-870f-a381dbb1b3f4] [Similarity score: 0.7949829822051445] In her twilight years, Lucrezia found herself sitting in the sun-drenched courtyard of her villa ...
> [Node 5d3dd235-80c0-46e7-870f-a381dbb1b3f4] [Similarity score: 0.7949829822051445] In her twilight years, Lucrezia found herself sitting in the sun-drenched courtyard of her villa ...
DEBUG:llama_index.vector_stores.chroma:> [Node 69aa34e5-f6d9-4330-a67d-2539422ec229] [Similarity score: 0.7949829822051445] In her twilight years, Lucrezia found herself sitting in the sun-drenched courtyard of her villa ...
> [Node 69aa34e5-f6d9-4330-a67d-2539422ec229] [Similarity score: 0.7949829822051445] In her twilight years, Lucrezia found herself sitting in the sun-drenched courtyard of her villa ...
DEBUG:llama_index.indices.utils:> Top 2 nodes:
> [Node 5d3dd235-80c0-46e7-870f-a381dbb1b3f4] [Similarity score:             0.794983] In her twilight years, Lucrezia found herself sitting in the sun-drenched courtyard of her villa ...
> [Node 69aa34e5-f6d9-4330-a67d-2539422ec229] [Similarity score:             0.794983] In her twilight years, Lucrezia found herself sitting in the sun-drenched courtyard of her villa ...
> Top 2 nodes:
> [Node 5d3dd235-80c0-46e7-870f-a381dbb1b3f4] [Similarity score:             0.794983] In her twilight years, Lucrezia found herself sitting in the sun-drenched courtyard of her villa ...
> [Node 69aa34e5-f6d9-4330-a67d-2539422ec229] [Similarity score:             0.794983] In her twilight years, Lucrezia found herself sitting in the sun-drenched courtyard of her villa ...
DEBUG:httpx:load_ssl_context verify=True cert=None trust_env=True http2=False
load_ssl_context verify=True cert=None trust_env=True http2=False
DEBUG:httpx:load_verify_locations cafile='/Users/ar/dev/dis/venvs/llm-python-310/lib/python3.10/site-packages/certifi/cacert.pem'
load_verify_locations cafile='/Users/ar/dev/dis/venvs/llm-python-310/lib/python3.10/site-packages/certifi/cacert.pem'
DEBUG:httpcore.connection:connect_tcp.started host='localhost' port=11434 local_address=None timeout=30.0 socket_options=None
connect_tcp.started host='localhost' port=11434 local_address=None timeout=30.0 socket_options=None
DEBUG:httpcore.connection:connect_tcp.complete return_value=<httpcore._backends.sync.SyncStream object at 0x3854df8e0>
connect_tcp.complete return_value=<httpcore._backends.sync.SyncStream object at 0x3854df8e0>
DEBUG:httpcore.http11:send_request_headers.started request=<Request [b'POST']>
send_request_headers.started request=<Request [b'POST']>
DEBUG:httpcore.http11:send_request_headers.complete
send_request_headers.complete
DEBUG:httpcore.http11:send_request_body.started request=<Request [b'POST']>
send_request_body.started request=<Request [b'POST']>
DEBUG:httpcore.http11:send_request_body.complete
send_request_body.complete
DEBUG:httpcore.http11:receive_response_headers.started request=<Request [b'POST']>
receive_response_headers.started request=<Request [b'POST']>
DEBUG:urllib3.connectionpool:https://app.posthog.com:443 "POST /batch/ HTTP/1.1" 200 None
https://app.posthog.com:443 "POST /batch/ HTTP/1.1" 200 None
DEBUG:httpcore.http11:receive_response_headers.complete return_value=(b'HTTP/1.1', 200, b'OK', [(b'Content-Type', b'application/json; charset=utf-8'), (b'Date', b'Tue, 30 Jan 2024 07:09:20 GMT'), (b'Content-Length', b'669')])
receive_response_headers.complete return_value=(b'HTTP/1.1', 200, b'OK', [(b'Content-Type', b'application/json; charset=utf-8'), (b'Date', b'Tue, 30 Jan 2024 07:09:20 GMT'), (b'Content-Length', b'669')])
INFO:httpx:HTTP Request: POST http://localhost:11434/api/chat "HTTP/1.1 200 OK"
HTTP Request: POST http://localhost:11434/api/chat "HTTP/1.1 200 OK"
DEBUG:httpcore.http11:receive_response_body.started request=<Request [b'POST']>
receive_response_body.started request=<Request [b'POST']>
DEBUG:httpcore.http11:receive_response_body.complete
receive_response_body.complete
DEBUG:httpcore.http11:response_closed.started
response_closed.started
DEBUG:httpcore.http11:response_closed.complete
response_closed.complete
DEBUG:httpcore.connection:close.started
close.started
DEBUG:httpcore.connection:close.complete
close.complete
**********
Trace: query
    |_query ->  7.439262 seconds
      |_retrieve ->  0.110484 seconds
        |_embedding ->  0.107957 seconds
      |_synthesize ->  7.328671 seconds
        |_templating ->  1.2e-05 seconds
        |_llm ->  7.326003 seconds
**********

====================
Response:

 Lucrezia, a legendary archaeologist, spent her long and fruitful life unearthing the secrets of ancient civilizations. In her twilight years, she was visited by young students who inspired her to share stories of her expeditions and the importance of preserving history for future generations. Together, they continued the exploration of Rome's rich past, inspiring new generations to uncover its mysteries.

====================

CBEvent(event_type=<CBEventType.LLM: 'llm'>, payload={<EventPayload.MESSAGES: 'messages'>: [ChatMessage(role=<MessageRole.SYSTEM: 'system'>, content="You are an expert Q&A system that is trusted around the world.\nAlways answer the query using the provided context information, and not prior knowledge.\nSome rules to follow:\n1. Never directly reference the given context in your answer.\n2. Avoid statements like 'Based on the context, ...' or 'The context information ...' or anything along those lines.", additional_kwargs={}), ChatMessage(role=<MessageRole.USER: 'user'>, content="Context information is below.\n---------------------\nfile_path: ../datasets/bio/Lucrezia/later-life.txt\n\nIn her twilight years, Lucrezia found herself sitting in the sun-drenched courtyard of her villa in Tuscan countryside. Surrounded by the lush greenery and the gentle hum of bees, she reminisced about the many adventures and discoveries that had filled her long and fruitful life.\n\nOne crisp autumn day, as the leaves began to turn golden, Lucrezia received an unexpected visit from a group of young archaeology students. They were eager to learn from the legendary figure who had dedicated her life to unearthing the secrets of ancient civilizations.\n\nLucrezia's heart swelled with pride and gratitude as she shared stories of her expeditions, the thrill of discovery, and the perseverance needed to overcome the challenges that came with archaeology. She spoke passionately about the importance of preserving history for future generations.\n\nAs they sat together in the courtyard, Lucrezia saw the fire in their eyes and felt a renewed sense of purpose. She knew that her legacy would continue through the work of these young scholars, who would carry on the exploration of Rome's rich past.\n\nWith a smile, Lucrezia stood up and walked with her guests to the excavation site she had discovered decades ago. The sun set over the rolling hills, casting a warm glow over the landscape as they began their work. And just like that, Lucrezia was once again part of an adventure, inspiring future generations to continue the journey of unearthing the mysteries of ancient Rome.\n\nfile_path: ../datasets/bio/Lucrezia/later-life.txt\n\nIn her twilight years, Lucrezia found herself sitting in the sun-drenched courtyard of her villa in Tuscan countryside. Surrounded by the lush greenery and the gentle hum of bees, she reminisced about the many adventures and discoveries that had filled her long and fruitful life.\n\nOne crisp autumn day, as the leaves began to turn golden, Lucrezia received an unexpected visit from a group of young archaeology students. They were eager to learn from the legendary figure who had dedicated her life to unearthing the secrets of ancient civilizations.\n\nLucrezia's heart swelled with pride and gratitude as she shared stories of her expeditions, the thrill of discovery, and the perseverance needed to overcome the challenges that came with archaeology. She spoke passionately about the importance of preserving history for future generations.\n\nAs they sat together in the courtyard, Lucrezia saw the fire in their eyes and felt a renewed sense of purpose. She knew that her legacy would continue through the work of these young scholars, who would carry on the exploration of Rome's rich past.\n\nWith a smile, Lucrezia stood up and walked with her guests to the excavation site she had discovered decades ago. The sun set over the rolling hills, casting a warm glow over the landscape as they began their work. And just like that, Lucrezia was once again part of an adventure, inspiring future generations to continue the journey of unearthing the mysteries of ancient Rome.\n---------------------\nGiven the context information and not prior knowledge, answer the query.\nQuery: Summarise Lucrezia's life in 50 words.\nAnswer: ", additional_kwargs={})], <EventPayload.ADDITIONAL_KWARGS: 'additional_kwargs'>: {}, <EventPayload.SERIALIZED: 'serialized'>: {'system_prompt': None, 'pydantic_program_mode': <PydanticProgramMode.DEFAULT: 'default'>, 'base_url': 'http://localhost:11434', 'model': 'mistral', 'temperature': 0.75, 'context_window': 3900, 'request_timeout': 30.0, 'prompt_key': 'prompt', 'additional_kwargs': {}, 'class_name': 'Ollama_llm'}}, time='01/30/2024, 08:09:12.999697', id_='10a91696-5fdf-45a5-a01d-4911f83ecc0a')
dict_keys([<EventPayload.MESSAGES: 'messages'>, <EventPayload.RESPONSE: 'response'>])
assistant:  Lucrezia, a legendary archaeologist, spent her long and fruitful life unearthing the secrets of ancient civilizations. In her twilight years, she was visited by young students who inspired her to share stories of her expeditions and the importance of preserving history for future generations. Together, they continued the exploration of Rome's rich past, inspiring new generations to uncover its mysteries.
```