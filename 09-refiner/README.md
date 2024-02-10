# Refiner

## Attempt 1

The result of the reranking is empty. The inspection of LlamaIndex's code revealed a problem with the LLM.

`LlamaIndex` version `0.9.22`

Stack:
- `LLM::predict::221`
- `LLMRerank::_postprocess_nodes::90`
- `BaseNodePostprocessor::postprocess_nodes::48`


Prompt:

type: CHOICE_SELECT (see [https://docs.llamaindex.ai/en/stable/api_reference/prompts.html](https://docs.llamaindex.ai/en/stable/api_reference/prompts.html)) 

```text
A list of documents is shown below. Each document has a number next to it along with a summary of the document. A question is also provided. 
Respond with the numbers of the documents you should consult to answer the question, in order of relevance, as well 
as the relevance score. The relevance score is a number from 1-10 based on how relevant you think the document is to the question.
Do not include any documents that are not relevant to the question. 
Example format: 
Document 1:
<summary of document 1>

Document 2:
<summary of document 2>

...

Document 10:
<summary of document 10>

Question: <question>
Answer:
Doc: 9, Relevance: 7
Doc: 3, Relevance: 4
Doc: 7, Relevance: 3

Let's try this now: 

{context_str}
Question: {query_str}
Answer:
```

Result:

```text
 Captain Nemo is the enigmatic commander of the underwater vessel _Nautilus_. He is a wealthy and mysterious man who has chosen to live in seclusion beneath the sea, exploring its depths and hidden wonders. His true identity, origins, and motivations are unknown to Professor Aronnax and his companions.
```

The LLM did not follow the example. It simply answered the question using the documents as context.

As a result the parsing returned an empty array:

Stack:

- `utils.py:110 -> default_parse_choice_select_answer_fn`
- `LLMRerank::_postprocess_nodes::96`
- `BaseNodePostprocessor::postprocess_nodes::48`

Note: reducing the number of retrieved nodes does not seem to help.

## Attempt 2

Customising the prompt:

### Variation 1

```text
A list of documents is shown below. Each document has a number next to it along with a summary of the document. A question is also provided. 
Respond with the numbers of the documents you should consult to answer the question, in order of relevance, as well 
as the relevance score. The relevance score is a number from 1-10 based on how relevant you think the document is to the question.
Do not include any documents that are not relevant to the question. 
Example format: 
Document 1:
<summary of document 1>

Document 2:
<summary of document 2>

...

Document 10:
<summary of document 10>

Question: <question>
Answer:
Doc: 9, Relevance: 7
Doc: 3, Relevance: 4
Doc: 7, Relevance: 3

Let's try this now: 

{context_str}
```

Result: timed out.

### Variation 2

```text
A list of documents is shown below. Each document has a number next to it along with a summary of the document. 
Given the following question:
{query_str}

Respond with the numbers of the documents you should consult to answer the question, in order of relevance, as well 
as the relevance score. The relevance score is a number from 1-10 based on how relevant you think the document is to the question.
Do not include any documents that are not relevant to the question. 
Example format: 
Document 1:
<summary of document 1>

Document 2:
<summary of document 2>

...

Document 10:
<summary of document 10>

Question: <question>
Answer:
Doc: 9, Relevance: 7
Doc: 3, Relevance: 4
Doc: 7, Relevance: 3

Let's try this now: 

{context_str}
```

Result: timed out.

### Variation 3

```text
A list of documents is shown below. Each document has a number next to it along with a summary of the document.
Given the following question:
{query_str}

Respond with the numbers of the documents you should consult to answer the question, in order of relevance, as well 
as the relevance score. The relevance score is a number from 1-10 based on how relevant you think the document is to the question.
Do not include any documents that are not relevant to the question. 
Example format: 
Document 1:
<summary of document 1>

Document 2:
<summary of document 2>

...

Document 10:
<summary of document 10>

Question: <question>
Answer:
Doc: 9, Relevance: 7
Doc: 3, Relevance: 4
Doc: 7, Relevance: 3

Let's try this now: 

{context_str}
Answer:
```

Result:

```text
The document appears to be an excerpt from Jules Verne's "Twenty Thousand Leagues Under the Sea." In this passage, the protagonist, Professor Aronnax, is preparing to escape from the submarine _Nautilus_ with Ned Land. He reflects on his time aboard the vessel and wonders about Captain Nemo's reaction to their departure. Aronnax also expresses anxiety about the potential discovery of their plan and the consequences it might have for Captain Nemo. The document does not contain any specific information related to marine creatures or scientific examination, but it contributes to the overall theme of the document series by showcasing the protagonist's thoughts and feelings as they prepare to leave the mysterious submarine.
```

### Variation 4

```text
A list of documents is shown below. Each document has a number next to it along with a summary of the document.

Given the following question: 
{query_str}

Rank the documents by relevance. 
Example format: 
Document 1:
<summary of document 1>

Document 2:
<summary of document 2>

...

Document 10:
<summary of document 10>

Question: <question>
Answer:
Doc: 9, Relevance: 7
Doc: 3, Relevance: 4
Doc: 7, Relevance: 3

Let's try this now: 

{context_str}
Answer:
```

Result:
```text
The document appears to be an excerpt from Jules Verne's "Twenty Thousand Leagues Under the Sea." In this passage, the narrator, Professor Aronnax, is preparing to escape from Captain Nemo and his submarine, the _Nautilus_. He is uncertain of how Captain Nemo will react to their departure and fears discovery or retaliation. The document also describes the anticipation and excitement of the impending escape, as well as the narrator's nostalgia for the wonders he has encountered during his time aboard the _Nautilus_. There is no mention of unidentified marine creatures or the hypotheses surrounding the sinking of the _Scotia_ in this particular passage.
```

## Attempt 3

### Variation 1

I created an alternative db with smaller chunks: 128 instead of 1024 and retried with `refined_attempt1`.

Still no luck. The raw response is:

```text
 Doc: 1-3, Relevance: 10 (All three documents have the same title and are about Jules Verne's "Twenty Thousand Leagues Under the Sea," which features Captain Nemo as a central character. Therefore, they are all highly relevant to the question.)
```

It still results with an empty array.

### Variation 2

I reduced the extraction to the minimum: only two chunks. 

```text
 Doc: 1, Relevance: 10
Doc: 2, Relevance: 3

The first document directly mentions Captain Nemo in the text, making it the most relevant document to answer the question. The second document has the same title and some similar content, but it does not mention Captain Nemo explicitly.
```

The reranking worked and only one node was returned.

### Variation 3

Same as above, but three chunks.

```text
 Doc: 1, 3, Relevance: 10 (These documents provide information about Captain Nemo from the context of Jules Verne's "Twenty Thousand Leagues Under the Sea." They confirm that Captain Nemo is a character in the novel and give some details about him, such as his name and actions related to exploration and technology.)

Doc: 2, Relevance: 1 (This document does not contain information directly relevant to the question. It only repeats the title of the book with no new information about Captain Nemo.)
```

The parsing fails:

```text
ValueError: could not convert string to float: '1 (This document does not contain information directly relevant to the question. It only repeats the title of the book with no new information about Captain Nemo.)'
```

### Variation 4

Three chunks, using Llama 2 instead of Mistral.

```text
To answer the question "Who is Captain Nemo?", you should consult Documents 1 and 2.

Document 1 provides a comprehensive title for this document, which encompasses the various unique entities, titles, and themes found in "The Iceberg" and related works, providing a broader understanding of their place within the body of work by Jules Verne. This document also includes information about Captain Nemo's isolation, altered spirits, and taciturnity, which are relevant to the question.

Document 2 provides additional context and information about Captain Nemo's home-sickness and his seclusion on the _Nautilus_. This document also includes quotes from the text that provide insight into Captain Nemo's personality and motivations.

Therefore, the relevance scores for these documents are:

Document 1: 8/10
Document 2: 9/10

Based on these scores, you should consult Documents 1 and 2 to answer the question "Who is Captain Nemo?".
```

Error:

```text
IndexError: list index out of range
```

I repeated the experiment multiple times. Although the input contains 3 nodes, the LLM does not include a rank for all of them.

## Attempt 4

Using `refiner_attempt2`, Llama2, chunks = 128, retrieving three chunks, and customised prompt:

```text
A list of documents is shown below. Each document has a number next to it along with a summary of the document. A question is also provided. 
Respond with the numbers of the documents you should consult to answer the question, in order of relevance, as well 
as the relevance score. The relevance score is a number from 1-10 based on how relevant you think the document is to the question.
Include a rank for all the documents. 
Example format: 
Document 1:
<summary of document 1>

Document 2:
<summary of document 2>

...

Document 10:
<summary of document 10>

Question: <question>
Answer:
Doc: 9, Relevance: 7
Doc: 3, Relevance: 4
Doc: 7, Relevance: 3

Let's try this now: 

{context_str}
Question: {query_str}
Answer:
```

Response:

```text
 Captain Nemo is the enigmatic captain of the submarine _Nautilus_ in Jules Verne's classic novel "Twenty Thousand Leagues Under the Sea." He is a solitary and mysterious figure, leading an independent existence in the deep ocean with his crew. He is known for his advanced technological abilities and his desire to explore the underwater world. His true identity, origins, and motives are shrouded in mystery.
```

The final list of reranked node is again empty. 

## Conclusion

Reranking using an LLM does not seem a safe strategy that guarantees results.

