import json
import requests
import re
import threading
import random
threading_dict_list = []
def A(i, j):
    global threading_dict_list
    dict_list = threading_dict_list[i]
    url = 'https://www.dictionarysearch.org/chengyu/'
    headers = {
        'user-agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36 Edg/108.0.1462.42'
    }
    params = {

    }
    for idx, word_dict in enumerate(dict_list):
        word = word_dict['word']
        print(str(idx) + '/' + str(len(dict_list)))
        true_url = url + word
        try_count = 0
        while try_count <= 10:
            try:    
                response = requests.get(url=true_url, params=params, headers=headers, timeout=15)
                response_text_list = response.text.split('\n')
                for line in response_text_list:
                    if word + ' 的出处' in line and '' == word_dict['source']:
                        r_pattern = re.compile(r'<br />([^<>]+)</div>')
                        source = r_pattern.findall(line)
                        word_dict['source'] = source[0]
                    if word + ' 的例句' in line:
                        after_line = line.replace('<strong>' + word + '</strong>', '~')
                        r_pattern = re.compile(r'<br />([^<>]+)</div>')
                        example = r_pattern.findall(after_line)
                        if word_dict['example'] != '':
                            word_dict['example'] = [word_dict['example']]
                        else:
                            word_dict['example'] = []
                        word_dict['example'].extend(example)
                break
            except:
                try_count += 1
if __name__ == '__main__':
    dict_list = []
    with open(file='fake_sentence.txt', mode='r', encoding='utf-8') as fr:
        for line in fr:
            dict_list.append(json.loads(line.strip()))
    threading_num = 20
    for i in range(threading_num):
        threading_dict_list.append([])
    for word_dict in dict_list:
        idx = random.randint(0, threading_num - 1)
        threading_dict_list[idx].append(word_dict)

    threading_list = []
    for i in range(threading_num):
        threading_list.append(threading.Thread(target=A, args=(i, i)))
        threading_list[-1].start()

    for i in range(threading_num):
        threading_list[i].join()
    another_list = []
    for dict_list in threading_dict_list:
        another_list.extend(dict_list)
    with open(file='fake_sentence2.txt', mode='w', encoding='utf-8') as save:
        for word_dict in another_list:
            save.write(json.dumps(word_dict, ensure_ascii=False) + '\n')