# FlowQA + Coreference

We used the [coreference model](https://github.com/kentonl/e2e-coref) proposed by Lee et all to improve the [FlowQA](https://github.com/momohuang/FlowQA) model. 
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

# Experiment

First, we set up the Coreference Model according to [instruction](https://github.com/kentonl/e2e-coref). 
Then we use their pre-trained coreference model to predict the coreference of QuAC data set.
We extract the latent representation of each token and save them. 
After that, we convert the result of the coreference model to one hot encoding.
Finally, we concatenate them with one hot encoding to obtain the augmented input vector that will be used to input FlowQA.
The augmented vector' size is 450 which consists of 400 for X* latent representation and 50 for one hot encoding.

Second, we set up the FlowQA model according to the [instruction](https://github.com/momohuang/FlowQA). 
We have to modify ```train_QuAC.py```, ```general_utils.py``` and ```detail_model.py``` to support the augmented representation. 
Then we train the model with this new input representation.


We use [Google Cloud Platform](https://cloud.google.com/) with 4 vCPUs, 26 GB memory and 1 x NVIDIA Tesla K80 to run both FlowQA and Coreference models. 
It takes around 50 hour to predict the coreference for entire QuAC dataset and takes around 4 hour per epoch to train FlowQA model


# Result

Below is the comparison of F1 between the original FlowQA model and our modification. We can see that the improved model perform slightly better.

![ ](/figure/coref-F1.png)
