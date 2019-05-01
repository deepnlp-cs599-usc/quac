import json
f=open('train_v0.2.json','r')
quacdata=json.load(f)
data=[]
for i in range(len(quacdata['data'])):
  temp={}
  temp["source"]="wikipedia"
  temp["filename"]=quacdata['data'][i]["title"]+".txt"
  temp["name"]=temp["filename"]
  temp["id"]=quacdata['data'][i]["paragraphs"][0]["id"]
  temp["story"]=quacdata['data'][i]["paragraphs"][0]["context"][:-13]
  temp["questions"]=[]
  temp["answers"]=[]
  turn=0
  for qa in quacdata['data'][i]["paragraphs"][0]["qas"]:
    turn+=1
    tempq={}
    tempa={}
    tempq["turn_id"]=turn
    tempq["input_text"]=qa["question"]
    temp["questions"].append(tempq)
    tempa["span_start"]=qa["orig_answer"]["answer_start"]
    tempa["span_end"]=qa["orig_answer"]["answer_start"]+len(qa["orig_answer"]["text"])
    answertext=qa["orig_answer"]["text"]
    if answertext=="CANNOTANSWER":
      answertext="unknown"
      tempa["span_start"]=-1
      tempa["span_end"]=-1
    tempa["span_text"]=answertext
    if qa["yesno"]=="y":
      tempa["input_text"]="Yes"
    elif qa["yesno"]=="n":
      tempa["input_text"]="No"
    else:
      tempa["input_text"]=answertext
    tempa["turn_id"]=turn
    temp["answers"].append(tempa)
  data.append(temp)
output={}
output["data"]=data
output["version"]="1.0"
outf=open('quac_train_processed.json','w')
json.dump(output, outf ,indent=2 )
outf.close()
f.close()

f=open('val_v0.2.json','r')
quacdata=json.load(f)
data=[]
for i in range(len(quacdata['data'])):
  temp={}
  temp["source"]="wikipedia"
  temp["filename"]=quacdata['data'][i]["title"]+".txt"
  temp["name"]=temp["filename"]
  temp["id"]=quacdata['data'][i]["paragraphs"][0]["id"]
  temp["story"]=quacdata['data'][i]["paragraphs"][0]["context"][:-13]
  temp["questions"]=[]
  temp["answers"]=[]
  turn=0
  for qa in quacdata['data'][i]["paragraphs"][0]["qas"]:
    turn+=1
    tempq={}
    tempa={}
    tempq["turn_id"]=turn
    tempq["input_text"]=qa["question"]
    temp["questions"].append(tempq)
    tempa["span_start"]=qa["orig_answer"]["answer_start"]
    tempa["span_end"]=qa["orig_answer"]["answer_start"]+len(qa["orig_answer"]["text"])
    answertext=qa["orig_answer"]["text"]
    if answertext=="CANNOTANSWER":
      answertext="unknown"
      tempa["span_start"]=-1
      tempa["span_end"]=-1
    tempa["span_text"]=answertext
    if qa["yesno"]=="y":
      tempa["input_text"]="Yes"
    elif qa["yesno"]=="n":
      tempa["input_text"]="No"
    else:
      tempa["input_text"]=answertext
    tempa["turn_id"]=turn
    temp["answers"].append(tempa)
  data.append(temp)
output={}
output["data"]=data
output["version"]="1.0"
outf=open('quac_val_processed.json','w')
json.dump(output, outf ,indent=2 )
outf.close()
f.close()
