# Question Answering In Context
Question Answering (QA) has long been a promising yet challenging task, and a large number of work has been done in this area. However, simple QA tasks such as extracting answer spans from a given text have been criticized as "shallow pattern recognition", which does not equip machines with the capability of reading. Recently, Conversational Question Answering has been proposed to address this issue. In this task, a program needs to not only answer questions, but also answer them in a conversational style.

In this project, we are going to use deep neural networks to address QuAC[1], one of these Conversational QA datasets. We are going to train existing models on QuAC and compare their pros and cons. We will also use models effective on other related datasets and invent new models involving different network architectures or mechanisms. We hope that we could obtain a better, and even state-of-the-art performance.

## QuAC
Question Answering in Context(QuAC)[1] is a newly proposed dataset with regards to conversational QA. The task is to answer a question in a conversation given a context and historical questions and answers in the conversation. Compared with the former ones, its questions are often highly context-dependent, elliptical, and even unanswerable.

<p align="center">
    <img src="figure/quac.png" width="400"/>
</p>
## Approaches and Results

### FlowQA

#### [FlowQA + Attention](FlowQA_Attention)

#### [FlowQA + Coreference](FlowQA_Coreference)

### [SD-Net](SDNet)

### [BiDAF++](BiDAF)


## Conclusion
