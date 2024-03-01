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