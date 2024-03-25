import requests
import re
import json
import threading
import random

file1 = open(file='chengyu.txt', mode='r', encoding='utf-8')
file2 = open(file='sentence.txt', mode='w', encoding='utf-8')

threading_num = 40
threading_word_list = []
for i in range(threading_num):
    threading_word_list.append([])
for line in file1.readlines():
    word = line.strip()
    idx = random.randint(0, threading_num - 1)
    threading_word_list[idx].append(word)
file_list = []
for i in range(threading_num):
    file_list.append(open(file='sentenceXX' + str(i + 1) + '.txt', mode='w', encoding='utf-8'))

def run(word_list : list, this_file):
    for word in word_list:
        url = "https://dict.baidu.com/s"
        keys = {
            'wd' : word,
            'from' : 'zici'
        }
        headers = {
            'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36 Edg/108.0.1462.42'
        }
        p = None
        for i in range(4):
            try:
                req = requests.get(url=url, params=keys, headers=headers, timeout=3)
                p = 1
                break
            except:
                continue
        if p is None:
            continue
        web_content = req.text
        filter_content = ''
        for ch in web_content:
            if ch != ' ' and ch != '\t' and ch != '\n':
                filter_content += ch
        chuchu_pattern = re.compile(r'<label>近义词</label><divclass="block">(<ahref="\?wd=[^&><]+&cf=synant&ptype=zici">[^&><]+</a>)+')
        chuchu_sentence = chuchu_pattern.findall(filter_content)
        for idx, jinyi in enumerate(chuchu_sentence):
            pattern = re.compile(r'<ahref="\?wd=[^&]+&cf=synant&ptype=zici">([^<>]+)</a>')
            chuchu_sentence[idx] = pattern.findall(jinyi)[0]

        liju_pattern = re.compile(r'<label>反义词</label><divclass="block">(<ahref="\?wd=[^&><]+&cf=synant&ptype=zici">[^&><]+</a>)+')
        liju_sentence = liju_pattern.findall(filter_content)
        for idx, fanyi in enumerate(liju_sentence):
            pattern = re.compile(r'<ahref="\?wd=[^&]+&cf=synant&ptype=zici">([^<>]+)</a>')
            liju_sentence[idx] = pattern.findall(fanyi)[0]
        this_file.write(json.dumps({
            'word' : word,
            '近义词' : chuchu_sentence,
            '反义词' : liju_sentence
        }, ensure_ascii=False) + '\n')
thr_list = []
for i in range(threading_num):
    thr_list.append(threading.Thread(target=run, args=(threading_word_list[i], file_list[i])))
    thr_list[-1].start()
for i in range(threading_num):
    thr_list[i].join()
for val in file_list:
    val.close()
file1.close()
file2.close()