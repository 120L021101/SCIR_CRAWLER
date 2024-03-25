import requests
import json
import re

def req(word : str):
    url = 'https://zaojv.com/wordQueryDo.php'
    datas = {
        'nsid' : 0,
        's': 4595742426291063331,
        'q':'',
        'wo':word,
        'directGo':1
    }
    headers = {
        'Accept' : 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'Accept-Encoding' : 'gzip, deflate, br',
        'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36 Edg/108.0.1462.42'
    }
    response = requests.post(url, datas,headers=headers)
    line_list = response.text.split('\n')
    for idx, line in enumerate(line_list):
        if 'student' in line:
            idx += 2
            line = line.replace('<em>' + word + '</em>', '~')
            r_pattern = re.compile(r'<div>[\d]+、([^<>]+)</div>')
            sentence_list = r_pattern.findall(line)
            if sentence_list:
                return sentence_list
    return []

if __name__ == '__main__':
    with open(file='common_set.txt', mode='r', encoding='utf-8') as fr:
        with open(file='common_set_sentence.txt', mode='w', encoding='utf-8') as save:
            lines = []
            for line in fr:
                lines.append(line.strip())
            for idx, line in enumerate(lines):
                print(str(idx) + '/' + str(len(lines)))
                word_list = line.split('\t')
                if len(word_list) == 2:
                    word1 = word_list[0]
                    word2_list = word_list[1].split(' ')
                    word_list = [word1]
                    word_list.extend(word2_list)
                sentence_list = []
                for word in word_list:
                    sentence_list.extend(req(word=word))
                print(word_list, sentence_list)
                save.write(json.dumps({
                    'word' : word_list[0],
                    'sentence_list' : sentence_list
                }, ensure_ascii=False) + '\n')