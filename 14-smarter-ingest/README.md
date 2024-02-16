# Smarter Ingest

It combines `SimpleDirectoryReader`, `LayoutPDFReader`, and `KeyBERT` from previous experiments in a single reader

Example of output.

```text
================================
chunk 5
Dementia > Contents > 1.1 Disease – 2 > 1.1.4 Prognosis – 12
(dementia, 0.669) / (resulting, 0.0783) / (prerequisites, 0.059) / (added, 0.039) / (especially, -0.0821)
--------------------------------
In Germany, more than 1.7 million people are currently suffering from dementia and about 300,000 new cases are added each year.
Taking into account the demographic development, it becomes clear that the disease dementia poses an enormous challenge in the future, especially since the care and support of people with dementia requires basic knowledge and extensive experience and is associated with a huge amount of time in the course of the disease.
In this chapter, the disease will be presented first.
The knowledge of the different forms and causes of dementia, the resulting losses of cognitive abilities, the typical symptoms and the existing treatment options are prerequisites for an appropriate handling of the affected people.
For each symptom, there are references to the respective chapters that deal with the resulting problems and the possible therapeutic interventions in the care of dementia patients.

================================
chunk 6
Dementia > Contents > 1.1 Disease – 2 > 1.1.4 Prognosis – 12 > 1.1 Disease
(dementia, 0.616) / (malnutrition, 0.2544) / (basis, 0.0078) / (principle, -0.0106) / (central, -0.0361)
--------------------------------
In principle, one distinguishes between primary dementias, which are caused by a degeneration of the brain substance, and dementia-like syndromes, which occur on the basis of another disease, such as malnutrition, alcohol dependence, metabolic disorders or inflammatory diseases of the central nervous system.

================================
chunk 7
Dementia > Contents > 1.1 Disease – 2 > 1.1.4 Prognosis – 12 > 1.1 Disease > Definition > Dementia
(dementia, 0.7149) / (latin, 0.2621) / (signs, 0.079) / (comes, 0.0451) / (specific, -0.0012)
--------------------------------
The term dementia comes from Latin and means translated “without mind”.
It does not mean a specific disease, but the occurrence of various signs of disease that involve a loss of mental abilities.

================================
chunk 8
Dementia > Contents > 1.1 Disease – 2 > 1.1.4 Prognosis – 12 > 1.1 Disease > Definition > Dementia
(dementia, 0.7248) / (defines, 0.1603) / (pronounced, 0.1049) / (reactions, 0.0226) / (including, -0.0648)
--------------------------------
Dementia-like syndrome The World Health Organization WHO defines a dementia-like syndrome as an “acquired global impairment of higher brain functions including memory, the ability to solve everyday problems, the execution of sensomotor and social skills, language and communication as well as the control of emotional reactions without pronounced impairment of consciousness.”
```

Each block contains
- The position of the paragraph.
- The keywords extracted from the text.
- The text of a paragraph without overlapping.
