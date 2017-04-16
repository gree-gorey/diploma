# Report

**Disclaimer!** Accuracy percantages here is lower than the real accuracy due to the alignment problems for the test set. These values are here to show dynamics.

## I. Accuracy ~ size of gold standard input

LM *size* is fixed: 4,880,838 words.<br>
LM *type* is fixed: both spoken + written language corpora.

### Table 1. Accuracy ~ size of gold standard input

| clause count | word count | train time | acc          | acc spellcheck | lemma acc    | 
|--------------|------------|------------|--------------|----------------|--------------| 
| 10           | 34         | 00:00:13   | 24.9         | 50.6           | 53           | 
| 25           | 81         | 00:00:15   | 59.8         | 69.2           | 75.8         | 
| 30           | 102        | 00:00:16   | 65.4         | 73             | 78.8         | 
| 50           | 163        | 00:00:18   | 67.5         | 73.5           | 78.6         | 
| 100          | 299        | 00:00:19   | 71.4         | 77.1           | 82.5         | 
| 300          | 1004       |  00:00:40  | 79.7         | 81.9           | 85.8         | 
| 500          | 1641       | 00:00:45   | 79.1         | 82.1           | 87.1         | 
| 1000         | 3330       | 00:05:37   | 83.3         | 84.5           | 88.5         | 
| 1500         | 4836       | 00:03:11   | 81.9         | 84.5           | 87.2         | 
| 2000         | 6561       | 00:04:41   | 83.6         | 85.3           | 88.9         | 
| 2500         | 8314       | 00:09:45   | 84.5         | 85.4           | 88.6         | 
| 3000         | 9950       | 00:18:11   | 84.1         | 85             | 88.5         | 
| 3500         | 11919      | 00:10:27   | 83.3         | 84.2           | 88.2         | 
| 4035         | 13767      | 00:11:15   | 83.6 **(84.8&ast;)** | 84.5 **(85.8&ast;)**   | 88.2 **(89.6&ast;)** | 

**&ast; after manual alignment.**

### Figure 1. Accuracy ~ size of gold standard input

![acc_dynamics](https://raw.githubusercontent.com/gree-gorey/diploma/master/static/acc_dynamics.png "acc_dynamics")

## II. Accuracy ~ type of language model

Gold standard size is fixed: 13767 words.

### Table 2. Accuracy ~ type of language model

| LM type | LM word count | training time | acc  | acc speellcheck | lemma acc | 
|---------|---------------|---------------|------|-----------------|-----------| 
| written | 1535861       | 00:22:40      | 82.1 | 82.9            | 87.2      | 
| spoken  | 1535861       | 00:13:27      | 80.9 | 81.7            | 85.9      | 
| both    | 6381702       | 00:18:54      | 82.2 | 84              | 88.2      | 

### Table 3. Chi square: type of LM

Calculated for spellchecked words.

| type    | true | false | 
|---------|------|-------| 
| written | 697  | 147   | 
| spoken  | 700  | 144   | 

```
	Pearson's Chi-squared test with Yates' continuity correction

X-squared = 0.016609, df = 1, p-value = 0.8975
```

## III. Accuracy ~ size of language model

Gold standard size is fixed: 13767 words.<br>
LM *type* is fixed: both spoken + written language corpora.

### Table 4. Accuracy ~ size of language model

| clause count | word count | train time | acc  | acc spellcheck | lemma acc |
| ------------ | ---------- | ---------- | ---- | -------------- | --------- |
| 4035         | 13767      | 00:11:15   | 83.6 | 84.5           | 88.2      |

### Figure 2. Accuracy ~ size of language model

## IV. Quality error ...