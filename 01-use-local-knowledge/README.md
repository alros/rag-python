# Results

## Base settings
- model_name = LLAMA2_7B_CHAT
- do_sample = False

## prompt = 'Summarise the symptoms of dementia'

### with base settings

```
The symptoms of dementia can vary widely from person to person, but they typically include:

* Memory loss, such as difficulty remembering recent events or learning new information
* Confusion and disorientation
* Difficulty with language, including trouble finding the right words or understanding what others are saying
* Difficulty with problem-solving, decision-making, and judgment
* Mood changes, such as depression, anxiety, or agitation
* Personality changes, such as becoming more passive or suspicious
* Difficulty with coordination and movement, including trouble with walking or balance
* Difficulty with visual perception, including trouble with reading or recognizing objects
* Difficulty with communication, including trouble with speaking or understanding speech
* Difficulty with initiating or continuing tasks, including trouble with starting or completing activities
* Difficulty with social interactions, including trouble with understanding social cues or interacting with others
* Difficulty with time and place, including trouble with understanding the passage of time or recognizing familiar locations.

It's important to note that these symptoms can be mild at first and gradually worsen over time, and they can also vary in severity and frequency depending on the individual and the type of dementia they have.
```

### do_sample = True

This settings implies `temperature=0.6` and `top_p=0.9` by default

```
The symptoms of dementia can vary widely from person to person, but common signs and symptoms include:

* Memory loss, such as difficulty remembering recent events or learning new information
* Confusion and disorientation
* Difficulty with communication, including trouble finding the right words or understanding what others are saying
* Difficulty with problem-solving, decision-making, and judgment
* Mood changes, such as depression, anxiety, or agitation
* Personality changes, such as becoming more passive or suspicious
* Difficulty with coordination and movement, including trouble with walking or balance
* Difficulty with performing daily activities, such as bathing, dressing, or grooming
* Difficulty with managing finances and other responsibilities
* Difficulty with recognizing familiar people and places
* Difficulty with following instructions or understanding what is happening around them

It's important to note that these symptoms can be mild at first and gradually worsen over time, and may also vary in severity from one person to another. Additionally, the rate of progression of these symptoms can vary across different types of dementia.
```

## prompt = 'Is blindness a symptom of dementia?' with base settings

### with base settings

```
Based on the provided context information, blindness is not a symptom of dementia. According to the text, dementia can cause problems with vision, including difficulty with perception and orientation, but blindness is not listed as a symptom. Therefore, the answer to the query is no, blindness is not a symptom of dementia.
```

### do_sample=True, temperature=100.0, max_time: 120.0

`max_time` was necessary because the model did not return anything after 15+ minutes

```
blob consequences scopeamm linux PicturesissionActguez organ lanç similar Ped probability
```

### do_sample=True, temperature=10.0, max_time: 120.0

Follow up, to test the effect of temperature with limited time

```
volont sulgradleblank� акаде reload assumed Resource rgba mentions Ki turno
```

### do_sample=True, temperature=0.01, max_time: 120.0

Follow up, to test the effect of temperature with limited time

```
Based on the provided context information, blindness is not a sympt
```