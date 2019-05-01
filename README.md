# Question Answering In Context
Question Answering (QA) has long been a promising yet challenging task, and a large number of work has been done in this area. However, simple QA tasks such as extracting answer spans from a given text have been criticized as "shallow pattern recognition", which does not equip machines with the capability of reading. Recently, Conversational Question Answering has been proposed to address this issue. In this task, a program needs to not only answer questions, but also answer them in a conversational style.

In this project, we are going to use deep neural networks to address QuAC[1], one of these Conversational QA datasets. We are going to train existing models on QuAC and compare their pros and cons. We will also use models effective on other related datasets and invent new models involving different network architectures or mechanisms. We hope that we could obtain a better, and even state-of-the-art performance.

## QuAC
<p align="center">
    <img src="figure/task.png" width="400"/>
    <br></br>
    Figure 1: Task setup of QuAC.
</p>

Question Answering in Context(QuAC)[1] is a newly proposed dataset with regards to conversational QA. The task is to answer a question in a conversation given a context and historical questions and answers in the conversation. Compared with the former ones, its questions are often highly context-dependent, elliptical, and even unanswerable.

<p align="center">
    <img src="figure/quac.png" width="400"/>
    <br></br>
    Figure 2: Baseline QA Model for QuAC.
</p>
## Approaches and Results
### FlowQA

#### [FlowQA + Attention](FlowQA_Attention)

#### [FlowQA + Coreference](FlowQA_Coreference)

### [SD-Net](SDNet)

### [BiDAF++](BiDAF)


## Conclusion
* **FlowQA+Attention**: adding attention layers over ﬂow operation layer slightly improves the FlowQA model. We believe that it is because the representations generated in this way focus more on recent dialogs and help resolve coreferences.

* **FlowQA+Coreferece**: Adding vector representation that encodes the coreference in long context can increase the performance of the model for task involving complex dependencies (context and dialogue)

* **Enhancing BiDAF++**: Replacing Glove embedding with ELMO and BERT embedding for input embedding layers. Because elmo extracts context features from language model and BERT uses pre-trained model which could perform better than Glove on QuAC dataset, these two embeddings could enhance the model performance.

* **SDNet**: SDnet is not originally applied on QuAC dataset. So we adjusted the format of dataset so it can be ﬁtted on SDNet. However the result is not as good as we expected. We can try to ﬁgure out issues and improve this model in future.

