# num = 1
# _set = set()
# file1 = open(file='sentence.txt', mode='w', encoding='utf-8')
# while num <= 40:
#     file2 = open(file='sentenceXX' + str(num) + '.txt', mode='r', encoding='utf-8')
#     for line in file2.readlines():
#         _set.add(line)
#     file2.close()
#     num += 1
# for item in _set:
#     file1.write(item)
# file1.close()
import json
sentence_list = []
sentence_dict = dict()
jin_fan_dict = dict()
with open(file='sentence.txt', mode='r', encoding='utf-8') as fr:
    for line in fr:
        sentence = line.strip()
        sentence_list.append(json.loads(sentence))
        sentence_dict[sentence_list[-1]['word']] = sentence_list[-1]['example']
with open(file='jin_fan.txt', mode='r', encoding='utf-8') as fr:
    for line in fr:
        jsonified_dict = json.loads(line.strip())
        jin_fan_dict[jsonified_dict['word']] = {
            "jin_yi" : jsonified_dict['近义词'],
            "fan_yi" : jsonified_dict['反义词']
        }
for s in sentence_list:
    s['近义词造句'] = []
    s['反义词造句'] = []
    _dict = jin_fan_dict.get(s['word'], None)
    if _dict:
        jin_yi_list = jin_fan_dict[s['word']]['jin_yi']
        fan_yi_list = jin_fan_dict[s['word']]['fan_yi']
        for jin_yi in jin_yi_list:
            sentence = sentence_dict.get(jin_yi, '')
            s['近义词造句'].append(sentence)
        for fan_yi in fan_yi_list:
            sentence = sentence_dict.get(fan_yi, '')
            s['反义词造句'].append(sentence)

with open(file='save.txt', mode='w', encoding='utf-8') as save:
    for s in sentence_list:
        save.write(json.dumps(s, ensure_ascii=False) + '\n')