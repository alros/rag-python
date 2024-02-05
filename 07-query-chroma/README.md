# Test Chroma

The experiment uses a Chroma Db built with the `gutenberg` dataset.

## Run 1

Query: `Who is captain Nemo?`

Response:

- id=a410a808-31e9-42d2-84ea-73c971ee1540 distances=0.8756459951400757 file=TwentyThousandLeaguesUnderTheSea.txt
- id=d58900bf-ecd4-4e43-af49-ee84fdb4253e distances=0.9018428921699524 file=TwentyThousandLeaguesUnderTheSea.txt

## Run 2

Query: `Who is captain Nemo?`

Filter: `where={'file_name': 'OnTheOriginOfSpeciesByMeansOfNaturalSelection.txt'}`

Response:

- id=6d8fc9c5-ac53-48dc-ad40-d2fcbe0e68eb distances=1.6489834785461426 file=OnTheOriginOfSpeciesByMeansOfNaturalSelection.txt
- id=414222ea-cfda-4221-ac0c-3688e4551619 distances=1.6729110479354858 file=OnTheOriginOfSpeciesByMeansOfNaturalSelection.txt

The distance of these results is higher.

## Run 3

Query: `Who is captain Nemo?`

Filter: `where={'file_name': 'OnTheOriginOfSpeciesByMeansOfNaturalSelection.txt'}`

Filter: `where_document={'$contains':'dog'}`

Response:

- id=de4caf97-3827-4fb1-ad2b-ab3b5a121228 distances=1.7505704164505005 file=OnTheOriginOfSpeciesByMeansOfNaturalSelection.txt
- id=b30174bb-3873-40d2-b0cd-b9c704b2052b distances=1.7678406238555908 file=OnTheOriginOfSpeciesByMeansOfNaturalSelection.txt

The distance of these results is even higher.

# More filters

ref: [https://docs.trychroma.com/usage-guide](https://docs.trychroma.com/usage-guide)