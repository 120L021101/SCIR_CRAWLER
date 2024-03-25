import json
import requests
import re
import threading
import random
import gzip 
def gzdecode(data):
    return gzip.decompress(data).decode('utf8')

threading_item_list = []
threading_list = []
threading_num = 20
for i in range(threading_num):
    threading_item_list.append([])

url = 'https://zaojv.com/wordQueryDo.php'
def req2(item : dict):
    datas = {
        'nsid' : 0,
        's': 4595742426291063331,
        'q':'',
        'wo': item['word'],
        'directGo':1
    }
    headers = {
        'Accept' : 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'Accept-Encoding' : 'gzip, deflate, br',
        'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36 Edg/108.0.1462.42'
    }
    response = requests.post(url, datas,headers=headers)
    with open(file='svae.html', mode='w', encoding='utf-8') as save:
        save.write(response.text)
    line_list = response.text.split('\n')
    for idx, line in enumerate(line_list):
        if 'student' in line:
            idx += 2
            line = line.replace('<em>' + item['word'] + '</em>', '~')
            r_pattern = re.compile(r'<div>[\d]+、([^<>]+)</div>')
            sentence_list = r_pattern.findall(line)
            if sentence_list:
                item['sentence_list'].extend(sentence_list)
            r_pattern = re.compile(r'<div>（[\d]+）([^（）<>]+)</div>')
            sentence_list = r_pattern.findall(line)
            if sentence_list:
                item['sentence_list'].extend(sentence_list)
    if 'sentence' in item.keys():
        item['sentence_list'] = item['sentence']
        item.pop('sentence')
def req(item):
    while True:
        try:
            url = 'http://www.baidu.com/s'
            params = {
                'wd' : item['word'] + '造句科举答题网'
            }
            headers = {
                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
                # 'Accept-Encoding': 'gzip, deflate, br',
                'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
                'Connection': 'keep-alive',
                'Host': 'www.baidu.com',
                'sec-ch-ua': '"Not?A_Brand";v="8", "Chromium";v="108", "Microsoft Edge";v="108"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"',
                'Sec-Fetch-Dest': 'document',
                'Sec-Fetch-Mode': 'navigate',
                'Sec-Fetch-Site': 'none',
                'Sec-Fetch-User': '?1',
                'Cookie' : '__yjs_duid=1_819127a515d5f720fe2c7244638e6b021635328635328; BIDUPSID=E855469DFDDB14ED63B4C8A220C85226; PSTM=1637224461; BDUSS=w1YThzRmd3NkFkSUE5a1VKfjdpeUdmTGlBRTBDT0dDVEN6ZXJJUS1WZzd4NDVpRVFBQUFBJCQAAAAAAAAAAAEAAABaSrRjwcvBy7y4uPa~tAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAADs6Z2I7OmdicG; BDUSS_BFESS=w1YThzRmd3NkFkSUE5a1VKfjdpeUdmTGlBRTBDT0dDVEN6ZXJJUS1WZzd4NDVpRVFBQUFBJCQAAAAAAAAAAAEAAABaSrRjwcvBy7y4uPa~tAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAADs6Z2I7OmdicG; BAIDUID=3E9041FE7E332A1D15CF0B665CF71251:FG=1; BD_UPN=12314753; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; BAIDUID_BFESS=3E9041FE7E332A1D15CF0B665CF71251:FG=1; BD_CK_SAM=1; PSINO=1; delPer=0; BA_HECTOR=8g2404810h840hak810l2l7f1hst3db1k; ZFY=6bkJyfWdU6smyx2sagSBowqD9rqHIvOZ7ByRzH9cBPI:C; H_PS_PSSID=36559_37555_36920_37990_36807_37936_26350_37958_22159_37881; sugstore=0; H_PS_645EC=e443gZ1p46EC1gVlEoY8o0yGvs2MpZfotFoRy%2FegRbZ3WK7p2sCLDbQo0FE',
                'Upgrade-Insecure-Requests': 1,
                'User-Agent':' Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36 Edg/108.0.1462.42'
            }
            response = requests.get(url=url, params=params, headers=headers, timeout=5)
            line_list = response.text.split('\n')
            for line in line_list:
                if 'mu="https://www.kejudati.com/juread/' in line:
                    headers = {
                        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
                        # 'Accept-Encoding': 'gzip, deflate, br',
                        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
                        'Connection': 'keep-alive',
                        # 'Host': 'www.baidu.com',
                        'sec-ch-ua': '"Not?A_Brand";v="8", "Chromium";v="108", "Microsoft Edge";v="108"',
                        'sec-ch-ua-mobile': '?0',
                        'sec-ch-ua-platform': '"Windows"',
                        'Sec-Fetch-Dest': 'document',
                        'Sec-Fetch-Mode': 'navigate',
                        'Sec-Fetch-Site': 'none',
                        'Sec-Fetch-User': '?1',
                        'Cookie' : '__yjs_duid=1_819127a515d5f720fe2c7244638e6b021635328635328; BIDUPSID=E855469DFDDB14ED63B4C8A220C85226; PSTM=1637224461; BDUSS=w1YThzRmd3NkFkSUE5a1VKfjdpeUdmTGlBRTBDT0dDVEN6ZXJJUS1WZzd4NDVpRVFBQUFBJCQAAAAAAAAAAAEAAABaSrRjwcvBy7y4uPa~tAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAADs6Z2I7OmdicG; BDUSS_BFESS=w1YThzRmd3NkFkSUE5a1VKfjdpeUdmTGlBRTBDT0dDVEN6ZXJJUS1WZzd4NDVpRVFBQUFBJCQAAAAAAAAAAAEAAABaSrRjwcvBy7y4uPa~tAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAADs6Z2I7OmdicG; BAIDUID=3E9041FE7E332A1D15CF0B665CF71251:FG=1; BD_UPN=12314753; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; BAIDUID_BFESS=3E9041FE7E332A1D15CF0B665CF71251:FG=1; BD_CK_SAM=1; PSINO=1; delPer=0; BA_HECTOR=8g2404810h840hak810l2l7f1hst3db1k; ZFY=6bkJyfWdU6smyx2sagSBowqD9rqHIvOZ7ByRzH9cBPI:C; H_PS_PSSID=36559_37555_36920_37990_36807_37936_26350_37958_22159_37881; sugstore=0; H_PS_645EC=e443gZ1p46EC1gVlEoY8o0yGvs2MpZfotFoRy%2FegRbZ3WK7p2sCLDbQo0FE',
                        'Upgrade-Insecure-Requests': 1,
                        'User-Agent':' Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36 Edg/108.0.1462.42'
                    }
                    r_pattern = re.compile(r'mu=\"([^\"]+)\"')
                    web_site = r_pattern.findall(line)[0]
                    response = requests.get(url=web_site, headers=headers, timeout=5)
                    response.encoding = 'utf-8'
                    text = response.text.split('\n')[0].replace('<b>' + item['word'] + '</b>', '~')
                    r_pattern = re.compile(r'<p >[\d]+、([^<>]+)</p>')
                    item['sentence_list'].extend(r_pattern.findall(text))
                    break
            break
        except:
            continue
def run(idx : int, fuck : str):
    global threading_item_list
    item_list = threading_item_list[idx]
    for _idx, item in enumerate(item_list):
        print(_idx, '/', len(item_list))
        req(item)

if __name__ == '__main__':
    with open(file='common_set_sentence.txt', mode='r', encoding='utf-8') as fr:
        for line in fr.readlines():
            idx = random.randint(0, threading_num - 1)
            threading_item_list[idx].append(json.loads(line.strip()))
    for i in range(threading_num):
        threading_list.append(threading.Thread(target=run, args=(i, 'fuck')))
        threading_list[-1].start()
    for i in range(threading_num):
        threading_list[i].join()
    
    with open(file='common_set_sentences.txt', mode='w', encoding='utf-8') as fw:
        for _list in threading_item_list:
            for item in _list:
                fw.write(json.dumps(item, ensure_ascii=False) + '\n')
_set = set()
with open(file='common_set_sentence.txt', mode='r', encoding='utf-8') as fr:
    for line in fr:
        _set.add(line)
with open(file='common_set_sentences.txt', mode='w', encoding='utf-8') as fr:
    for line in _set:
        fr.write(line)