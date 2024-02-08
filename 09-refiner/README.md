# Refiner

## Attempt 1

The result of the reranking is empty. The inspection of LlamaIndex's code revealed a problem with the LLM.

`LlamaIndex` version `0.9.22`

Stack:
- `LLM::predict::221`
- `LLMRerank::_postprocess_nodes::90`
- `BaseNodePostprocessor::postprocess_nodes::48`


Prompt (redacted for brevity):

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

Document 1:
creation_date: 2024-02-04
document_title: The Submarine Monster Mystery: Unraveling the Secrets of Unidentified Maritime Creatures in the Depths of the Ocean: From Hypotheses and Public Interest to Scientific Examination and the Sinking of the _Scotia_"

This title encapsulates the overall theme of the document, which revolves around the exploration of unidentified marine creatures, the public's fascination with these enigmas, and the scientific community's attempts to unravel their mysteries. It also highlights the specific case of the sinking of the _Scotia_ and the two main hypotheses – a submarine or a monster – that emerged from this event. The title also suggests the presence of hidden secrets and powerful rivals, adding to the intrigue and suspense surrounding the subject matter.
file_name: TwentyThousandLeaguesUnderTheSea.txt
file_path: kb/gutenberg/TwentyThousandLeaguesUnderTheSea.txt
file_size: 624997
file_type: text/plain
last_accessed_date: 2024-02-04
last_modified_date: 2024-02-03

“Yes, joker,” said Ned Land. “And one fine day the creature plunges,...

Document 2:
creation_date: 2024-02-04
document_title: Paradise Lost: A Poetic Exploration of Man's Disobedience, Eternal Providence, and the Creation Story: The Fall of Man and the Rebellion of Satan, The Defiance of the Fallen Angels, and Their Awakening in Hell"

This title encapsulates all the main entities (Man, God, Satan, angels, Heaven, Hell), themes (rebellion, redemption, suffering, transformation, judgment, divine wrath, heavenly hierarchy, biblical allusions), and events (The Fall of Man, Satan's Rebellion, The Defiance of the Fallen Angels, Their Awakening in Hell) mentioned in the given context.
file_name: ParadiseLost.txt
file_path: kb/gutenberg/ParadiseLost.txt
file_size: 479552
file_type: text/plain
last_accessed_date: 2024-02-04
last_modified_date: 2024-02-03

For Hot, Cold, Moist, and Dry, four champions fierce,...

...

Question: Who is Captain Nemo
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
