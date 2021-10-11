import webbrowser
import platform
import requests
from bs4 import BeautifulSoup
import urllib.request as ur
import json
import re
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import datetime
import googletrans
import pandas as pd
from datetime import datetime
import sqlite3
# MacOS
#chrome_path = 'open -a /Applications/Google\ Chrome.app %s'
# Windows
chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
# Linux
# chrome_path = '/usr/bin/google-chrome %s'
result = ""
def __init__(self):
    chrome_path='C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'

def CurrencyRate():
    r = requests.get('https://rate.bot.com.tw/xrt?Lang=zh-TW')
    soup = BeautifulSoup(r.content, 'lxml')

    body = soup.select("#ie11andabove > div > table > tbody")
    th_all = body[0].find_all('tr')
    print('type',type(th_all))
    print('len',len(th_all))
    list =[]
    global result
    result=""
    for item in th_all:
        currency = item.find("div",class_="visible-phone print_hide").text.replace(" ","")
        price = item.find_all("td",class_="rate-content-cash text-right print_hide")
        price_buy = (price[0].text)
        price_sell = (price[1].text)
        result += "幣別:"+currency+" 買入:"+price_buy+"賣出"+price_sell+"\n"

    print(result)

#查詢台中天氣
def SearchingWeather():
    f = open("output.txt", 'r')
    content = f.read()
    f.close()
    content = content.split("查詢天氣")[1]
    content = content.replace("台","臺")
    citylist = ["臺北市","新北市","桃園市","臺中市","臺南市","高雄市","新竹縣","苗栗縣","彰化縣","南投縣","雲林縣","嘉義縣","屏東縣","宜蘭縣","花蓮縣","臺東縣","澎湖縣","金門縣","連江縣","基隆市","新竹市","嘉義市"]
    if content in citylist:
        content = content
    else:
        content="臺北市"
    global result
    result = ""
    token = "CWB-33EA397F-4951-4D18-8236-4BF2F07DE537"
    url = 'https://opendata.cwb.gov.tw/api/v1/rest/datastore/F-C0032-001?Authorization=' + token + '&format=JSON&locationName=' + str(
        content)
    Data = requests.get(url)
    Data = (json.loads(Data.text, encoding='utf-8'))['records']['location']
    #print(Data)
    #print((Data[0]['locationName']))
    city = (Data[0]['locationName'])
    weather = (Data[0]['weatherElement'][0]['time'][0]['parameter']['parameterName'])
    degree = ((Data[0]['weatherElement'][2]['time'][0]['parameter']['parameterName']))

    result = (city+"\n氣候:"+weather+" 溫度:"+degree)


#中翻英
def TransEnglish():
    #print("global",Main.getGlobalText())
    # Initial
    f = open("output.txt",'r')
    content = f.read()
    f.close()
    content = content.strip()
    content =  content.split("翻譯")[1]
    translator = googletrans.Translator()
    global result
    result = translator.translate(content).text


#開啟網頁
def openWithURL():
    url=input()
    webbrowser.get(chrome_path).open(url)
def openURL(url):
    webbrowser.get(chrome_path).open(url)



#爬取維基百科
def SearchWiki():
    SaraSpeak.SpeakChinese("請給我你要搜尋的名稱")
    searching=input('請輸入你要搜索什麼:')
    res=requests.get('https://zh.wikipedia.org/wiki/{}'.format(searching))
    soup=BeautifulSoup(res.text,'lxml')
    result=soup.select_one('.mw-parser-output p').text
    time.sleep(1)
    SaraSpeak.SpeakChinese("以上為維基百科搜尋結果")
    print(result)
#星座運勢
def constellationLuck():
    SaraSpeak.SpeakChinese('你是什麼星座?')
    choose=input("請問你的星座是？(1)牡羊 (2)金牛 (3)雙子 (4)巨蟹 (5)獅子 (6)處女 (7)天秤 (8)天蠍 (9)射手 (10)摩羯 (11)水瓶 (12)雙魚)")
    r=requests.get('https://m.click108.com.tw/astro/index.php?astroNum='+choose)
    soup=BeautifulSoup(r.content,'lxml')
    dayluktitle=soup.find(id='astroDailyWording')
    print('今日運勢:'+dayluktitle.text)
    dayloveluk=soup.find(id='astroDailyData_love')
    print('愛情運:'+dayloveluk.text)
#電影推薦
def MovieRecommand():
    global result
    r=requests.get('https://movies.yahoo.com.tw/movie_intheaters.html')
    soup=BeautifulSoup(r.content,'lxml')
    soupresult=soup.find("ul",{"class":"ranking_list_r"})
    temp = soupresult.text.splitlines()
    check =""
    for i in range(len(temp)):
        #print(len(temp[i]))
        #print("----------------")
        if len(temp[i]) is 0 and i<len(temp)-1:
            print(i)
            if len(temp[i+1]) is 0:
                temp[i] =""
            else:
                temp[i] = "\n"
        check+=temp[i]
    #print(check)
    result ="以下是我根據本周熱門排行 推薦的電影\n"+ check
    return result
def ListenMusic():
    import youtube_dl
    SaraSpeak.SpeakChinese('請問你要聽什麼音樂')
    time.sleep(1)
    print('請問你要聽什麼音樂?')
    User_Saymusic=SaraListen.Listen()
    if User_Saymusic:
        url='https://www.youtube.com/results?search_query='+User_Saymusic
        print(url)
        r=requests.get(url)
        soup=BeautifulSoup(r.content,'lxml')
        downloadTarget=soup.select('h3')[3].select('a')[0]['href']
        url="https://www.youtube.com"+downloadTarget
        openURL(url)
    else:
        SaraSpeak.SpeakChinese('不好意思我聽不懂 你可以輸入給我嗎')
        searchMusic=input('請問你想聽什麼音樂?')
        url='https://www.youtube.com/results?search_query='+searchMusic
        print(url)
        r=requests.get(url)
        soup=BeautifulSoup(r.content,'lxml')
        downloadTarget=soup.select('h3')[3].select('a')[0]['href']
        url="https://www.youtube.com"+downloadTarget
        openURL(url)

if __name__ == '__main__':
    MovieRecommand()