# FlowQA + Attention Over Flow



## How we improve FlowQA -- Adding Self-attention

However, we have noticed that in the "flow" operation, no attention mechanism is used. We believe that applying attention here should be considered, because not every historical conversation is important. When new questions are posted, it is highly likely that only several previous questions are involved, instead of all. By adding attention in the "flow" operation, we could align new representations with previous useful ones. We would like to call it "attention-over-flow".

![image](https://github.com/deepnlp-cs599-usc/quac/blob/master/FlowQA_Attention/figure/Attention%20Over%20Flow.png)


## Experiments

We conducted experiments on Google Cloud, using a 2-CPU, 1 Tesla K80 GPU with 11 GB GPU memory and 60 GB disk memory. We use python 3.6.8 and pytorch 1.0.1. The batch size is set to be 2. 

How to run the code is the same as FlowQA. However, using "attention over flow" is set to be default.

From https://github.com/momohuang/FlowQA we borrow their instructions as follows

Step 1:
perform the following:

> pip install -r requirements.txt

to install all dependent python packages.

Step 2:
download necessary files using:

> ./download.sh

Step 3:
preprocess the data files using:

> python preprocess_QuAC.py

Step 4:
run the training code using:

> python train_QuAC.py

To specify not using "attention over flow", run:

> python train_QuAC.py --flow_attention=0


## Results

The result shows that our attempt slightly improves FlowQA by 0.1 of F-1 value on dev set. We would like to mention that the model converges much faster, as only 10 epochs is used instead of 20.

![image](https://github.com/deepnlp-cs599-usc/quac/blob/master/FlowQA_Attention/figure/result.png)


## References

[Flowqa: Grasping flow in history for conversational machine comprehensionn.](https://arxiv.org/abs/1810.06683) By Huang H Y, Choi E, Yih W.

[Quac: Question answering in context.](https://arxiv.org/abs/1808.07036) By Choi E, He H, Iyyer M, et al. 








