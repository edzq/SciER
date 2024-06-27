import json
import os
from data_structures import Dataset

def load_jsonl(jsonl_path:str) -> list:
    data = []
    with open(jsonl_path) as f:
        for line in f:
            data.append(json.loads(line))
    return data




dataset = load_jsonl('/home/tuo96248/projects/LLM4NLP/datasets/scired/test_sent_llm.jsonl')
sent = dataset[0]
print(sent.keys())
print(sent['sentence'])
print('----------------')
print(sent['ner'])
print('----------------')
print(sent['rel'])
print('----------------')
print(sent['rel_plus'])



# ========= usage example for Dataset class when using supervised methods
# dev_path = './SciER/dev.jsonl'
# dataset = Dataset(dev_path)
# for c, doc in enumerate(dataset):
#     for i, sent in enumerate(doc):
#         print(sent.text) # list of tokens of one sentence
#         print(sent.ner) # list of NERs in the sentence
#         exit()