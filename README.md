# Question Answering In Context
Question Answering (QA) has long been a promising yet challenging task, and a large number of work has been done in this area. However, simple QA tasks such as extracting answer spans from a given text have been criticized as "shallow pattern recognition", which does not equip machines with the capability of reading. Recently, Conversational Question Answering has been proposed to address this issue. In this task, a program needs to not only answer questions, but also answer them in a conversational style.

In this project, we are going to use deep neural networks to address QuAC[1], one of these Conversational QA datasets. We are going to train existing models on QuAC and compare their pros and cons. We will also use models effective on other related datasets and invent new models involving different network architectures or mechanisms. We hope that we could obtain a better, and even state-of-the-art performance.

## [QuAC](http://quac.ai)
<p align="center">
    <img src="figure/task.png" width="400"/>
    <br></br>
    Figure 1: Task setup of QuAC.
</p>

[Question Answering in Context(QuAC)](https://quac.ai/) is a newly proposed dataset with regards to conversational QA. The task is to answer a question in a conversation given a context and historical questions and answers in the conversation. Compared with the former ones, its questions are often highly context-dependent, elliptical, and even unanswerable. The architecture o typical QA models for QuAC:

<p align="center">
    <img src="figure/quac.png" width="400"/>
    <br></br>
    Figure 2: Baseline QA Model for QuAC.
</p>

## Approaches and Results
### FlowQA

## What do we try to improve

FlowQA has been shown to have a considerable good performance on conversational question-answering tasks such as CoQA and QuAC. Firstly, we re-run the FlowQA model and investigate why it has great performance and why it is special. 

Why does FlowQA work? We believe that it is because of its "flow" operation, which uses a LSTM (or GRU) to represent context words in terms of question turns. By using "flow" operation, FlowQA could capture and retain conversational information. Since
conversations are in fact sequences, it is a natural, yet smart, idea, to encode conversational information in this way.

![image](https://github.com/deepnlp-cs599-usc/quac/blob/master/FlowQA_Attention/figure/Vanilla%20Flow%20Operation.png)

#### [FlowQA + Attention](FlowQA_Attention)

#### [FlowQA + Coreference](FlowQA_Coreference)

### [SD-Net](SDNet)
A contextualized attention-based deep neural network developed by Microsoft. It is originally evaluated on another question answering dataset CoQA, and it is the first model that reaches in-domain F1 score higher than 80% (80.7%) on CoQA. Here we are applying this model on QuAC dataset. Since the format of two datasets are different, we need to preprocess data carefully.

### [BiDAF++](BiDAF)
An original BiDAF++ model uses Char-CNN for character embedding and GLoVe for word embedding. It is also equipped with contextualized embeddings and self attention. In this model, marker embeddings corresponding to previous answer words are used, while question turn numbers are encoded into question embeddings. We intend to append ELMo or BERT embedding to word embeddings and contextualized embeddings to get better performance.

## Conclusion
* **FlowQA+Attention**: adding attention layers over ﬂow operation layer slightly improves the FlowQA model. We believe that it is because the representations generated in this way focus more on recent dialogs and help resolve coreferences.

* **FlowQA+Coreferece**: Adding vector representation that encodes the coreference in long context can increase the performance of the model for task involving complex dependencies (context and dialogue)

* **Enhancing BiDAF++**: Appending ELMo or BERT embedding to word embeddings and contextualized embeddings. Because ELMo extracts context features from language model and BERT uses pre-trained model which could perform better than GLoVe on QuAC dataset, these two embeddings could enhance the model performance.

* **SDNet**: SDnet is not originally applied on QuAC dataset. So we adjusted the format of dataset so it can be ﬁtted on SDNet. However the result is not as good as we expected. We can try to ﬁgure out issues and improve this model in future.

