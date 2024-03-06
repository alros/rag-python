import json

with_context = [{
    "Question": "Have you experienced any difficulty with communicating or understanding language recently?",
    "Explanation": "Given your age and the reported memory loss, I am exploring the possibility of vascular dementia or Alzheimer's disease. While memory loss is a common symptom for both types, vascular dementia can also present with difficulties in communication and understanding language. Therefore, it's essential to explore this further."
}, {
    "Question": "Have you experienced any difficulty in organizing your daily tasks or paying bills recently?",
    "Explanation": "Based on the context and the conversation with the patient, since they mentioned forgetting where they are but not recognizing faces or objects, it is possible that they might have vascular dementia or Alzheimer's disease with mild memory loss symptoms. However, to better understand their condition, it would be helpful to ask about difficulties in organizing daily tasks and managing finances as these can be early indicators of vascular dementia."
}, {
    "Question": "Have you experienced any difficulties with language or reading recently?",
    "Explanation": "Based on the context information, Alzheimer's disease and frontotemporal dementia can cause language and reading difficulties. Since the patient has denied experiencing memory loss or difficulty recognizing familiar faces, these common symptoms of Alzheimer's disease were not present in this conversation. However, the context information mentions that frontotemporal dementia, which affects the frontal lobes of the brain and can cause language and reading difficulties, is another type of dementia."
}, {
    "Question": "Have you experienced any difficulty with language, such as trouble finding the right words or understanding others?",
    "Explanation": "Based on the context information and the conversation with the patient, the symptoms described suggest that the patient may have vascular dementia or a different type of dementia. However, since the patient reported no difficulty recognizing familiar faces or objects, which is a common symptom of Alzheimer's disease and some other types of dementia, I would like to explore further whether there are any language-related difficulties."
}, {
    "Question": "Have you experienced any difficulty with communication, such as finding the right words or understanding what others are saying?",
    "Explanation": "Given the patient's age and reported memory loss, it's important to rule out other types of dementia besides Alzheimer's disease. The context information mentions that vascular dementia and Lewy body dementia also cause communication problems. Asking about difficulty with communication will help differentiate between these types of dementia."
}, {
    "Question": "Have you experienced any problems with language or difficulty finding the right words when speaking?",
    "Explanation": "Based on the context information, Alzheimer's disease and frontotemporal dementia can affect memory and speech. Since the patient mentioned forgetting where they are but not having problems recognizing faces or objects, I would like to explore if they have experienced any difficulties with language."
}, {
    "Question": "Have you experienced any difficulty with language, such as finding the right words to use or understanding what others are saying?",
    "Explanation": "Based on the conversation and the context information provided, it seems that the patient has not reported memory loss related to familiar faces or objects. However, the patient did mention experiencing forgetfulness about their current location. Although this is a symptom of dementia, it could also be due to other reasons such as confusion or disorientation caused by a new environment. To rule out other types of dementia, it would be important to investigate if there are any language-related symptoms. Therefore, the next question should focus on language skills."
}, {
    "Question": "Have you experienced any difficulty with communication such as understanding words or speaking clearly?",
    "Explanation": "Given the patient's age and reported memory loss, I want to explore if they have any difficulties with communication which could indicate different types of dementia. Since they did not report problems recognizing familiar faces or objects, vascular dementia might be less likely based on the context information."
}, {
    "Question": "Have you experienced any difficulties with language, such as finding the right words to use?",
    "Explanation": "Based on the context information provided and the conversation with the patient, it appears that the patient does not have memory loss or difficulty recognizing familiar faces or objects typical of Alzheimer's disease. However, the patient is 75 years old and there are other types of dementia that can affect older adults such as vascular dementia and frontotemporal dementia. Vascular dementia can cause specific problems with language and communication. Therefore, it would be important to ask about any difficulties the patient may have had with language to help narrow down the potential diagnosis."
}, {
    "Question": "Have you experienced any difficulty with language, such as trouble finding the right words or understanding what others are saying?",
    "Explanation": "Given your age and the reported memory loss, it is important to rule out other types of dementia besides Alzheimer's disease. One type, frontotemporal dementia, primarily affects language abilities. Asking this question will help determine if further testing for this condition is necessary."
}]

without_context = [
    {
        "Question": "Have you experienced any issues with learning new information or following complex instructions recently?",
        "Explanation": "Given your reported memory loss and difficulty in recalling recent events, I would like to explore if there are specific types of memory that may be affected."
    }, {
        "Question": "Have you noticed any changes in your ability to learn new things or perform tasks that were once familiar to you?",
        "Explanation": "Given the patient's self-reported memory loss and confusion about current location, it would be important to assess their cognitive abilities further. One common symptom of memory loss is difficulty in learning new information or performing tasks that were once familiar."
    }, {
        "Question": "Have you noticed any changes in your ability to learn new things or perform tasks that were once familiar?",
        "Explanation": "This question is asked to assess the patient's cognitive abilities, specifically their capacity for learning and remembering new information. Since the patient has reported memory loss and forgetting where they are, it's important to investigate if this is a general issue or specific to recent events."
    }, {
        "Question": "Have you noticed any difficulty in remembering names of people or common objects?",
        "Explanation": "Given your age and reported memory loss, it's important to assess if this issue extends to recognizing names. This question will help us understand if there are specific memory problems or if this is a more general cognitive issue."
    }, {
        "Question": "Have you noticed any difficulty in learning new things or remembering information that you have recently learned?",
        "Explanation": "Given your response about forgetting where you are and experiencing memory loss, I'd like to explore further if this also applies to new information. This question will help me assess if there could be underlying cognitive issues."
    }, {
        "Question": "Have you noticed any difficulty in learning new things or remembering recently acquired information?",
        "Explanation": "Given your reported memory loss and difficulty in recalling recent events, I would like to ask if you have also experienced any issues with learning new things or remembering newly acquired information."
    }, {
        "Question": "Have you noticed any difficulties with learning new information or completing familiar tasks recently?",
        "Explanation": "Given your age and previous response about memory loss, I would like to explore further if you have experienced any issues with learning new things or completing tasks that were once familiar to you."
    }, {
        "Question": "Have you experienced any issues with remembering names of people or common objects recently?",
        "Explanation": "Given your age and self-reported memory loss, it is important to assess if this affects your ability to recognize specific names of people or common objects. This information will help us understand the extent and nature of your memory concerns."
    }, {
        "Question": "Have you noticed any difficulty in remembering names of people or common objects?",
        "Explanation": "Given your age and reported memory loss, it's important to assess if this is affecting your ability to recall names of people or common objects. This can help us better understand the nature of your memory difficulties."
    }, {
        "Question": "Have you noticed any changes in your ability to learn new information or perform familiar tasks?",
        "Explanation": "Given the patient's self-reported memory loss and confusion about current location, it is important to assess if these symptoms extend to other cognitive domains such as learning new information or performing familiar tasks."
    }
]

words = [
    ['age'],
    ['Alzheimer'],
    ['bladder'],
    ['brain'],
    ['concentration'],
    ['confusion'],
    ['decision'],
    ['Dementia'],
    ['depression'],
    ['disorientation'], ['emotion'],
    ['fall'],
    ['frontotemporal'],
    ['hallucinations'],
    ['language'],
    ['learn', 'learning'],
    ['Lewy body'],
    ['Memory', 'memory loss'],
    ['mixed'],
    ['mood'],
    ['neurones'],
    ['organisation', 'organisational'],
    ['personality'],
    ['reading'],
    ['remember', 'remembering'],
    ['sleep'],
    ['speech'],
    ['swallow', 'swallowing'],
    ['task'],
    ['tremors'],
    ['understand', 'understanding'],
    ['vascular dementia'],
    ['walking'],
    ['writing']
]

result = []


def contains(text, word):
    text = f' {text.lower()} '
    for remove in ['?', '\'s', '.']:
        text = text.replace(remove, '')
    return f' {word} ' in text


def partial(obj, words):
    partial_result = {
        'Question': 0,
        'Explanation': 0
    }
    contains_q = False
    contains_e = False
    for word in words:
        word = word.lower()
        contains_q = contains(obj['Question'], word) or contains_q
        contains_e = contains(obj['Explanation'], word) or contains_e
    partial_result['Question'] = partial_result['Question'] + (1 if contains_q else 0)
    partial_result['Explanation'] = partial_result['Explanation'] + (1 if contains_e else 0)
    return partial_result


report = {}
for word_list in words:
    key = '/'.join(word_list)
    line = {
        'With Context: Question': 0,
        'With Context: Explanation': 0,
        'Without Context: Question': 0,
        'Without Context: Explanation': 0,
    }
    for doc in with_context:
        partial_line = partial(doc, word_list)
        line['With Context: Question'] = partial_line['Question'] + line['With Context: Question']
        line['With Context: Explanation'] = partial_line['Explanation'] + line['With Context: Explanation']
    for doc in without_context:
        partial_line = partial(doc, word_list)
        line['Without Context: Question'] = partial_line['Question'] + line['Without Context: Question']
        line['Without Context: Explanation'] = partial_line['Explanation'] + line['Without Context: Explanation']
    report[key] = line

print(
    '|Word/s|With/Question|With/Explanation|Without/Question|Without/Explanation|W>Wo Question|W>Wo Explanation|W<Wo Question|W<Wo Explanation|')
print(
    '|------|-------------|----------------|----------------|-------------------|-------------|----------------|-------------|----------------|')
total = 0
total_equivalent_key_used = 0
total_equivalent_key_not_used = 0
total_with_q_gt_without = 0
total_with_e_gt_without = 0
total_with_b_gt_without = 0
total_with_q_lt_without = 0
total_with_e_lt_without = 0
total_with_b_lt_without = 0

for key in report:
    with_q_gt_without = report[key]['With Context: Question'] > report[key]['Without Context: Question']
    with_e_gt_without = report[key]['With Context: Explanation'] > report[key]['Without Context: Explanation']
    with_q_lt_without = report[key]['With Context: Question'] < report[key]['Without Context: Question']
    with_e_lt_without = report[key]['With Context: Explanation'] < report[key]['Without Context: Explanation']

    total_with_q_gt_without = total_with_q_gt_without + (1 if with_q_gt_without else 0)
    total_with_e_gt_without = total_with_e_gt_without + (1 if with_e_gt_without else 0)
    total_with_b_gt_without = total_with_b_gt_without + (1 if with_q_gt_without and with_e_gt_without else 0)

    total_with_q_lt_without = total_with_q_lt_without + (1 if with_q_lt_without else 0)
    total_with_e_lt_without = total_with_e_lt_without + (1 if with_e_lt_without else 0)
    total_with_b_lt_without = total_with_b_lt_without + (1 if with_q_lt_without and with_e_lt_without else 0)

    the_same = not with_q_gt_without and not with_e_gt_without and not with_q_lt_without and not with_e_lt_without
    key_was_used = report[key]['With Context: Question'] > 0 or report[key]['With Context: Explanation'] > 0 \
                   or report[key]['Without Context: Question'] > 0 or report[key]['Without Context: Explanation'] > 0
    total_equivalent_key_used = total_equivalent_key_used + (1 if the_same and key_was_used else 0)
    total_equivalent_key_not_used = total_equivalent_key_not_used + (1 if the_same and not key_was_used else 0)

    print(f'|{key}|\
{report[key]["With Context: Question"]}|\
{report[key]["With Context: Explanation"]}|\
{report[key]["Without Context: Question"]}|\
{report[key]["Without Context: Explanation"]}|\
{with_q_gt_without}|\
{with_e_gt_without}|\
{with_q_lt_without}|\
{with_e_lt_without}|')
    total = total + 1

print('=' * 40)
print(f'Total keys: {total}')
print('-' * 40)
print(f'With>Without for Questions: {total_with_q_gt_without}')
print(f'With>Without for Explanation: {total_with_e_gt_without}')
print(f'With<Without for Questions: {total_with_q_lt_without}')
print(f'With<Without for Explanation: {total_with_e_lt_without}')
print('-' * 40)
print(f'With>Without for Questions and Explanation: {total_with_b_gt_without}')
print(f'With<Without for Questions and Explanation: {total_with_b_lt_without}')

print('-' * 40)
print(f'No difference (key used): {total_equivalent_key_used}')
print(f'No difference (key not used): {total_equivalent_key_not_used}')

