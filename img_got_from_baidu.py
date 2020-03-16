import re
import requests
import urllib2
from bs4 import BeautifulSoup
import os
 
num = 0
numPicture = 0
file = ''
List = []
 
 
def Find(url):
    global List
    print('in finding url')
    num_of_url = 0
    length_of_string = 0
    while num_of_url < 1000:
        Url = url + str(num_of_url)
        try:
            Result = requests.get(Url, timeout=7)
        except BaseException:
            num_of_url = num_of_url + 60
            continue
        else:
            result = Result.text
            pic_url = re.findall('"objURL":"(.*?)",', result, re.S)  
            length_of_string += len(pic_url)
            if len(pic_url) == 0:
                break
            else:
                List.append(pic_url)
                num_of_url = num_of_url + 60
    return length_of_string
 
 
def recommend(url):
    Re = []
    try:
        html = requests.get(url)
    except urllib2.error.HTTPError as e:
        return
    else:
        html.encoding = 'utf-8'
        bsObj = BeautifulSoup(html.text, 'html.parser')
        div = bsObj.find('div', id='topRS')
        if div is not None:
            listA = div.findAll('a')
            for i in listA:
                if i is not None:
                    Re.append(i.get_text())
        return Re
 
 
def dowmloadPicture(html, keyword):
    global num
    pic_url = re.findall('"objURL":"(.*?)",', html, re.S)  
    print('find key word:' + keyword + 'start to download img...')
    for each in pic_url:
        print('Order is :' + str(num + 1) + 'Address is :' + str(each))
        try:
            if each is not None:
                pic = requests.get(each, timeout=7)
            else:
                continue
        except BaseException:
            print('error, check your connection')
            continue
        else:
            string = file + r'/' + keyword + '_' + str(num) + '.jpg'
            fp = open(string, 'wb')
            fp.write(pic.content)
            fp.close()
            num += 1
        if num >= numPicture:
            return
 
 
if __name__ == '__main__':  
    word = raw_input("input key word")
    url = 'http://image.baidu.com/search/flip?tn=baiduimage&ie=utf-8&word=' + str(word) + '&pn='
    tot = Find(url)
    Recommend = recommend(url)  
    print('is %stypes consist of %d imgs' % (word, tot))
    numPicture = int(raw_input('input the limitation number '))
    file = raw_input('input the folder name')
    y = os.path.exists(file)
    if y == 1:
        print('file exists')
        file = raw_input('input the folder name')
        os.mkdir(file)
    else:
        os.mkdir(file)
    t = 0
    tmp = url
    while t < numPicture:
        try:
            url = tmp + str(t)
            result = requests.get(url, timeout=10)
            print(url)
        except urllib2.error.HTTPError as e:
            print('error, check your connection')
            t = t+60
        else:
            dowmloadPicture(result.text, word)
            t = t + 60
 
    print('end')
    print('for more you like')
    for recommend in Recommend:
        print(recommend)
        print '  '