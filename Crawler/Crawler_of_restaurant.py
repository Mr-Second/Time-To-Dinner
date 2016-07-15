#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import requests, json, pyprind, sys, shutil
from bs4 import BeautifulSoup
base_url = "http://www.gomaji.com/"
json_arr = {}

def startCrawler(fileName):
    res = requests.get('http://www.gomaji.com/index.php?city=Taichung')
    #一開始的台中頁面  然後去爬上面所有的餐廳分類網址
    soup = BeautifulSoup(res.text)

    location = soup.select('.sf-with-ul')[0].text
    global json_arr 
    json_arr = {location:{}}

    aLen = len(soup.select("#lb_tag  a"))/2 # "lb_tag  a"是餐廳分類的tag 但是每個分類都有2個重複的tag，所以要/2
    aIndex = 1
    recipNum = len(soup.select('ul.deal16 li.box-shadow2px'))
    ProgreBar = pyprind.ProgBar(aLen, title = "%s 共 %d 個餐廳類別要處理" %( location, aLen))
    for a in soup.select("#lb_tag  a"):
        href = a['href']
        resType = a.text
        if aIndex > aLen: break
        parsePage(base_url+href, location, resType)
        aIndex = aIndex + 1
        ProgreBar.update(1,item_id = aIndex, force_flush=True)#item_id可以讓使用者追蹤到底執行到第幾個ID
        #ID通常是放for loop裏面的變數，update()會讓進度條更新

    #建立一個進度條物件
    dump(fileName)

def parsePage(url, location, resType):
    res = requests.get(url)
    childSoup = BeautifulSoup(res.text)
    tmp = {resType:[]}

    for i, img in zip(childSoup.select('ul.deal16 li.box-shadow2px'), childSoup.select('ul.deal16 li.box-shadow2px img')):
        href = i.find('a')['href']# 把a的href屬性的值抓出來
        href = base_url+href
        d = getResProf(href)

        name = i.find('a').find('div','boxc').find('h2')# find可以找到他的child那一層
        name = purgeResName(name.text.strip(), d)

        imageUrl = img['src']
        img = requests.get(imageUrl,stream=True)
        with open(name+'.jpg', 'wb') as f:
            shutil.copyfileobj(img.raw, f)
        d["url"] = href
        tmp[resType].append(d)

    json_arr[location].update(tmp)

def dump(fileName):
    with open(fileName, 'w', encoding='UTF-8') as f:
        json.dump(json_arr, f)

def purgeResName(raw, d):
    try:
        return d['restaurant']
    except Exception as e:
        return raw.split('】')[0].replace('【','')

def getResProf(href):
    res = requests.get(href)
    resSoup = BeautifulSoup(res.text)
    tmp = {}
    # tmp['restaurant'] = resSoup.find('div', style="display: table-cell;").text
    # print(tmp['restaurant'])
    num=1
    try:
        for i in resSoup.findAll('div', style="display: table-cell;")[1].children:
            try:
                if len(i.text) > 0:     
                    if num==1:
                        tmp['restaurant'] = i.text   
                    else:        
                        i = i.text.replace('\n','')
                        clean = i.split('：')
                        tmp[clean[0]] = clean[1]
                    num=num+1
            except AttributeError as e:
                pass
    except Exception as e:
        print(href)
    
    return tmp

if __name__  ==  "__main__":
    if len(sys.argv) < 2:
        #sys.argv[0]是模組名稱喔!
        print("Usage:\n\tpython[3] "+sys.argv[0]+" <filename.json>")
        print("\n\tURL can be:http://www.gomaji.com/index.php?city=Taichung&tag_id=99");
        sys.exit(1)#0為正常結束，其他數字exit會拋出一個例外，可以被捕獲
    startCrawler(sys.argv[1])
