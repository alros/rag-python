# Using FAISS

Index created with `def use_indexes`: it creates the folder `storage` in the test's folder.

Run `query` to get a response from FAISS.

Result:
```text
id=ac77835b-9079-4a05-9e57-9e943f53e030 TwentyThousandLeaguesUnderTheSea.txt

...684 long chunk...

id=eb9bc3ce-59e5-4775-9de9-006e54ad60a4 TwentyThousandLeaguesUnderTheSea.txt

...671 long chunk...
```

Run `retrieve_only` to get the list retrieved nodes.

Result:
```text
0 id=ac77835b-9079-4a05-9e57-9e943f53e030 TwentyThousandLeaguesUnderTheSea.txt 0.30805692076683044
1 id=eb9bc3ce-59e5-4775-9de9-006e54ad60a4 TwentyThousandLeaguesUnderTheSea.txt 0.30830368399620056
2 id=1db18fa8-e642-46d4-98cd-88c84a406c67 TwentyThousandLeaguesUnderTheSea.txt 0.30866241455078125
3 id=8444e0a2-d253-48d8-b1e5-a75dfd7af448 TwentyThousandLeaguesUnderTheSea.txt 0.31451624631881714
4 id=6d98d1ae-9f8f-479a-a3a6-f842f57e31a1 TwentyThousandLeaguesUnderTheSea.txt 0.3237929344177246
```

Increasing `similarity_top_k` proves that also nodes from different books can be retrieved:

```text
...
150 id=c3fdc0f1-2eb1-49ca-832f-29ed4cc64955 TheRepubblic.txt 0.48570042848587036
...
```