# FlowQA + Coreference

We used the [coreference model](https://github.com/kentonl/e2e-coref) proposed by Lee et all. 
In short, this model clusters spans in text that coreference among other.
For example, let's consider below conversation;

A: What is the story about?

B: young girl and her dog 

A: What were they doing?

B: set out a trip

In this conversation, the phrase "young girl and her dog" said by A refers to "they" said by B.
Also, the pronoun "her" said by A refers to "young girl" which appears earlier.
Therefore, the model will cluster the following spans;

[["young girl", "her"], ["young girl and her dog", "they"]]


In order to feed this coreference information to the FlowQA model, we can

* Feed the result from the coreference model to the FlowQA model
* Feed the internal representation of each tokens in coreference model to the FlowQA model
