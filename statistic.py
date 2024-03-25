import json
count = 1

dict_sentence = dict()

with open(file='common_set_sentences.txt', mode='r', encoding='utf-8') as fr1:
    for line in fr1:
        _dict = json.loads(line)
        dict_sentence[_dict['word']] = _dict['sentence_list']
    
with open(file='temp.txt', mode='r', encoding='utf-8') as fr1:
    with open(file='temp2.txt', mode='w', encoding='utf-8') as fw:
        for line in fr1: 
            _dict = json.loads(line)
            if _dict['word'] in _dict.keys():
                continue
            fw.write(line)