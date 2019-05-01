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
* Feed the internal representation of each tokens in coreference model to the FlowQA model.

We concatenate these two new representation with the existing input of FlowQA, which consists of word embeddings, part of speech and named entity.

## Feed the result from the coreference model 

We use one hot encoding to represent the results from coreference model. 
Each token will be coresponding to a vector of which the length is the number of clusters.
If a token belong to an ith cluster, the element ith in one hot vector will be 1.
Here is the one hot encoding for above example.

"young" [1, 1]
"girl" [1, 1]
"and" [0 ,1]
"her" [1, 1]
"dog" [1, 1]
"What" [0, 0]
"were" [0, 0]
"they" [0, 1]
"doing" [0, 0]

## Feed the internal representation 

We use the latent representation from the coreference model as an input of FlowQA model. To be precise, we use X* from the figure 3 of [this paper](https://arxiv.org/abs/1707.07045). Since the model predicts the coreference, we hypothesize that the latent representation of the model will encode the coreference as well.

# Result

![alt text](figure/coref-F1)
