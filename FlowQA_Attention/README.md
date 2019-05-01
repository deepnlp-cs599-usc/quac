# What do we try to improve

FlowQA has been shown to have a considerable good performance on conversational question-answering tasks such as CoQA and QuAC. Firstly, we re-run the FlowQA model and investigate why it has great performance and why it is special. 

Why does FlowQA work? We believe that it is because of its "flow" operation, which uses a LSTM (or GRU) to represent context words in terms of question turns. By using "flow" operation, FlowQA could capture and retain conversational information. Since
conversations are in fact sequences, it is a natural, yet smart, idea, to encode conversational information in this way.

# How we improve FlowQA

However, we have noticed that in the "flow" operation, no attention mechanism is used. We believe that applying attention here should be considered, because not every historical conversation is important. When new questions are posted, it is highly likely that only several previous questions are involved, instead of all. By adding attention in the "flow" operation, we could align new representations with previous useful ones. We would like to call it "attention-over-flow".

# Technical detail

We would describe how we modified the "flow" operation in detail.


# Results

The result shows that our attempt slightly improves FlowQA by 0.1 of F-1 value. We would like to mention that the model converges much faster, as only 10 epochs is used instead of 20.

# Experiments



