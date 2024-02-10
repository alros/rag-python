# Test Chroma

- [Test 1](#Test_1)
  - [Test 1 Control](#Test_1_Control)
- [Test 2](#Test_2)
  - [Test 2 Control](#Test_2_Control)

## Test 1

Based on `08-query-chroma`.

Using a db build with:
- dataset `gutemberg`
- length of the chunks: 128
- 5 keywords

Question: `Who is captain Nemo?`

Question keywords:
```text
('nemo', 0.7322)
('captain', 0.5324)
```

Response:

```text
id=029d4442-5336-4ab9-a1fe-181339d3c18b
distances=0.6432109274382903
file=TwentyThousandLeaguesUnderTheSea.txt
keywords=nemo,manuscript,waves,retaliations,tell
Does Captain Nemo still live? And does he still follow
under the ocean those frightful retaliations? Or, did he stop after the
last hecatomb?

Will the waves one day carry to him this manuscript containing the
history of his life? Shall I ever know the name of this man? Will the
missing vessel tell us by its nationality that of Captain Nemo?

I hope so.
```

```text
id=5aa46db9-2f5d-4769-85d1-53a26d63aa83
distances=0.6856973171234131
file=TwentyThousandLeaguesUnderTheSea.txt
keywords=nemo,pitiless,united,approaching,chimerical
One part of the mysterious existence of Captain Nemo had
been unveiled; and, if his identity had not been recognised, at least,
the nations united against him were no longer hunting a chimerical
creature, but a man who had vowed a deadly hatred against them. All the
formidable past rose before me. Instead of meeting friends on board the
approaching ship, we could only expect pitiless enemies. But the shot
rattled about us.
```

```text
id=be576052-173c-4124-92e1-292ae5ebda81
distances=0.6858726143836975
file=TwentyThousandLeaguesUnderTheSea.txt
keywords=nemo,captain,forest,evidently,proposed
Captain
Nemo ate at first without saying a word. Then he began—

“Sir, when I proposed to you to hunt in my submarine forest of Crespo,
you evidently thought me mad.
```

```text
id=f1704839-9080-421a-b144-dcffa52b1e25
distances=0.6898425817489624
file=TwentyThousandLeaguesUnderTheSea.txt
keywords=nemo,lieutenant,gestures,assurances,cool
For some minutes he was immovable, without taking his eye off the point
of observation. Then he lowered his glass and exchanged a few words
with his lieutenant. The latter seemed to be a victim to some emotion
that he tried in vain to repress. Captain Nemo, having more command
over himself, was cool. He seemed, too, to be making some objections to
which the lieutenant replied by formal assurances. At least I concluded
so by the difference of their tones and gestures.
```

```text
id=bb095e1e-c224-4e64-b1ba-f4b515cdf7ba
distances=0.7036728046393157
file=TwentyThousandLeaguesUnderTheSea.txt
keywords=nemo,hope,gulf,appeased,contemplation
I hope so. And I also hope that his powerful vessel has conquered the
sea at its most terrible gulf, and that the _Nautilus_ has survived
where so many other vessels have been lost! If it be so—if Captain Nemo
still inhabits the ocean, his adopted country, may hatred be appeased
in that savage heart! May the contemplation of so many wonders
extinguish for ever the spirit of vengeance!
```

```text
id=ee87a67f-665f-416d-b264-c100185c2ccf
distances=0.7243133187294006
file=TwentyThousandLeaguesUnderTheSea.txt
keywords=nemo,1868,continents,degree,bunting
Captain Nemo, on this 21st day of March, 1868, have reached the
South Pole on the ninetieth degree; and I take possession of this part
of the globe, equal to one-sixth of the known continents.”

“In whose name, Captain?”

“In my own, sir!”

Saying which, Captain Nemo unfurled a black banner, bearing an “N” in
gold quartered on its bunting.
```

```text
id=175be658-4cfb-4284-a443-7d2f81c0a0d3
distances=0.7395543456077576
file=TwentyThousandLeaguesUnderTheSea.txt
keywords=nemo,sorrowful,nautical,true,clusters
“Also,” he added, “true existence is there; and I can imagine the
foundations of nautical towns, clusters of submarine houses, which,
like the _Nautilus_, would ascend every morning to breathe at the
surface of the water, free towns, independent cities. Yet who knows
whether some despot——”

Captain Nemo finished his sentence with a violent gesture. Then,
addressing me as if to chase away some sorrowful thought:

“M.
```

```text
id=68a2b68e-bc89-4aa2-8128-d53c6975b493
distances=0.7410337924957275
file=TwentyThousandLeaguesUnderTheSea.txt
keywords=nemo,burying,coral,companions,tried
Captain
Nemo joined me. I rose and said to him:

“So, as I said he would, this man died in the night?”

“Yes, M. Aronnax.”

“And he rests now, near his companions, in the coral cemetery?”

“Yes, forgotten by all else, but not by us. We dug the grave, and the
polypi undertake to seal our dead for eternity.” And, burying his face
quickly in his hands, he tried in vain to suppress a sob.
```

```text
id=41dbc87f-db6d-42ef-9b63-825081b9b214
distances=0.7444064617156982
file=TwentyThousandLeaguesUnderTheSea.txt
keywords=nemo,captain,did,presentiment,altitude
If not, what did he feel? Remorse or regret? For a long while this
thought haunted my mind, and I had a kind of presentiment that before
long chance would betray the captain’s secrets.

The next day, the 1st of June, the _Nautilus_ continued the same
process. It was evidently seeking some particular spot in the ocean.
Captain Nemo took the sun’s altitude as he had done the day before. The
sea was beautiful, the sky clear.
```

```text
id=f288c8b3-435f-4334-9496-bb44c1b9fe4e
distances=0.7532105445861816
file=TwentyThousandLeaguesUnderTheSea.txt
keywords=nemo,noon,recollections,did,european
It seemed to be
seeking a spot it had some trouble in finding. At noon, Captain Nemo
himself came to work the ship’s log. He spoke no word to me, but seemed
gloomier than ever. What could sadden him thus? Was it his proxim ity
to European shores? Had he some recollections of his abandoned country?
If not, what did he feel? Remorse or regret?
```

| distance           |
|--------------------|
| 0.6432109274382903 |
| 0.6856973171234131 |
| 0.6858726143836975 |
| 0.6898425817489624 |
| 0.7036728046393157 |
| 0.7243133187294006 |
| 0.7395543456077576 |
| 0.7410337924957275 |
| 0.7444064617156982 |
| 0.7532105445861816 |

#### Test 1 Control

Same question, without filters on the keywords:

```text
id=029d4442-5336-4ab9-a1fe-181339d3c18b
distances=0.6432109274382903
file=TwentyThousandLeaguesUnderTheSea.txt
keywords=nemo,manuscript,waves,retaliations,tell
Does Captain Nemo still live? And does he still follow
under the ocean those frightful retaliations? Or, did he stop after the
last hecatomb?

Will the waves one day carry to him this manuscript containing the
history of his life? Shall I ever know the name of this man? Will the
missing vessel tell us by its nationality that of Captain Nemo?

I hope so.
```

```text
id=5aa46db9-2f5d-4769-85d1-53a26d63aa83
distances=0.6856973171234131
file=TwentyThousandLeaguesUnderTheSea.txt
keywords=nemo,pitiless,united,approaching,chimerical
One part of the mysterious existence of Captain Nemo had
been unveiled; and, if his identity had not been recognised, at least,
the nations united against him were no longer hunting a chimerical
creature, but a man who had vowed a deadly hatred against them. All the
formidable past rose before me. Instead of meeting friends on board the
approaching ship, we could only expect pitiless enemies. But the shot
rattled about us.
```

```text
id=be576052-173c-4124-92e1-292ae5ebda81
distances=0.6858726143836975
file=TwentyThousandLeaguesUnderTheSea.txt
keywords=nemo,captain,forest,evidently,proposed
Captain
Nemo ate at first without saying a word. Then he began—

“Sir, when I proposed to you to hunt in my submarine forest of Crespo,
you evidently thought me mad.
```

```text
id=f1704839-9080-421a-b144-dcffa52b1e25
distances=0.6898425817489624
file=TwentyThousandLeaguesUnderTheSea.txt
keywords=nemo,lieutenant,gestures,assurances,cool
For some minutes he was immovable, without taking his eye off the point
of observation. Then he lowered his glass and exchanged a few words
with his lieutenant. The latter seemed to be a victim to some emotion
that he tried in vain to repress. Captain Nemo, having more command
over himself, was cool. He seemed, too, to be making some objections to
which the lieutenant replied by formal assurances. At least I concluded
so by the difference of their tones and gestures.
```

```text
id=bb095e1e-c224-4e64-b1ba-f4b515cdf7ba
distances=0.7036728046393157
file=TwentyThousandLeaguesUnderTheSea.txt
keywords=nemo,hope,gulf,appeased,contemplation
I hope so. And I also hope that his powerful vessel has conquered the
sea at its most terrible gulf, and that the _Nautilus_ has survived
where so many other vessels have been lost! If it be so—if Captain Nemo
still inhabits the ocean, his adopted country, may hatred be appeased
in that savage heart! May the contemplation of so many wonders
extinguish for ever the spirit of vengeance!
```

```text
id=ee87a67f-665f-416d-b264-c100185c2ccf
distances=0.7243133187294006
file=TwentyThousandLeaguesUnderTheSea.txt
keywords=nemo,1868,continents,degree,bunting
Captain Nemo, on this 21st day of March, 1868, have reached the
South Pole on the ninetieth degree; and I take possession of this part
of the globe, equal to one-sixth of the known continents.”

“In whose name, Captain?”

“In my own, sir!”

Saying which, Captain Nemo unfurled a black banner, bearing an “N” in
gold quartered on its bunting.
```

```text
id=175be658-4cfb-4284-a443-7d2f81c0a0d3
distances=0.7395543456077576
file=TwentyThousandLeaguesUnderTheSea.txt
keywords=nemo,sorrowful,nautical,true,clusters
“Also,” he added, “true existence is there; and I can imagine the
foundations of nautical towns, clusters of submarine houses, which,
like the _Nautilus_, would ascend every morning to breathe at the
surface of the water, free towns, independent cities. Yet who knows
whether some despot——”

Captain Nemo finished his sentence with a violent gesture. Then,
addressing me as if to chase away some sorrowful thought:

“M.
```

```text
id=68a2b68e-bc89-4aa2-8128-d53c6975b493
distances=0.7410337924957275
file=TwentyThousandLeaguesUnderTheSea.txt
keywords=nemo,burying,coral,companions,tried
Captain
Nemo joined me. I rose and said to him:

“So, as I said he would, this man died in the night?”

“Yes, M. Aronnax.”

“And he rests now, near his companions, in the coral cemetery?”

“Yes, forgotten by all else, but not by us. We dug the grave, and the
polypi undertake to seal our dead for eternity.” And, burying his face
quickly in his hands, he tried in vain to suppress a sob.
```

```text
id=41dbc87f-db6d-42ef-9b63-825081b9b214
distances=0.7444064617156982
file=TwentyThousandLeaguesUnderTheSea.txt
keywords=nemo,captain,did,presentiment,altitude
If not, what did he feel? Remorse or regret? For a long while this
thought haunted my mind, and I had a kind of presentiment that before
long chance would betray the captain’s secrets.

The next day, the 1st of June, the _Nautilus_ continued the same
process. It was evidently seeking some particular spot in the ocean.
Captain Nemo took the sun’s altitude as he had done the day before. The
sea was beautiful, the sky clear.
```

```text
id=f288c8b3-435f-4334-9496-bb44c1b9fe4e
distances=0.7532105445861816
file=TwentyThousandLeaguesUnderTheSea.txt
keywords=nemo,noon,recollections,did,european
It seemed to be
seeking a spot it had some trouble in finding. At noon, Captain Nemo
himself came to work the ship’s log. He spoke no word to me, but seemed
gloomier than ever. What could sadden him thus? Was it his proxim ity
to European shores? Had he some recollections of his abandoned country?
If not, what did he feel? Remorse or regret?
```

The query returned exactly the same nodes.

## Test 2

Question `What type of bird is a parrot?`

Question keywords:
```text
('parrot', 0.7687)
('bird', 0.6413)
('type', 0.2809)
```

Result:

```text
id=00a8b578-a4be-4755-a276-ae85845bf588
distances=0.9824135899543762
file=TwentyThousandLeaguesUnderTheSea.txt
keywords=bird,shades,chestnut,comparatively,tips
It was the “large
emerald bird, the most rare kind.” It measured three feet in length.
Its head was comparatively small, its eyes placed near the opening of
the beak, and also small. But the shades of colour were beautiful,
having a yellow beak, brown feet and claws, nut-coloured wings with
purple tips, pale yellow at the back of the neck and head, and emerald
colour at the throat, chestnut on the breast and belly.
```

```text
id=f811d194-38be-4593-9616-c60b518ec796
distances=1.0501205921173096
file=TwentyThousandLeaguesUnderTheSea.txt
keywords=bird,gin,hardly,walk,conseil
See, friend Ned, see the monstrous
effects of intemperance!”

“By Jove!” exclaimed the Canadian, “because I have drunk gin for two
months, you must needs reproach me!”

However, I examined the curious bird. Conseil was right. The bird,
drunk with the juice, was quite powerless. It could not fly; it could
hardly walk.

This bird belonged to the most beautiful of the eight species that are
found in Papua and in the neighbouring islands.
```

```text
id=3aacf49b-3b6a-4609-88a9-2941b242a6c0
distances=1.1597737073898315
file=OnTheOriginOfSpeciesByMeansOfNaturalSelection.txt
keywords=bird,variability,innate,truly,gains
There may be truly said to be a constant struggle
going on between, on the one hand, the tendency to reversion to a less
modified state, as well as an innate tendency to further
variability of all kinds, and, on the other hand, the power of steady
selection to keep the breed true. In the long run selection gains the
day, and we do not expect to fail so far as to breed a bird as coarse
as a common tumbler from a good short-faced strain.
```

```text
id=080cb98f-ff7f-4e5e-a98e-65da70b8590a
distances=1.1785153150558472
file=TwentyThousandLeaguesUnderTheSea.txt
keywords=bird,natives,fineness,completed,prolonged
Two horned,
downy nets rose from below the tail, that prolonged the long light
feathers of admirable fineness, and they completed the whole of this
marvellous bird, that the natives have poetically named the “bird of
the sun.”

But if my wishes were satisfied by the possession of the bird of
paradise, the Canadian’s were not yet.
```

```text
id=8edcc304-164a-4d84-b3f6-4c118a875fac
distances=1.31316077709198
file=ParadiseLost.txt
keywords=bird,blandishment,whereof,bring,kinds
In sign whereof, each bird and beast behold
After their kinds; I bring them to receive
From thee their names, and pay thee fealty
With low subjection; understand the same
Of fish within their watery residence,
Not hither summoned, since they cannot change
Their element, to draw the thinner air.”
As thus he spake, each bird and beast behold
Approaching two and two; these cowering low
With blandishment; each bird stooped on his wing.
```

```text
id=62223982-281d-4f91-982d-154eada4d2f3
distances=1.528022050857544
file=TheRepublic.txt
keywords=immutable,bird,opinion,erring,region
Everything is and is not, as in the
old riddle—‘A man and not a man shot and did not shoot a bird and not a
bird with a stone and not a stone.’ The mind cannot be fixed on either
alternative; and these ambiguous, intermediate, erring, half-lighted
objects, which have a disorderly movement in the region between being
and not-being, are the proper matter of opinion, as the immutable
objects are the proper matter of knowledge.
```

```text
id=f6c07863-4a59-4143-a2a7-b00520296e41
distances=1.6390913724899292
file=OnTheOriginOfSpeciesByMeansOfNaturalSelection.txt
keywords=type,principle,independent,descent,cuvier
By
unity of type is meant that fundamental agreement in structure, which
we see in organic beings of the same class, and which is quite
independent of their habits of life. On my theory, unity of type is
explained by unity of descent. The expression of conditions of
existence, so often insisted on by the illustrious Cuvier, is fully
embraced by the principle of natural selection.
```

#### Test 2 Control

```text
id=5a93f36d-555b-45c1-b9ad-eee085eadc3d
distances=0.7196259498596191
file=TwentyThousandLeaguesUnderTheSea.txt
keywords=parrots,fork,agree,conseil,worth
“But they are eatable,” replied the harpooner.

“I do not agree with you, friend Ned, for I see only parrots there.”

“Friend Conseil,” said Ned, gravely, “the parrot is like pheasant to
those who have nothing else.”

“And,” I added, “this bird, suitably prepared, is worth knife and
fork.”

Indeed, under the thick foliage of this wood, a world of parrots were
flying from branch to branch, only needing a careful education to speak
the human language.
```

```text
id=b5e3ee33-ee32-444b-a034-6c579b4f388e
distances=0.8941778540611267
file=OnTheOriginOfSpeciesByMeansOfNaturalSelection.txt
keywords=birds,puffinuria,berardi,grebe,manner
yet it is a woodpecker which never climbs a
tree!

Petrels are the most aërial and oceanic of birds, yet in the quiet
Sounds of Tierra del Fuego, the Puffinuria
berardi, in its general habits, in its astonishing power of diving, its
manner of swimming, and of flying when unwillingly it takes flight,
would be mistaken by any one for an auk or grebe; nevertheless, it is
essentially a petrel, but with many parts of its organisation
profoundly modified.
```

```text
id=b2be36a5-ca81-423a-a14d-50dd978ecc10
distances=0.9195135831832886
file=OnTheOriginOfSpeciesByMeansOfNaturalSelection.txt
keywords=birds,productions,extraordinarily,differ,ranked
in pouters, fantails, runts,
barbs, dragons, carriers, and tumblers. Now some of these birds, when
mature, differ so extraordinarily in length and form of beak, that they
would, I cannot doubt, be ranked in distinct genera, had they been
natural productions.
```

```text
id=d742b9ff-dea4-462b-b266-fcfb24d35396
distances=0.9344061017036438
file=OnTheOriginOfSpeciesByMeansOfNaturalSelection.txt
keywords=pigeons,does,shown,disposition,degree
The shape and size of the eggs
vary. The manner of flight differs remarkably; as does in some breeds
the voice and disposition. Lastly, in certain breeds, the males and
females have come to differ to a slight degree from each other.

Altogether at least a score of pigeons might be chosen, which if shown
to an ornithologist, and he were told that they were wild birds, would
certainly, I think, be ranked by him as well-defined species.
```

```text
id=be4b7a00-7d01-4605-8f91-2888357927fa
distances=0.9434136152267456
file=OnTheOriginOfSpeciesByMeansOfNaturalSelection.txt
keywords=pigeons,rump,edged,occasional,externally
With pigeons, however, we have another case, namely, the occasional
appearance in all the breeds, of slaty-blue birds with two black bars
on the wings, a white
rump, a bar at the end of the tail, with the outer feathers externally
edged near their bases with white.
```

```text
id=714ceb3e-2359-48f4-b2ea-8dbdbc340c6d
distances=0.9563398957252502
file=OnTheOriginOfSpeciesByMeansOfNaturalSelection.txt
keywords=birds,memoir,american,gestures,supposed
There are twenty-six land birds, and
twenty-five of these are ranked by Mr. Gould as distinct species,
supposed to have been created here; yet the close affinity of most of
these birds to American species in every character, in their habits,
gestures, and tones of voice, was manifest. So it is with the other
animals, and with nearly all the plants, as shown by Dr. Hooker in his
admirable memoir on the Flora of this archipelago.
```

```text
id=102519fa-352a-464d-8490-566f57a29736
distances=0.9640275239944458
file=OnTheOriginOfSpeciesByMeansOfNaturalSelection.txt
keywords=ostrich,latitude,kinds,nearly,emeu
He hears from closely allied, yet distinct
kinds of birds, notes nearly similar, and sees their nests similarly
constructed, but not quite alike, with eggs coloured in nearly the same
manner. The plains near the Straits of Magellan are inhabited by one
species of Rhea (American ostrich), and northward the plains of La
Plata by another species of the same genus; and not by a true ostrich
or emeu, like those found in Africa and Australia under the same
latitude.
```

```text
id=9384f0d5-b27f-433d-9b76-edaf00a0fa4e
distances=0.9690279960632324
file=OnTheOriginOfSpeciesByMeansOfNaturalSelection.txt
keywords=peacock,eminently,confinement,preferences,know
Those who have closely attended to birds in
confinement well know that they often take individual preferences and
dislikes: thus Sir R. Heron has described how one pied peacock was
eminently attractive to all his hen birds.
```

```text
id=5ee5dc81-4197-41c3-9107-30e4ed0735e6
distances=0.971354603767395
file=OnTheOriginOfSpeciesByMeansOfNaturalSelection.txt
keywords=species,islets,madeira,entirely,ago
Many years ago, when comparing, and seeing others compare, the
birds from the separate islands of the Galapagos Archipelago, both one
with another, and with those from the American mainland, I was much
struck how entirely vague and arbitrary is the distinction between
species and varieties. On the islets of the little Madeira group there
are many insects which are characterized as varieties in Mr.
```

```text
id=73d98588-4520-4401-9cda-79ae506c33fb
distances=0.9795908331871033
file=OnTheOriginOfSpeciesByMeansOfNaturalSelection.txt
keywords=pigeons,analogous,aboriginal,pouter,normal
The most distinct breeds of pigeons, in countries most widely
apart, present sub-varieties with reversed feathers on the head and
feathers on the feet,—characters not possessed by the aboriginal
rock-pigeon; these then are analogous variations in two or more
distinct races. The frequent presence of fourteen or even sixteen
tail-feathers in the pouter, may be considered as a variation
representing the normal structure of another race, the fantail.
```

#### Result

With keywords:

| distance           |
|--------------------|
| 0.9824135899543762 |
| 1.0501205921173096 |
| 1.1597737073898315 |
| 1.1785153150558472 |
| 1.31316077709198   |
| 1.528022050857544  |
| 1.6390913724899292 |

Without keywords:

| distance           |
|--------------------|
| 0.7196259498596191 |
| 0.8941778540611267 |
| 0.9195135831832886 |
| 0.9344061017036438 |
| 0.9434136152267456 |
| 0.9563398957252502 |
| 0.9640275239944458 |
| 0.9690279960632324 |
| 0.971354603767395  |
| 0.9795908331871033 |

Keywords are an effective strategy to filter the results.