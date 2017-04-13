# Report

## I. Accuracy ~ size of gold standard input

**Disclaimer!** Accuracy percantages here is lower than the real accuracy due to the alignment problems for the test set. These values are here to show dynamics.<br>

LM size is fixed: 89090 words.<br>
LM type is fixed: both spoken + written language corpora.

### Table 1. Accuracy ~ size of gold standard input

| clause count | word count | training time | acc  | acc (spellcheck) | real acc |
| ------------ | ---------- | ------------- | ---- | ---------------- | -------- |
| 10           | 34         | 00:00:17      | 24.0 | 48.8             |          |
| 25           | 81         |               |      |                  |          |
| 30           | 102        |               |      |                  |          |
| 50           | 163        |               |      |                  |          |
| 100          | 299        |               |      |                  |          |
| 500          | 1641       |               |      |                  |          |
| 1000         | 3330       |               |      |                  |          |
| 1500         | 4836       |               |      |                  |          |
| 2000         | 6561       |               |      |                  |          |
| 2500         | 8314       |               |      |                  |          |
| 3000         | 9950       | 00:18:11      | 81.3 | 82.1             | 96.7     |
| 3500         |            |               |      |                  |          |
| 4092         |            |               |      |                  |          |

### Figure 1. Accuracy ~ size of gold standard input

### Quality error ...



## II. Accuracy ~ type of language model

...

## III. Accuracy ~ size of language model