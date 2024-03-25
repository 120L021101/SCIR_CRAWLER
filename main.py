import requests
import re
import json
import unicodedata
import threading
import random
import time

threading_word_list = []
threading_search_set_list = []
threading_real_word_set_list = []
word_set = set()
real_word_set = set()

r_pattern = re.compile(r'<a href="(//cidian\.bi0\.cn/[^.]+\.html)">([^a-z]{4})</a>')
def req(site : str):
    ret = []
    url = 'https:' + site
    params = {

    }
    headers = {
        'accept' : 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
        'origin' : 'https://cidian.bi0.cn',
        'referer' : 'https://cidian.bi0.cn/',
        'user-agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36 Edg/108.0.1462.42'
    }
    count = 1
    while count <= 5:
        try:
            response = requests.get(url=url, params=params, headers=headers, timeout=5)
            response.encoding = 'utf-8'
            ret = r_pattern.findall(response.text)
            response.close()
            break
        except:
            count += 1
            if count == 5:
                print('实在失败了')
    time.sleep(0.2)
    return ret

def req_list(i : int, word_set : set) -> None:
    global threading_word_list, threading_search_set_list, threading_real_word_set_list

    word_list = threading_word_list[i]
    search_set = threading_search_set_list[i]
    this_real_word_set = threading_real_word_set_list[i]

    count = 1
    total_num = len(word_list)
    for word in word_list:
        print(str(count) + '/' + str(total_num))
        for w in req(word):
            site = w[0]
            word2 = w[1]
            if site not in word_set:
                search_set.add(site)
            this_real_word_set.add(word2)
        count += 1
    
c = 20

def levelOrder(word_list : list, write_file) -> None:
    global c, threading_word_list, threading_search_set_list, word_set, threading_real_word_set_list
    c -= 1
    if 0 == c:
        return

    threading_word_list = []
    threading_search_set_list = []
    threading_real_word_set_list = []
    threading_num = 20

    for i in range(threading_num):
        threading_word_list.append([])
        threading_search_set_list.append(set())
        threading_real_word_set_list.append(set())
    for word in word_list:
        idx = random.randint(0, threading_num - 1)
        threading_word_list[idx].append(word)
    
    threading_list = []
    for i in range(threading_num):
        threading_list.append(threading.Thread(target=req_list, args=(i, word_set)))
        threading_list[-1].start()
    for i in range(threading_num):
        threading_list[i].join()
    
    search_set = set()
    for i in range(threading_num):
        for word in threading_search_set_list[i]:
            search_set.add(word)
        for word in threading_real_word_set_list[i]:
            real_word_set.add(word)
    for word in search_set:
        word_set.add(word)
    filter_word_list = list(search_set)
    if not filter_word_list:
        return
    levelOrder(filter_word_list,  write_file)

if __name__ == '__main__':
    read_file = open(file='site.txt', mode='r', encoding='utf-8')
    write_file = open(file='chengyu.txt', mode='w', encoding='utf-8')

    word_list = []
    for line in read_file.readlines():
        word = line.strip()
        word_set.add(word)
        word_list.append(word)
    levelOrder(word_list=word_list, write_file=write_file)
    for word in real_word_set:
        write_file.write(word + '\n')

    read_file.close()
    write_file.close()

# r_pattern = re.compile(r'<a href="(//cidian\.bi0\.cn/[^.]+\.html)">([^a-z]{4})</a>')
# def req(word : str):
#     url = 'https://www.bi0.cn/e/search/index.php'
#     datas = {
#         'keyboard[]' : word,
#         'show' : 'k',
#         'hh' : 'LK',
#         'tempid' : '3',
#         'classid' : '76'
#     }
#     headers = {
#         'accept' : 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
#         'accept-encoding': 'gzip, deflate, br',
#         'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
#         'origin' : 'https://cidian.bi0.cn',
#         'referer' : 'https://cidian.bi0.cn/',
#         'user-agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36 Edg/108.0.1462.42'
#     }
#     response = requests.post(url=url, data=datas, headers=headers, timeout=30)
#     response.encoding = 'utf-8'
#     response.close()
#     return r_pattern.findall(response.text)

# threading_words_lists = []
# threading_search_lists = []
# Search_set = set()

# def req_list(i : int):
#     words_list = threading_words_lists[i]
#     search_list = threading_search_lists[i]
#     length = len(words_list)
#     for idx, word in enumerate(words_list):
#         print(str(idx) + '/' + str(length))
#         for site_and_word in req(word):
#             word = site_and_word[1]
#             site = site_and_word[0]
#             if word not in Search_set:
#                 search_list.append(site)
    

# if __name__ == '__main__':
#     with open(file='site10.txt', mode='w', encoding='utf-8') as fw:
#         words_list = []
#         with open(file='chengyu10.txt', mode='r', encoding='utf-8') as fr:
#             for line in fr:
#                 words_list.append(line.strip())
#         threading_num = 15
#         for i in range(threading_num):
#             threading_words_lists.append([])
#             threading_search_lists.append([])
        
#         for word in words_list:
#             idx = random.randint(0, threading_num - 1)
#             threading_words_lists[idx].append(word)
#         threading_list = []

#         for i in range(threading_num):
#             threading_list.append(threading.Thread(target=req_list, args=(i, )))
#             threading_list[-1].start()
        
#         for thr in threading_list:
#             thr.join()
        
#         for list in threading_search_lists:
#             for word in list:
#                 if word:
#                     fw.write(word + '\n')
        