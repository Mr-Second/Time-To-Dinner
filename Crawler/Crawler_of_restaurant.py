#!/usr/bin/env python3
import requests, json
from bs4 import BeautifulSoup

def startCrawler():
    prod_dict={}
    base_url = "http://www.gomaji.com/"
    fileName = 'gomaji.json'
    json_arr = []

    res = requests.get('http://www.gomaji.com/index.php?city=Taichung&tag_id=99')
    #print(res.text)
    soup = BeautifulSoup(res.text)
    liTag = soup.find_all("li","box-shadow2px ")
    for i in liTag:
        href = i.find('a')['href']# 把a的href屬性的值抓出來
        href = base_url+href

        name = i.find('a').find('div','program').find('h1')# find可以找到他的child那一層
        name = name.text.strip()

        d = {name: href}
        json_arr.append(d)
    
    start_json(fileName)
    to_json(fileName, json_arr)
    end_json(fileName)        


def start_json(json_path):
    with open(json_path, 'w' ,encoding = 'UTF-8') as json_file:
        json_file.truncate()#如果沒有傳入參數的話，就會本全文清空
        #若傳入整數n的話，是指把n位置以後的文字都刪掉
        json_file.write('[')#單純只是寫入而已

def to_json(json_path,arr,notFirst = False):
    # print(arr)
    with open(json_path, 'a', encoding='UTF-8') as json_file:
        #with 述句執行完畢後會自動關檔，後面的as 則是把開檔完的reference指派給as 後的變數
        #as裡面的名稱在外部是看不到的，是區域變數
        for d in arr:
            json_str = json.dumps(d, ensure_ascii=False, sort_keys=True)
            #在這裡使用到json的module,dump是轉存，將python的物件型態轉成json的物件型態
            #因為json是js的型態；ensure_ascii若為true(預設)
            #就會確保所有輸入的字元都是ascii，若非則跳過那個字元
            #設為false就會照原樣輸出
            #sort_keys預設為false，功用為把key做排序
            json_file.write('{}{}'.format((',' if notFirst else ''), json_str))
            #str.format()這個函式，會在{}裡面填入字串，{}裡面可以放index或key名稱
            notFirst = True

def end_json(json_path):
    with open(json_path, 'a' ,encoding = 'UTF-8') as json_file:
        json_file.write(']')

if __name__  ==  "__main__":
    startCrawler()
    #print(course_unit)
    # to_json('ptt_comment.json',course_unit,False)
    # end_json('ptt_comment.json')