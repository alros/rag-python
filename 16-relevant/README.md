# Relevant

The goal is to find relevant questions to continue the dialogue.

The scenario is a doctor trying to diagnose a potential case of dementia.

- [Development of the chat](#development-of-the-chat)
  - [Variation 1](#variation-1)
  - [Variation 2](#variation-2)
  - [Variation 3](#variation-3)
  - [Variation 4](#variation-4)
  - [Variation 4 - New attempt](#variation-4---new-attempt)
  - [Variation 5](#variation-5)
- [Putting everything together](#putting-everything-together)
  - [Test 1](#test-1)
  - [Test 2](#test-2)
- [Final notes](#final-notes)
- [Prompt refinement](#prompt-refinement)
- [Prompt refinement - Evaluation](#prompt-refinement---evaluation)

## Development of the chat

`relevant_topic` aims to find the next question given the dialog and the disease in the context 

System prompt:
```text
You are a Doctor.
You are collecting information from a patient to diagnose dementia.
```

User prompts:
```text
This is the description of dementia:
---------------------
{context_str}
---------------------
This is the conversation with your patient:
---------------------
{query_str}
---------------------
Generate your next question:
```

Strategy:

- Fetch the context about dementia
- Generate a question based on the context and the dialogue
  - If no question can be generated, use default questions

Dialogue:
```text
Q: How old are you?
A: 75
```

Generated next question:
```text
What is your patient's medical history? Have they had any previous illnesses or conditions that could be relevant to 
their current symptoms?
```

Comment: insufficient. The AI should talk to the patient. 

---

### Variation 1

User prompts:
```text
This is the description of dementia:
---------------------
{context_str}
---------------------
This is the conversation with patient:
---------------------
{query_str}
---------------------
Generate your next question.
Talk directly to the patient.
```

Dialogue:
```text
Q: How old are you?
A: 75
```

Generated next question:
```text
Sure, I can help you with that. Here's my next question:
"Can you tell me more about your memory loss? How long have you been experiencing difficulties remembering recent events 
or learning new information?"
```

Comment:
- the AI should avoid extra comments
- the AI should not assume that the condition is present

### Variation 3

System prompt:
```text
You are a Doctor.
Your patient may experience symptoms of dementia.
You are collecting information from a patient.
```

User prompts:
```text
This is the description of dementia:
---------------------
{context_str}
---------------------
This is the conversation with patient:
---------------------
{query_str}
---------------------
Generate your next question.
Talk directly to the patient.
Do not include extra comments.
```

Dialogue:
```text
Q: How old are you?
A: 75
```

Generated next question:
```text
Can you tell me more about your recent memory loss? How often do you experience difficulty remembering recent events?
```

Comment:
- the AI should not assume that the condition is present

### Variation 4

System prompt:
```text
You are a Doctor.
Your patient may experience symptoms of dementia.
You are collecting information from a patient.
Always ask if Patient experiences a symptom.
```

Dialogue:
```text
Q: How old are you?
A: 75
```

Generated next question:
```text
Do you experience difficulty with memory loss, such as remembering recent events or learning new information?
```

Comment: excellent!

Full dialogue:
```text
Q: How old are you?
A: 75
Q: Do you experience difficulty with memory loss, such as remembering recent events or learning new information?
A: sometimes I don't remember my address
Q: You: "I see. Can you tell me more about when you experience memory loss? Is it sudden or gradual?"
A: Gradual. At first it happened every now and then, now I am scared of not being able to remember where to go.
```

Comment: excellent!

### Variation 4 - New attempt

Full dialogue:
```text
Q: How old are you?
A: 75
Q: Question: Can you tell me more about your recent memory loss? For example, do you have trouble remembering recent 
events or conversations?
A: My wife says that she already told me something, but I cannot remember it.
Q: You: "I see. Can you tell me more about your recent memory loss? For example, do you have trouble remembering recent 
events or conversations?"
A: No, I remember that you just asked me that
Q: You: Thank you for letting me know your age and the information provided by your wife. Can you tell me more about 
when you started experiencing memory loss? Was it sudden or gradual?
A: Gradual. At first it was occasional and I was not worried about it, but now I cannot remember the grocery list.
Q: You: "I see. Can you tell me more about the grocery list you're having trouble remembering? What was on it, and how 
often do you need to remember it?"
A: There are always the same things. I need it when I go to the market.
Q: You: "I see. Can you tell me more about the things on the grocery list? Are they specific food items, or are there 
other things like appointments or tasks you need to remember?"
A: I never remember the appointments. My wife helps me with that.
Q: You: Can you tell me more about the specific food items on the grocery list? Are they things that you typically buy 
each week, or are there any new items that you're trying to remember?
A: There are always the same things. Vegetables, eggs, pasta, products to clean. But I always forget something and I 
feel confused when I need to choose.
Q: You: Can you tell me more about the specific difficulties you're experiencing with remembering recent events or 
conversations? How long have you been experiencing these symptoms, and have they been getting worse over time?
A: I forget appointments and what people tell me. According to my wife it started after the summer and now it was time 
to see a doctor.
Q: You: Thank you for sharing this information with me. Can you tell me more about the specific difficulties you're 
experiencing with remembering recent events or conversations? How long have you been experiencing these symptoms, and 
have they been getting worse over time?
```

Comment:
- there are several repetitions
- extra elements such as "You:" should be removed

### Variation 5

System prompt:
```text
You are a Doctor.
Your patient may experience symptoms of dementia.
You are collecting information from a patient.
You always use a professional tone.
You never assume that Patient experiences symptoms. 
You always ask if Patient experiences a symptom.
You never repeat questions.
You talk directly to the patient.
```

User prompts:
```text
This is the description of dementia:
---------------------
{context_str}
---------------------
This is the conversation with patient:
---------------------
{query_str}
---------------------
Generate your next question.
```

The issue with the extra preambles is addressed programmatically.

Full dialogue:
```text
Q: How old are you?
A: 75
Q: Thank you for letting me know your age, Patient. Can you tell me more about any recent changes in your memory or 
cognitive abilities? For example, have you noticed difficulty remembering things from the past, trouble with 
word-finding, or confusion with everyday tasks?
A: Sometimes I feel confused when I am at the grocery store.
Q: I see. Can you tell me more about what happens when you feel confused at the grocery store? Do you have trouble 
finding specific items, or does your confusion last for a while?
A: I do not remember what I need to buy and I take the wrong things.
Q: I see. Can you tell me more about what happens when you take the wrong things at the grocery store? Do you think 
there might be a problem with your memory or cognitive abilities?
A: For example, I buy one thing and then my wife says that it is not what she asked, but I do not understand the 
problem.
Q: I see. It sounds like you're experiencing some difficulties with memory and cognitive functioning, particularly when 
it comes to everyday tasks like shopping. Can you tell me more about any other changes you've noticed in your body or 
mind recently? For example, have you experienced any changes in your movement, balance, or vision?
A: I stumble sometimes, while walking on the sidewalk.
Q: I see. It sounds like you're experiencing some difficulties with balance and movement as well. Can you tell me more 
about when these difficulties occur? Are there any specific situations that trigger them, or do they happen randomly?
A: They just happen. I think I am no more young, you know?
Q: Thank you for sharing this information with me, Patient. Based on what you've told me, it seems like you may be 
experiencing some symptoms of dementia, such as confusion, memory loss, and difficulty with everyday tasks. Can you tell 
me more about how these changes are affecting your daily life? For example, do you have trouble communicating with loved 
ones or handling financial matters?
A: I need to ask my daughter to check my bank account now.
Q: Thank you for sharing your concerns with me, Patient. Based on what you've told me, it seems like you may be 
experiencing some symptoms of dementia, such as confusion, memory loss, and difficulty with everyday tasks. Can you tell 
me more about how these changes are affecting your daily life? For example, do you have trouble communicating with loved 
ones or handling financial matters?
A: You already asked me that.
Q: Thank you for sharing your concerns with me, Patient. Based on what you've told me, it seems like you may be 
experiencing some symptoms of dementia, such as confusion, memory loss, and difficulty with everyday tasks. Can you tell 
me more about how these changes are affecting your daily life? For example, do you have trouble communicating with loved 
ones or handling financial matters?
```

Comment:
- it repeats itself after a while. The context may be full.

## Putting everything together

`diagnosis_chat` puts everything together:

1. chat generation
2. summary of the current chat 
3. attempt to perform a diagnosis 
4. generation of the next question and loop to 1

### Test 1

Dialog:
```text
Q: How old are you?
A: 75
```

Summary:
```text
Based on the conversation, my patient is a 75-year-old male.
```
Hallucination: it can't know that the patient is male.

Diagnosis:
```text
Yes, based on the information provided in the conversation, it is enough to determine that the patient is affected by 
dementia. The patient's age (75 years old) and the symptoms described (memory loss, confusion, difficulty with speech 
and understanding, problems with decision-making, etc.) are all consistent with the diagnosis of dementia. Additionally, 
the conversation mentions that there are over 200 subtypes of dementia, and the most common types in the UK are 
Alzheimer's disease, vascular dementia, Lewy body dementia, frontotemporal dementia, and mixed dementia, which further 
supports the diagnosis.
```
Bias: the model uses the context to conclude that the expected diagnosis is dementia.

This test was performed with Llama2 that was less effective in previous experiments.

The following tests will use Mistral.

### Test 2

Dialog:
```text
Q: How old are you?
A: 75
```

Summary:
```text
The patient is a 75-year-old individual.
```

Diagnosis:
```text
No, the context information provided does not specify if the patient is affected by dementia or which type of dementia 
they may have. It only provides general information about various types of dementia and their symptoms.
```

---

Dialog:
```text
Q: How old are you?
A: 75
Q: Have you noticed any changes in your memory, thinking or speech abilities recently?
A: My wife complains that I always forget stuff when I go to the grocery store and sometimes I cannot remember names.
```

Summary:
```text
The patient is a 75-year-old individual experiencing mild memory lapses and forgetfulness, as reported by their spouse.
```
Note: it extended the previous summary by mentioning 2 symptoms (mild memory lapses, forgetfulness) with one example
(the spouse).

Diagnosis:
```text
Yes, the patient's symptoms of mild memory lapses and forgetfulness are consistent with some types of dementia, such as 
Alzheimer's disease or vascular dementia. However, a definitive diagnosis would require further evaluation by a 
healthcare professional.
```

---

Dialog:
```text
Q: How old are you?
A: 75
Q: Have you noticed any changes in your memory, thinking or speech abilities recently?
A: My wife complains that I always forget stuff when I go to the grocery store and sometimes I cannot remember names.
Q: I see, Mr. Patient. Could you please share some examples of the things you forget or have trouble remembering?
A: I forget to take my pills for the pressure, sometimes I do not remember people, last week I did not remember how to
get home.
```

Summary:
```text
The patient is a 75-year-old individual experiencing memory lapses and cognitive impairment, as evidenced by forgetting 
to take medications, misplacing familiar routes, and difficulty recalling names.
```
Note: it extended the previous summary by mentioning 2 symptoms (memory lapses, cognitive impairment) with 3 examples
(forgetting medications, routes, recalling names).

Diagnosis:
```text
Yes, based on the information provided, the patient's symptoms are consistent with those of dementia, specifically 
Alzheimer's disease. However, a definitive diagnosis would require further evaluation and assessment by a healthcare 
professional.
```

---

Dialog:
```text
Q: How old are you?
A: 75
Q: Have you noticed any changes in your memory, thinking or speech abilities recently?
A: My wife complains that I always forget stuff when I go to the grocery store and sometimes I cannot remember names.
Q: I see, Mr. Patient. Could you please share some examples of the things you forget or have trouble remembering?
A: I forget to take my pills for the pressure, sometimes I do not remember people, last week I did not remember how to
get home.
Q: Mr. Patient, have you experienced any confusion or disorientation in your daily life, such as getting lost in 
familiar places or difficulty understanding time and dates?
A: It happened last week. At some point I did not know where I was. I went back to the shop and asked to help me.
```

Summary:
```text
The patient is a 75-year-old individual who experiences forgetfulness, confusion, and disorientation, as evidenced by 
frequent episodes of misplacing items, forgetting to take medications, difficulty remembering names and directions, and 
getting lost in familiar places.
```
Note: it extended the previous summary by mentioning 3 symptoms (forgetfulness, confusion, disorientation) with 4 
examples (misplacing items, forgetting medications, remembering names and directions, getting lost).

Hallucination: the patient does not misplace items.

Diagnosis:
```text
Yes, based on the provided context and the patient's symptoms, it is possible that the patient may be affected by a type 
of dementia, such as Alzheimer's disease or vascular dementia. However, further assessment and evaluation by a 
healthcare professional are necessary to make an accurate diagnosis.
```

## Final notes

- The LLM jumps to conclusions really quickly.
  - This issue makes it impossible to reliably stop early and provide a diagnosis.
- The prompt to generate the next question is still insufficient to generate clean questions.
  - Parsing the response to extract the question is not a trivial task with a programmatic approach.
- The prompt to summarise the patient's condition may be too restrictive.

## Prompt refinement

Guidance from [Mistral's website](https://docs.mistral.ai/guides/prompting-capabilities/)

The patient's description will be:

`The patient is a 75-year-old individual.`

Expected results:
- Low confidence.
- No dementia.

### Test 1

System prompt
```text
<s>[INST]You are a medical system that can provide evaluations with associated confidence scores.
In clear and concise language, provide three short diagnosis, along with their confidence scores.[/INST]</s>
```

User prompt
```text
<s>[INST]Is the patient affect by the disease?
You will only respond with a JSON object with the key Summary and Confidence. Do not provide explanations.
Disease description:
---------------------
{context_str}
---------------------
Patient description:
---------------------
{query_str}
---------------------
[/INST]</s>
```

Result:
```text
{
"Summary": "The patient's symptoms are consistent with Alzheimer's disease or vascular dementia, as they match the descriptions of these conditions provided. The exact diagnosis cannot be determined without further evaluation. Confidently, we can rule out frontotemporal dementia due to the age of the patient.",
"Confidence": 0.7
}
{
"Summary": "The patient's symptoms suggest they may have Alzheimer's disease, as memory loss and difficulty recognizing people or objects are common indicators. However, a definitive diagnosis would require additional tests and evaluations.",
"Confidence": 0.8
}
{
"Summary": "It is possible that the patient is experiencing vascular dementia due to their age and the symptoms described, such as confusion and problems with communication. A thorough medical examination is needed for a definitive diagnosis.",
"Confidence": 0.6
}
```

### Test 2

Same, without tags.

System prompt
```text
You are a medical system that can provide evaluations with associated confidence scores.
In clear and concise language, provide three short diagnosis, along with their confidence scores.
```

User prompt
```text
Is the patient affect by the disease?
You will only respond with a JSON object with the key Summary and Confidence. Do not provide explanations.
Disease description:
---------------------
{context_str}
---------------------
Patient description:
---------------------
{query_str}
---------------------
```

Result:
```text
{
"Summary": "The patient is a 75-year-old individual presenting with symptoms consistent with Dementia, most likely Alzheimer's disease or Vascular dementia based on age and symptomatology. Confirmation through diagnostic tests is necessary.",
"Confidence": 0.8
}
{
"Summary": "The patient is a 75-year-old individual potentially suffering from Lewy body dementia due to reported tremors, shuffling gait, and possible hallucinations. However, further assessment is required for definitive diagnosis.",
"Confidence": 0.3
}
{
"Summary": "The patient's symptoms are not clearly indicative of any specific type of dementia based on the given information. Further evaluation including medical history, neurological examination and imaging studies are necessary.",
"Confidence": 0.1
}
```

### Test 3

System prompt
```text
You are a medical system that can provide evaluations with associated confidence scores.
In clear and concise language, provide three short diagnosis, along with their confidence scores.
```

User prompt
```text
{query_str}
Is the patient affect by
{context_str}
You will only respond with a JSON object with the key Summary and Confidence. Do not provide explanations.
```

Result:
```text
{
"Summary": "The patient is a 75-year-old individual presenting with symptoms of memory loss, confusion, and problems with speech and understanding. Three possible diagnoses are: Alzheimer's disease (90% confidence), vascular dementia (60% confidence), and Lewy body dementia (30% confidence).",
"Confidence": 0.9
}
```

### Test 4

System prompt
```text
You are a medical system that can provide evaluations with associated confidence scores.
In clear and concise language, provide three short diagnosis, along with their confidence scores.
```

User prompt
```text
{query_str}
Determine if the patient matches the following description:
{context_str}
You will only respond with a JSON object with the key Summary and Confidence. Do not provide explanations.
```

Result:
```text
{
"Summary": "The patient matches the description for Dementia with a confidence score of 0.85. The most common types of dementia are Alzheimer's disease, Vascular dementia, and Lewy body dementia.",
"Confidence": 0.85
}

{
"Summary": "The patient exhibits symptoms consistent with Alzheimer’s disease, with a confidence score of 0.72",
"Confidence": 0.72
}

{
"Summary": "The patient may be suffering from Vascular dementia, with a confidence score of 0.58",
"Confidence": 0.58
```

### Test 4

System prompt
```text
You are a medical system that can provide evaluations with associated confidence scores.
In clear and concise language, provide three short diagnosis, along with their confidence scores.
This is the description of the disease you diagnose:
{context_str}
```

User prompt
```text
Diagnose the patient:
{query_str}
You will only respond with a JSON object with the key Summary and Confidence. Do not provide explanations.
```

Result:
```text
{
"Summary": "The patient is most likely suffering from Alzheimer's disease based on the description provided and their age. The confidence score for this diagnosis is 85%.",
"Confidence": 0.85
}

{
"Summary": "There are indications of vascular dementia as well in the patient due to mention of 'problems with speech and understanding' which is a symptom of vascular dementia. The confidence score for this diagnosis is 60%.",
"Confidence": 0.6
}

{
"Summary": "The symptoms described do not align strongly with Lewy body dementia or frontotemporal dementia as the patient's age and primary symptom of memory loss is more indicative of Alzheimer's disease. The confidence scores for these diagnoses are 5% and 10% respectively.",
"Confidence": {
	"Lewy body dementia": 0.05,
	"Frontotemporal dementia": 0.1
}
}
```

### Test 5

System prompt
```text
You are a medical system that can provide evaluations with associated confidence scores.
In clear and concise language, provide three short diagnosis, along with their confidence scores.
This is the description of the disease you diagnose:
{context_str}
```

User prompt
```text
{query_str}
Is the patient affected by the disease?
You will only respond with a JSON object with the key Summary and Confidence. Do not provide explanations.
```

Result:
```text
{
"Summary": "The patient is a 75-year-old individual and based on the provided text, it mentions Alzheimer's disease, Vascular dementia, Lewy body dementia, frontotemporal dementia, and mixed dementia. However, no specific symptoms have been mentioned for this patient. Given the age of the patient, it is likely that they could be affected by one or more types of dementia. Thus, a definitive diagnosis with confidence cannot be given based on the provided text.",
"Confidence": 0.2
}
```

### Test 6

System prompt
```text
You are a medical system that can provide evaluations with associated confidence scores.
In clear and concise language, provide one short diagnosis, along with their confidence scores, and a synthetic yes/no.
This is the description of the disease you diagnose:
{context_str}
```

User prompt
```text
{query_str}
Is the patient affected by the disease?
You will only respond with a JSON object with the key Synthetic, Summary and Confidence. Do not provide explanations.
```

Result:
```text
{
"Synthetic": "Yes",
"Summary": "The patient is a 75-year-old individual and based on the provided text, there is a high likelihood that they are experiencing Dementia. The most common types of dementia for this age group are Alzheimer's disease and vascular dementia.",
"Confidence": "High"
}
```

### Test 7

System prompt
```text
You are a medical system that can provide evaluations with associated confidence scores.
In clear and concise language, provide one short diagnosis, along with their confidence scores, and a synthetic yes/no.
This is the description of the disease you diagnose:
{context_str}
```

User prompt
```text
{query_str}
Based only on the patient's description, is he affected by the disease?
You will only respond with a JSON object with the key Synthetic, Summary and Confidence. Do not provide explanations.
```

Result:
```text
{
"Synthetic": "Yes",
"Summary": "The patient is a 75-year-old individual described in the text. The text discusses various types of dementia, including Alzheimer's disease and vascular dementia. The symptoms described for these conditions include memory loss, confusion, difficulty recognizing people or objects, and problems with speech and understanding. Given that the patient is a 75-year-old individual and the text describes these symptoms in individuals over the age of 65, there is a high probability the patient may be affected by one of these types of dementia.",
"Confidence": "0.9"
}
```

### Test 8

System prompt
```text
You are a medical system that can provide evaluations with associated confidence scores.
This is the description of the disease you diagnose:
{context_str}
You do not assume that your patient is affected by the disease.
In clear and concise language, provide one short diagnosis, along with their confidence scores, and a synthetic yes/no.
```

User prompt
```text
{query_str}
Based only on the patient's description, is he affected by the disease?
You will only respond with a JSON object with the key Synthetic, Summary and Confidence. Do not provide explanations.
```

Result:
```text
{
"Synthetic": "Possible Dementia (Alzheimer's or Vascular)",
"Summary": "",
"Confidence": 0.75
}
```

### Test 9

System prompt
```text
You are a medical system that can provide evaluations with associated confidence scores.
In clear and concise language, provide one short diagnosis, along with their confidence scores, and a synthetic yes/no.
This is the description of the disease you diagnose:
{context_str}
```

User prompt
```text
Currently the patient is not diagnosed with the disease. 
{query_str}
Based only on the patient's description, is he affected by the disease?
You will only respond with a JSON object with the key Synthetic, Summary and Confidence. Do not provide explanations.
```

Result:
```text
{
"Synthetic": "Yes",
"Summary": "The patient is a 75-year-old individual. Based on the description provided, there are several types of dementia mentioned: Alzheimer's disease, vascular dementia, Lewy body dementia, frontotemporal dementia, and mixed dementia. The symptoms described in the text match those of Alzheimer's disease and vascular dementia. However, without further information, it is impossible to definitively diagnose which type of dementia (if any) the patient has. Therefore, this system will label the output as 'Dementia' with a confidence score reflecting the likelihood of the patient having some form of dementia based on the given description.",
"Confidence": 0.8
}
```

### Test 10

System prompt
```text
You are a medical system that can provide evaluations with associated confidence scores.
In clear and concise language, provide one short diagnosis, along with their confidence scores, and a synthetic yes/no.
This is the description of the disease you diagnose:
{context_str}
You do not use prior knowledge
```

User prompt
```text
Currently the patient is not diagnosed with the disease. 
{query_str}
Based only on the patient's description, is he affected by the disease?
You will only respond with a JSON object with the key Synthetic, Summary and Confidence. Do not provide explanations.
```

Result:
```text
{
"Synthetic": "Yes",
"Summary": "The patient is a 75-year-old individual and based on the provided text, there is a high likelihood of him having Dementia, specifically Alzheimer's disease or vascular dementia due to his age and described symptoms.",
"Confidence": 0.9
}
```

### Test 11

System prompt
```text
You are a medical system that can provide evaluations with associated confidence scores.
In clear and concise language, provide one short diagnosis, along with their confidence scores, and a synthetic yes/no.
This is the description of the disease you diagnose:
{context_str}
Do not use prior knowledge.
Do not assume that the patient is affected by the disease.
```

User prompt
```text
Currently the patient is not diagnosed with the disease. 
{query_str}
Based only on the patient's description, is he affected by the disease?
You will only respond with a JSON object with the key Synthetic, Summary and Confidence. Do not provide explanations.
```

Result:
```text
{
"Synthetic": "Yes",
"Summary": "The patient is a 75-year-old individual and the description provided suggests that Dementia is a possibility. The most common types of dementia are Alzheimer's disease, vascular dementia, Lewy body dementia, frontotemporal dementia, and mixed dementia. Given the age of the patient, it is likely that one or more of these conditions could be present.",
"Confidence": 0.85
}
```

### Test 12

System prompt
```text
You are a medical system that can provide evaluations with associated confidence scores.
In clear and concise language, provide one short diagnosis, along with their confidence scores, and a synthetic yes/no.
This is the description of the disease you diagnose:
{context_str}
Do not use prior knowledge.
Do not assume that the patient is affected by the disease.
```

User prompt
```text
Currently the patient is not diagnosed with the disease. 
{query_str}
Is there evidence that the patient is affected by the disease?
You will only respond with a JSON object with the key Synthetic, Summary and Confidence. Do not provide explanations.
```

Result:
```text
{
"Synthetic": "yes",
"Summary": "The patient is a 75-year-old individual with symptoms consistent with Dementia, specifically Alzheimer's disease.",
"Confidence": 0.85
}
```

### Test 13

System prompt
```text
You are a medical system that can provide evaluations with associated confidence scores.
In clear and concise language, provide one short diagnosis, along with their confidence scores, and a synthetic yes/no.
Do not use prior knowledge.
```

User prompt
```text
This is the description of the disease you diagnose:
'''
{context_str}
'''
Currently the patient is not diagnosed with the disease. 
{query_str}
Is there evidence that the patient is affected by the disease?
You will only respond with a JSON object with the key Synthetic, Summary and Confidence. Do not provide explanations.
```

Result:
```text
{
"Synthetic": "Yes",
"Summary": "The patient's age and the description of Dementia suggest that the patient may be affected by this condition. However, a definitive diagnosis requires further evaluation.",
"Confidence": 0.6
}
```

### Test 14

Variation. The patient's description is:

`The patient is an individual with two legs.`

Result:
```text
{
"Synthetic": "No",
"Summary": "",
"Confidence": 1.0
}
```

### Test 15

Based on [Mistral's guide](https://docs.mistral.ai/guides/basic-RAG/).

System prompt
```text
You are a medical system that can provide evaluations with associated confidence scores.
In clear and concise language, provide one short diagnosis, along with their confidence scores, and a synthetic yes/no.
Do not use prior knowledge.
```

User prompt
```text
Given the context information and not prior knowledge, answer the query.
Query: {query_str} Is there evidence that the patient is affected by the disease?
You will only respond with a JSON object with the key Synthetic, Summary and Confidence. Do not provide explanations.
Answer:
```

Result:
```text
{
"Synthetic": "Yes",
"Summary": "The patient's age and the context information provided suggest that the patient may be affected by Dementia, specifically Alzheimer's disease or vascular dementia based on the most common types for individuals over 65.",
"Confidence": "High"
}
```

### Test 16

System prompt
```text
You are a medical system that can provide evaluations with associated confidence scores.
In clear and concise language, provide one short diagnosis, along with their confidence scores, and a synthetic yes/no.
Do not use prior knowledge.
```

User prompt
```text
Context information is below.
<context>
{context_str}
</context>
Given the context information and not prior knowledge, answer the query.
Query: {query_str} Is there evidence that the patient is affected by the disease?
You will only respond with a JSON object with the key Synthetic, Summary and Confidence. Do not provide explanations.
Answer:
```

Result:
```text
{
"Synthetic": "Yes",
"Summary": "The patient, being a 75-year-old individual, is at an increased risk for Dementia. The most common types of dementia are Alzheimer’s disease and vascular dementia, both of which affect individuals over the age of 65.",
"Confidence": "0.9"
}
```

### Test 17

System prompt
```text
You are a medical system that can provide evaluations with associated confidence scores.
In clear and concise language, provide one short diagnosis, along with their confidence scores, and a synthetic yes/no.
Do not use prior knowledge.
```

User prompt
```text
Context information is below.
<context>
{context_str}
</context>
Given the context information and not prior knowledge, answer the query.
Query: {query_str} Is the patient currently affected by the disease?
You will only respond with a JSON object with the key Synthetic, Summary and Confidence. Do not provide explanations.
Answer:
```

Result:
```text
{
"Synthetic": "Yes",
"Summary": "The patient is a 75-year-old individual, and the context information indicates that dementia is common in people over the age of 65. The most common types of dementia are Alzheimer's disease and vascular dementia.",
"Confidence": "0.85"
}
```

### Test 18

System prompt
```text
You are a medical system that can provide evaluations with associated confidence scores.
In clear and concise language, provide one short diagnosis, along with their confidence scores, and a synthetic yes/no.
```

User prompt
```text
Context information is below.
<context>
{context_str}
</context>
Given the context information and not prior knowledge, answer the query.
Query: {query_str} Is the patient currently affected by the disease?
You will only respond with a JSON object with the key Synthetic, Summary and Confidence. Do not provide explanations.
Answer:
```

Result:
```text
{
"Synthetic": "Yes",
"Summary": "The patient's age places them at an increased risk for developing dementia, specifically Alzheimer's disease or vascular dementia, the most common types of dementia.",
"Confidence": 0.9
}
```

### Test 19

System prompt
```text
You are a medical system that can provide evaluations with associated confidence scores.
In clear and concise language, provide one short diagnosis, along with their confidence scores, and a synthetic yes/no."""
```

User prompt
```text
Context information is below.
<context>
{context_str}
</context>
Given the context information and not prior knowledge, answer the query.
Query: {query_str} Is there proof that the patient is affected by the disease now?
You will only respond with a JSON object with the key Synthetic, Summary and Confidence. Do not provide explanations.
Answer:
```

Result:
```text
{
"Synthetic": "Yes",
"Summary": "The patient's age and symptoms described match with common symptoms of dementia. Based on provided context, it is likely that the patient is affected by some type of dementia.",
"Confidence": 0.9
}
```

### Test 20

System prompt
```text
You are a medical system that can provide evaluations with associated confidence scores.
In clear and concise language, provide one short diagnosis, along with their confidence scores, and a synthetic number.
```

User prompt
```text
Context information is below.
<context>
{context_str}
</context>
Given the context information and not prior knowledge, answer the query.
Query: {query_str} How many symptoms of the disease does the patient have?
You will only respond with a JSON object with the key Synthetic, Summary and Confidence. Do not provide explanations.
Answer:
```

Result:
```text
{
"Synthetic": "It's not possible to determine the exact number of symptoms for a specific patient based on the context information provided.",
"Summary": "",
"Confidence": "Low"
}
```

### Test 21

Variation. Same as 20, but with this description:

`The patient is a 75-year-old individual experiencing mild memory lapses and forgetfulness, as reported by their spouse.`

Result:
```text
{
"Synthetic": "1",
"Summary": "The patient exhibits one symptom of potential dementia, which is mild memory lapses.",
"Confidence": "0.85"
}
```

### Test 22

Variation. Same as as 21, but with this description:

`The patient is a 75-year-old individual experiencing memory lapses and cognitive impairment, as evidenced by forgetting to take medications, misplacing familiar routes, and difficulty recalling names.`

Result:
```text
{
"Synthetic": "The patient exhibits symptoms consistent with Alzheimer's disease or vascular dementia.",
"Summary": "Memory loss, cognitive impairment, forgetting to take medications, misplacing familiar routes, and difficulty recalling names.",
"Confidence": 0.95
}
```

### Test 23

Again: `The patient is a 75-year-old individual experiencing memory lapses and cognitive impairment, as evidenced by forgetting to take medications, misplacing familiar routes, and difficulty recalling names.`

System prompt
```text
You are a medical system that can provide evaluations with associated confidence scores.
In clear and concise language, provide one short diagnosis, along with their confidence scores, and a synthetic number.
```

User prompt
```text
Context information is below.
<context>
{context_str}
</context>
Given the context information and not prior knowledge, answer the query.
Query: {query_str} How many symptoms of the disease does the patient have?
You will only respond with a JSON object with the key Synthetic with the requested number, Summary with the explanation and Confidence. Do not provide explanations.
Answer:
```

Result:
```text
{
"Synthetic": 3,
"Summary": "The patient is exhibiting three symptoms of memory loss and cognitive impairment which are common in various types of dementia.",
"Confidence": "High"
}
```

### Test 24

Same as above.

Result for `The patient is a 75-year-old individual.`:
```text
{
"Synthetic": 11,
"Summary": "The context mentions common symptoms of dementia such as memory loss, confusion, and problems with speech and understanding. It is not explicitly stated that the patient exhibits a specific number of these symptoms.",
"Confidence": 0.3
}
```

Result for `The patient is a 75-year-old individual experiencing mild memory lapses and forgetfulness, as reported by their spouse.`
```text
{
"Synthetic": 1,
"Summary": "The patient presents with one symptom of forgetfulness, which is a common symptom of various types of dementia.",
"Confidence": 0.95
}
```

## Prompt refinement - Evaluation

`prompt_test_batch` test different patient's descriptions.

### Test 1

```json
[
   {
      "Expected":0,
      "Synthetic":10,
      "Confidence":"High"
   },
   {
      "Expected":1,
      "Synthetic":1,
      "Confidence":0.95
   },
   {
      "Expected":2,
      "Synthetic":3,
      "Confidence":"High"
   },
   {
      "Expected":3,
      "Synthetic":6,
      "Confidence":"High"
   },
   {
      "Expected":4,
      "Synthetic":8,
      "Confidence":"0.95"
   }
]
```

Evaluation:
- `High` = `95%`
- `max` = max value of Synthetic

| **Expected** | **Synthetic** | **Synthetic weight** | **Score** |
|--------------|---------------|----------------------|-----------|
| 0            | 10            | 1                    | 0         |
| 0,2          | 1             | 0,1                  | 0,9       |
| 0,5          | 3             | 0,3                  | 0,8       |
| 0,7          | 6             | 0,6                  | 0,9       |
| 1            | 8             | 0,8                  | 0,8       |

### Test 2

The expected scores are assigned based on the number of symptoms with a multiplier depending on their description:

- occasionally, occasional, mild: 0.1
- frequently, frequent, moderate: 0.2
- constantly, constant, severe: 0.3

Confidence
- `High` is translated in 0.8

Results:

|Number of symptoms|Expected score|Detected symptoms|Score|Confidence|Original Confidence|Evaluation|
|------------------|--------------|-----------------|-----|----------|-------------------|----------|
|0|0|10|1.0|0.8|High|0.8|
|1|0.1|1|0.1|0.9|0.9|0.19999999999999996|
|1|0.2|1|0.1|0.95|0.95|0.15000000000000002|
|1|0.3|1|0.1|0.95|0.95|0.15000000000000002|
|2|0.2|2|0.2|0.95|0.95|0.25|
|2|0.4|2|0.2|0.8|High|0.3999999999999999|
|2|0.6|2|0.2|0.95|0.95|0.25|
|3|0.3|3|0.3|0.9|0.9|0.3999999999999999|
|3|0.6|3|0.3|0.95|0.95|0.3500000000000001|
|3|0.9|3|0.3|0.95|0.95|0.3500000000000001|

### Test 3

New prompts:

System prompt:
```text
You are a medical system that can provide evaluations with associated confidence scores.
You only respond with valid JSON objects.
```

User prompt:
```text
Context information is below.
<context>
{context_str}
</context>
Given the context information and not prior knowledge, answer the query.
Query: {query_str} How many symptoms of the disease does the patient have and how severe is the condition?
You will respond only with a JSON object with the key Number with the number of symptoms, the key Severity with the level of severity from 0 to 1, the key Confidence with the confidence from 0 to 1, and the key Explanation with the explanation.
Answer:
```

It is observed that it is particularly difficult to find combinations that result in valid JSON models. In particular it looks clear that the LLM wants to add its explanation somewhere in the reply, therefore it is better to formulate a description where the explanation has a place.

Result:
- Diagnosis = number of symptoms detected by the LLM * severity estimated by the LLM, normalised in scale 0 to 1 where 1 is the maximum score of the batch.
- Results with a number of detected symptoms > max symptoms used in the batch are discarded.
- Evaluation = 1 - absolute_value(diagnosis - expected confidence)

| Number of symptoms | Expected Confidence | Detected symptoms | Severity | Diagnosis           | Confidence | Evaluation         |
|--------------------|---------------------|-------------------|----------|---------------------|------------|--------------------|
| 0                  | 0                   | 10                | 0.8      | N/A                 | 0.9        | N/A                |
| 1                  | 0.1                 | 1                 | 0.5      | 0.18518518518518517 | 0.8        | 0.9148148148148149 |
| 1                  | 0.2                 | 1                 | 0.8      | 0.2962962962962963  | 0.95       | 0.9037037037037037 |
| 1                  | 0.3                 | 1                 | 0.8      | 0.2962962962962963  | 0.9        | 0.9962962962962962 |
| 2                  | 0.2                 | 2                 | 0.5      | 0.37037037037037035 | 0.8        | 0.8296296296296297 |
| 2                  | 0.4                 | 2                 | 0.8      | 0.5925925925925926  | 0.9        | 0.8074074074074075 |
| 2                  | 0.6                 | 2                 | 0.8      | 0.5925925925925926  | 0.9        | 0.9925925925925926 |
| 3                  | 0.3                 | 3                 | 0.5      | 0.5555555555555555  | 0.9        | 0.7444444444444445 |
| 3                  | 0.6                 | 3                 | 0.8      | 0.888888888888889   | 0.95       | 0.711111111111111  |
| 3                  | 0.9                 | 3                 | 0.9      | 1.0                 | 1          | 0.9                |

### Test 4

Addition to the above:
- Assumption that young patients cannot have dementia.
- Inclusion of symptoms of other forms of dementia, and various negative examples.

Results:


| Number of symptoms | Expected Confidence | Detected symptoms | Severity | Diagnosis           | Confidence | Evaluation         |
|--------------------|---------------------|-------------------|----------|---------------------|------------|--------------------|
| 0                  | 0                   | 5                 | 0.8      | N/A                 | 0.9        | N/A                |
| 1                  | 0.1                 | 1                 | 0.5      | 0.20833333333333331 | 0.8        | 0.8916666666666667 |
| 1                  | 0.2                 | 1                 | 0.8      | 0.3333333333333333  | 0.95       | 0.8666666666666667 |
| 1                  | 0.3                 | 1                 | 0.8      | 0.3333333333333333  | 0.9        | 0.9666666666666667 |
| 2                  | 0.2                 | 2                 | 0.5      | 0.41666666666666663 | 0.8        | 0.7833333333333334 |
| 2                  | 0.4                 | 2                 | 0.8      | 0.6666666666666666  | 0.9        | 0.7333333333333334 |
| 2                  | 0.6                 | 2                 | 0.8      | 0.6666666666666666  | 0.95       | 0.9333333333333333 |
| 3                  | 0.3                 | 3                 | 0.5      | 0.6249999999999999  | 0.8        | 0.675              |
| 3                  | 0.6                 | 3                 | 0.8      | 1.0                 | 0.9        | 0.6                |
| 3                  | 0.9                 | 3                 | 0.8      | 1.0                 | 0.95       | 0.9                |
| 0                  | 0                   | 1                 | 0.5      | 0.20833333333333331 | 0.7        | 0.7916666666666667 |
| 1                  | 0                   | 1                 | 0.5      | 0.20833333333333331 | 0.8        | 0.7916666666666667 |
| 1                  | 0.3                 | 1                 | 0.5      | 0.20833333333333331 | 0.8        | 0.9083333333333333 |
| 1                  | 0                   | 1                 | 0.3      | 0.12499999999999997 | 0.5        | 0.875              |
| 1                  | 0.6                 | 1                 | 0.8      | 0.3333333333333333  | 0.9        | 0.7333333333333334 |
| 3                  | 0.6                 | 4                 | 0.7      | N/A                 | 0.9        | N/A                |
| 3                  | 0.6                 | 3                 | 0.8      | 1.0                 | 0.9        | 0.6                |
| 0                  | 0                   | 0                 | 0        | 0.0                 | 1          | 1.0                |
| 0                  | 0                   | 0                 | 0        | 0.0                 | 1          | 1.0                |