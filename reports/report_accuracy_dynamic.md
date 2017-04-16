# Report

**Disclaimer!** Accuracy percantages here is lower than the real accuracy due to the alignment problems for the test set. These values are here to show dynamics.

## I. Accuracy ~ size of gold standard input

LM *size* is fixed: 4,880,838 words.<br>
LM *type* is fixed: both spoken + written language corpora.

### Table 1. Accuracy ~ size of gold standard input

| clause count | word count | train time | acc          | acc spellcheck | lemma acc    | 
|--------------|------------|------------|--------------|----------------|--------------| 
| 10           | 34         | 00:00:13   | 24.4         | 49.5           | 51.9         | 
| 25           | 81         | 00:00:15   | 58.9         | 68.1           | 74.6         | 
| 30           | 102        | 00:00:16   | 64.1         | 71.5           | 77.2         | 
| 50           | 163        | 00:00:18   | 66.4         | 72.3           | 77.3         | 
| 100          | 299        | 00:00:19   | 70           | 75.5           | 80.7         | 
| 500          | 1641       | 00:00:45   | 77.9         | 80.9           | 85.8         | 
| 1000         | 3330       | 00:05:37   | 82           | 83.2           | 87.2         | 
| 1500         | 4836       | 00:03:11   | 80.5         | 83.1           | 85.8         | 
| 2000         | 6561       | 00:04:41   | 82.5         | 84.1           | 87.6         | 
| 2500         | 8314       | 00:09:45   | 83.1         | 84             | 87.2         | 
| 3000         | 9950       | 00:18:11   | 82.8         | 83.7           | 87.2         | 
| 3500         | 11919      | 00:10:27   | 82.1         | 83.1           | 86.9         | 
| 4035         | 13767      | 00:11:15   | 82.5 **(84.8&ast;)** | 83.3 **(85.8&ast;)**   | 86.9 **(89.6&ast;)** | 


### Figure 1. Accuracy ~ size of gold standard input

### Quality error ...



## II. Accuracy ~ type of language model

...

## III. Accuracy ~ size of language model