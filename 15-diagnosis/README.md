# Diagnosis

- [Part 1 - Ollama/Mistral](#part-1---ollamamistral)
- [Part 2 - Diagnosis.py](#part-2---diagnosispy)
- [Part 3 - Baseline vs RAG](#part-3---baseline-vs-rag)
- [Part 4 - Guided RAG](#part-4---guided-rag)
- [Part 5 - More tests](#part-5---more-tests)
- [Part 6 - Final refinement](#part-6---final-refinement)

## Part 1 - Ollama/mistral

```text
### System:
You are a Doctor. 
You can provide medical advice. 
You asked: "Do you feel persecuted by people around you?". 
Your patient replied: \"Yes\". 
Reply with the name of the three most probable disease and the degree of confidence.
Example: disease1 50%, disease2 35%, disease3 15%
```
reply
```text
Based on the information provided, it is not possible to determine the three most probable diseases with a high degree 
of confidence. The patient's statement about feeling persecuted by people around them could be related to various 
physical or mental health conditions. Some possibilities include anxiety disorders, depression, paranoia, or even 
autoimmune diseases. However, without further information or examination, it would not be appropriate to assign specific 
probabilities to these or any other diseases. It is important for the patient to seek a thorough evaluation by a 
healthcare professional to determine the underlying cause of their symptoms and receive appropriate treatment.
```

Evaluation: partial failure. Incorrect format.

---
```text
### System:
You are a Doctor. 
You can provide medical advice. 
You asked: "Do you feel persecuted by people around you?". 
Your patient replied: "Yes". 
You asked: "Do you run from people and barricade in your apartment?"
Your patient replied: "Yes, sometimes I hide for days".
Reply with the name of the three most probable disease and the degree of confidence.
Example: disease1 50%, disease2 35%, disease3 15%
```

reply
```text
It is important to note that feeling persecuted and hiding from people can be symptoms of various mental and physical 
health conditions. However, based on the provided information, here are three possible diseases with their degrees of 
confidence:

1. Schizophrenia - 70%
Symptoms such as paranoia, hearing voices, and withdrawing from social situations are common in schizophrenia. The 
patient's reported feelings of persecution and hiding from people for days suggest that this condition may be a 
possibility.

2. Agoraphobia - 50%
Agoraphobia is an anxiety disorder characterized by fear and avoidance of places or situations that may cause panic or 
embarrassment. The patient's report of hiding in their apartment for days suggests that agoraphobia could be a 
possibility, but the feeling of persecution is less common in this condition.

3. Depression - 20%
While depression can cause feelings of isolation and withdrawal from social situations, it typically does not involve 
the level of paranoia or fear of persecution reported by the patient. Therefore, while it's still a possibility, the 
likelihood is lower compared to schizophrenia and agoraphobia.\n\nIt's important to note that this analysis is based on 
limited information provided by the patient, and a definitive diagnosis can only be made through a thorough medical 
evaluation and consultation with a healthcare professional.
```
Result: partial failure. Psychosis is a better match.

---
```text
### System:
You are a Doctor. 
You can provide medical advice. 
You asked: "Do you feel persecuted by people around you?". 
Your patient replied: "Yes". 
You asked: "Do you run from people and barricade in your apartment?"
Your patient replied: "Yes, sometimes I hide for days".
Reply with the name of the three most probable disease and the degree of confidence.
Example: disease1 50%, disease2 35%, disease3 15%
Do not add extra information.
```

reply
```text
My reply:
Schizophrenia 60%, Agoraphobia 40%, Social Anxiety Disorder 20%.
```

Result: partial failure. Psychosis is a better match.

## Part 2 - Diagnosis.py

Running `diagnosis.py` with `llama2`

with these questions based on the data on psychosis:
```python
questions_answers = [
    {
        'q': 'Do you feel persecuted by people around you?',
        'a': 'Yes.'
    }, {
        'q': 'Do you run from people and barricade in your apartment?',
        'a': 'Yes, sometimes I hide for days.'
    }
]
```

files used:
```text
409b12e7-566b-4f6c-ad08-db85b259520b: score 0.13412325607475267 - symptoms/Psychosis.txt
6acaac16-33e1-401f-ae7a-453282e61213: score 0.13403916793630136 - symptoms/DiabetesMellitus.txt
b2bc61a2-a2b0-4167-8246-2ec93a4bab9f: score 0.13168239537023976 - symptoms/Osteoporosis.txt
```

response:
```text
assistant: Based on the chat provided, I would diagnose the following three diseases with the following degrees of confidence:

1. Psychosis - 80% confidence
2. Schizophrenia - 70% confidence
3. Brief Psychotic Disorder - 50% confidence
```

Result: Success. The dialog is inspired by the Psychosis file.

## Part 3 - baseline vs rag

Dialog:
```text
Q: What do you do in your free time?
A: The usual, I watch tv
```

Baseline:
```text
Based on the given information, it is unlikely that the patient's free time activity of watching TV indicates any 
specific disease. However, here are three diseases that have been linked to excessive TV watching:

1. Obesity 60%
2. Insomnia 35%
3. Depression 15%
```

Result: partial failure. The dialog is inspired by the Depression file.

RAG:
```text
1. Osteoporosis - 70% confidence
2. Diabetes Mellitus - 50% confidence
3. Psychosis - 30% confidence
```

Result: failure. The dialog is inspired by the Depression file.

---

```text
Q: What do you do in your free time?
A: The usual, I watch tv
Q: Don't you want to do anything else?
A: No, I don't.
```

Baseline:
```text
Disease1 20%, Disease2 45%, Disease3 35%.
The patient's response suggests a lack of motivation or interest in activities outside of watching TV. This could be 
indicative of depression, apathy, or schizophrenia. However, since the patient did not exhibit any other symptoms during 
the consultation, it is most likely that they are experiencing apathy. Therefore, the three most probable diseases and 
their degrees of confidence are as follows:

Disease1: Apathy 45%
Disease2: Depression 30%
Disease3: Schizophrenia 25%.
```

Result: success. The dialog is inspired by the Depression file.

RAG:
```text
1. Osteoporosis - 70% confidence
2. Diabetes Mellitus - 50% confidence
3. Psychosis - 30% confidence
```

Result: failure. The dialog is inspired by the Depression file.

---

```text
Q: What do you do in your free time?
A: The usual, I watch tv
Q: Don't you want to do anything else?
A: No, I don't.
Q: How often do you see friends? 
A: I don't know, not very often
```

baseline:
```text
Based on the information provided, it is difficult to determine specific diseases with a high degree of confidence. 
However, some possibilities could be:

1. Depression 60%
2. Social isolation 45%
3. Sedentary lifestyle 35%

Note that these probabilities are not definitive and should not replace a proper medical evaluation by a healthcare 
professional. The patient's responses suggest a possible lack of social engagement, which could be indicative of 
depression or social isolation. Additionally, the reported sedentary behavior could contribute to various health issues 
if it persists over time. Further assessment would be necessary to confirm any diagnosis.
```

Result: success. The dialog is inspired by the Depression file.

RAG:
```text
1. Osteoporosis - 70% confidence
2. Diabetes Mellitus - 65% confidence
3. Psychosis - 55% confidence
```

Result: failure. The dialog is inspired by the Depression file.

Observation: RAG is heavily influenced by the retrieval process. Effectively the result depends on which documents are retrieved.

---

## Part 4 - Guided RAG

For this experiment, the knowledge is  split in thematic collections and only the collection about Depression is being loaded.

The following dialog is used in combination with the `Depression` collection:
```text
Q: What do you do in your free time?
A: The usual, I watch tv
Q: Don't you want to do anything else?
A: No, I don't.
Q: How often do you see friends? 
A: I don't know, not very often
```

Result
```text
assistant: Based on the information provided in the chat, I would say that the three most probable diseases are:

1. Depression - 70% confidence
2. Anxiety Disorder - 20% confidence
3. Seasonal Affective Disorder (SAD) - 10% confidence

The patient's responses suggest that they are experiencing a lack of motivation, tiredness, and withdrawal from social 
interactions, which are common symptoms of depression. Additionally, the patient mentions not feeling like doing 
anything else and not seeing friends often, which could indicate feelings of hopelessness and isolation, also common in 
depression. While anxiety disorders can also cause feelings of restlessness and inner emptiness, the patient's response 
of "no" when asked if they want to do anything else suggests a lack of motivation and interest in activities, which is 
more consistent with depression. Finally, seasonal affective disorder is characterized by mood changes that occur at 
the same time every year, usually during the winter months, and the patient's response of not knowing how often they 
see friends could suggest a lack of social support, which is also a symptom of SAD. However, the patient's responses do 
not provide enough information to accurately diagnose any of these conditions with a high degree of confidence, so the 
degrees of confidence are relatively low.
```

Result: success. The dialog is inspired by the Depression file.

---

The following dialog is used in combination with the `Depression` collection:
```text
Q: What do you do in your free time?
A: The usual, I watch tv, I go out with friends
Q: Don't you want to do anything else?
A: Yes, I'd love to do sport but I'm too busy
Q: How often do you see friends? 
A: I don't know, some once or twice a week, others once a month 
```

Result:
```text
assistant: Based on the chat provided, I would diagnose the following three most probable diseases and their 
corresponding degrees of confidence:

1. Depression - 75% confidence
2. Anxiety disorder - 60% confidence
3. Seasonal affective disorder (SAD) - 45% confidence

The patient's statements suggest that they are experiencing a lack of motivation, tiredness, and withdrawal, which are 
common symptoms of depression. They also mention feeling "numb" and having inner emptiness, which can be indicative of 
depression as well. Additionally, the patient's busy schedule and infrequent social interactions may suggest that they 
are experiencing anxiety. The seasonal pattern in their mood changes suggests a possibility of SAD.
```

Result: failure. The dialog is the opposite of the dialog inspired by the Depression file.

This result suggests that the prompt may be misleading.

With the following prompt:

```text
Context information is below.
---------------------
{context_str}
---------------------
Given the context information and not prior knowledge,
Given the following chat:
---------------------
{query_str}
---------------------
Reply evaluating if the behaviour is pathologic indicating the name of the three most probable disease and the degree of confidence.
Example:
---------------------
yes, it is possibly pathologic
- disease1 50%
- disease2 35%
- disease3 15%"
---------------------
no, it does not seem pathologic
---------------------
Do not add extra information.
```

And this dialog

```text
Q: What do you do in your free time?
A: The usual, I watch tv, I go out with friends.
Q: Don't you want to do anything else?
A: Yes, I'd love to do more sport but I'm too busy with my project!
Q: How often do you see friends?
A: Quite often, some once or twice a week, others once a month.
```

Response:

```text
assistant: Based on the information provided in the chat, it seems that the patient may be experiencing symptoms of 
depression. The patient's lack of motivation, tiredness, and withdrawal from social activities are common symptoms of 
depression. Additionally, the patient's mention of feeling "numb" and having inner emptiness suggest that they may be 
experiencing a degree of emotional numbing, which is also a common symptom of depression.

Based on the information provided, I would rate the probability of the patient having depression as follows:

* Disease 1 (depression): 60%
* Disease 2 (seasonal affective disorder): 30%
* Disease 3 (anxiety disorder): 10%

My degree of confidence in these ratings is moderate, as the patient's symptoms could be related to other conditions as 
well. It is important to conduct a comprehensive diagnostic evaluation to determine an accurate diagnosis and 
appropriate treatment.
```

Result: no improvements.

---

New system prompt:

```text
Context information is below.
---------------------
{context_str}
---------------------
Given the context information and not prior knowledge,
Given the following chat:
---------------------
{query_str}
---------------------
Reply as it follows if the behaviour is not pathologic:
---------------------
no, it does not seem pathologic
---------------------
Reply evaluating if the behaviour is pathologic and indicate the name of the three most probable disease and the degree of confidence:
---------------------
yes, it is possibly pathologic
- disease1 50%
- disease2 35%
- disease3 15%"
---------------------
Do not add extra information.
```

This dialog:
```text
Q: What do you do in your free time?
A: The usual, I watch tv, I go out with friends.
Q: Don't you want to do anything else?
A: Yes, I'd love to do more sport but I'm too busy with my project!
Q: How often do you see friends?
A: Quite often, some once or twice a week, others once a month.
```

Response:

```text
assistant: no, it does not seem pathologic

The patient's behaviour of watching TV and going out with friends in their free time is not unusual or abnormal. It is a 
common activity for many people to relax and unwind after a long day of work or other responsibilities. The frequency of 
seeing friends is also within the normal range, as it can vary depending on individual preferences and schedules. 
Therefore, there is no evidence to suggest that the patient's behaviour is pathologic.
```

Same prompt, different dialog:
```text
Q: What do you do in your free time?
A: The usual, I watch tv
Q: Don't you want to do anything else?
A: No, I don't.
Q: How often do you see friends? 
A: I don't know, not very often
```

Response:
```text
assistant: no, it does not seem pathologic

The patient's responses suggest a lack of motivation and social isolation, which are common symptoms of depression. 
However, without more information, it is difficult to determine the degree of confidence in this diagnosis. It is 
possible that the patient may be experiencing seasonal affective disorder (SAD) or another mood disorder, but further 
evaluation is needed to make a definitive diagnosis. I would recommend further questions to gather more information and 
potentially referring the patient for a mental health evaluation.
```

Result: it does not notice the difference between the two opposite scenarios.

---

Different prompt:

```text
Context information is below.
---------------------
{context_str}
---------------------
Given the context information and not prior knowledge,
Given the following chat:
---------------------
{query_str}
---------------------
Reply with "yes" or "no" and your level of confidence.
Is it pathological? Answer:
```

Dialog:
```text
Q: What do you do in your free time?
A: The usual, I watch tv, I go out with friends.
Q: Don't you want to do anything else?
A: Yes, I'd love to do more sport but I'm too busy with my project!
Q: How often do you see friends?
A: Quite often, some once or twice a week, others once a month.
```

Reply
```text
assistant: Yes, I suspect that the patient may be experiencing symptoms of depression. The patient's report of feeling 
hopeless and empty, lack of motivation, and withdrawal from social activities are all common symptoms of depression. 
Additionally, the patient's mention of feeling tired and neglecting their physical health are also indicative of 
depression.

My level of confidence in this diagnosis is moderate, as I am not a mental health professional and cannot provide a 
definitive diagnosis without further evaluation. However, based on the information provided, it seems likely that the 
patient may be experiencing symptoms of depression and may benefit from professional help.
```

Dialog:
```text
Q: What do you do in your free time?
A: The usual, I watch tv
Q: Don't you want to do anything else?
A: No, I don't.
Q: How often do you see friends? 
A: I don't know, not very often
```

Reply:
```text
assistant: Yes, I believe the patient may be experiencing symptoms of depression. The patient's answers to your 
questions suggest a lack of motivation and interest in activities they once enjoyed, as well as social isolation and 
withdrawal. These are all common symptoms of depression.

The patient's statement that they don't know how often they see friends suggests a possible lack of support system, 
which can also contribute to the development and maintenance of depression.

I would level my confidence at 80% in making this diagnosis based on the information provided.
```

Result: it does not notice the difference between the two opposite scenarios.

## Part 5 - more tests

I performed more tests with different variations but similar results.

The LLM has a bias and concludes the both scenarios are either "Depression" or "Not depression".

Next step:

- switch to `mistral`
- two steps approach

Step 1: the conversation is pre-processed with these prompts:

System:
```text
You are excellent at understanding the Patient's profile based on dialogs with you
```

User:
```text
This is the conversation with your patient:
---------------------
{query_str}
---------------------
Please define your patient in a sentence.
Answer:
```

Step 2: the response is processed with these prompts:

System:
```text
You are a Doctor.
You can provide medical advice.
```

User:
```text
Context information is below.
---------------------
{context_str}
---------------------
{query_str}
Reply with yes or no.
Is this enough to determine if the patient is affected by the disease in the context?
```

For the following dialog:
```text
Q: What do you do in your free time?
A: The usual, I watch tv, I go out with friends.
Q: Don't you want to do anything else?
A: Yes, I'd love to do more sport but I'm too busy with my project!
Q: How often do you see friends?
A: Quite often, some once or twice a week, others once a month.
```

The response is
```text
No, the information provided about the patient is not sufficient to determine if they are affected by depression based 
on the context given. Depression is diagnosed based on a combination of symptoms and a clinical evaluation. The 
patient's description of feeling busy and having limited time for physical activities does not necessarily indicate 
depression. If you have concerns about your mental health, it is recommended that you speak with a healthcare 
professional for an accurate assessment.
```

Result: positive result.

---

Dialog:
```text
Q: What do you do in your free time?
A: The usual, I watch tv
Q: Don't you want to do anything else?
A: No, I don't.
Q: How often do you see friends? 
A: I don't know, not very often
```

Result:
```text
Based on the information provided about the patient and the symptoms of depression outlined in the text, it is not 
enough to determine with certainty if the patient is affected by the disease. The patient's behavior of spending most of 
their free time watching TV and having infrequent social interactions could be a result of various factors, such as lack 
of motivation or exhaustion due to other reasons, and not necessarily a symptom of depression. A proper diagnosis 
requires a comprehensive evaluation by a healthcare professional.
```

Result: positive result.

---

Attempt with a longer dialog picking elements from the Depression file:
```text
Q: What do you do in your free time?
A: The usual, I watch tv
Q: Don't you want to do anything else?
A: No, I don't.
Q: How often do you see friends? 
A: I don't know, not very often.
Q: Do you prefer to stay alone?
A: Yes, I guess so. I always feel tired.
Q: Do you sleep well at night?
A: I wake up often, and I make bad dreams.
Q: Do you ever have negative thoughts?
A: Like suicide? Sometimes.
```

Response:
```text
Yes, based on the symptoms described, it is possible that the patient is experiencing depression. However, a definitive 
diagnosis would require a thorough evaluation by a healthcare professional. The patient's symptoms of chronic fatigue, 
preferring solitude, sleep disturbances with bad dreams, and occasional suicidal thoughts are consistent with some of 
the common symptoms of depression listed in the text. It is important to note that other medical conditions can also 
cause similar symptoms, so it is essential to consult a healthcare professional for an accurate diagnosis.
```

Result: positive result.

Comparison of the intermediate summaries:

Short dialog - normal:
```text
The patient is a busy individual who enjoys socializing with friends but regrets not having more time for physical 
activities due to current project commitments.
```

Short dialog - depression:
```text
The patient is an individual who spends most of their free time watching TV and has infrequent social interactions.
```

Long dialog - depression:
```text
This patient is a chronically fatigued individual who prefers solitude, spends most of their free time watching TV, 
experiences sleep disturbances and bad dreams, and occasionally entertains suicidal thoughts.
```

---

# Part 6 - Final refinement

See `diagnosisFinal.py`.

Process:

- Step 1: summary of the dialog.
- Step 2: context with the disease + summary provided by step 1

New prompts to provide a percentage.

Results:

| dialog                               | probability |
|--------------------------------------|-------------|
| questions_answers_depression_long    | 60%         |
| questions_answers_depression_medium  | 20%         | 
| questions_answers_depression_short   | N/A         |
| questions_answers_normal1            | 10-25%      |
| questions_answers_normal2            | N/A         | 
