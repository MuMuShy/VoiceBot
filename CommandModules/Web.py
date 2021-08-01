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
# MacOS
#chrome_path = 'open -a /Applications/Google\ Chrome.app %s'
# Windows
chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
# Linux
# chrome_path = '/usr/bin/google-chrome %s'
def __init__(self):
    chrome_path='C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'

#開啟網頁
def openWithURL():
    url=input()
    webbrowser.get(chrome_path).open(url)
def openURL(url):
    webbrowser.get(chrome_path).open(url)
#查詢台中天氣
def SearchingWeather():
    url = 'https://opendata.cwb.gov.tw/api/v1/rest/datastore/O-A0001-001?Authorization=CWB-250D5B86-5B3B-4E12-B419-8C39A9EC4CDC&format=JSON&locationName=%E6%A1%83%E5%9C%92&elementName=TEMP'
    site = ur.urlopen(url)
    page = site.read()
    contents = page.decode()
    data = json.loads(contents)
    print(data)
    temp = data['records']['location'][0]['weatherElement'][0]['elementValue']
    print(temp)
    return temp
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
    SaraSpeak.SpeakChinese('我來幫你看看有什麼最新電影')
    r=requests.get('https://movies.yahoo.com.tw/movie_intheaters.html')
    soup=BeautifulSoup(r.content,'lxml')
    result=soup.find("ul",{"class":"ranking_list_r"})
    time.sleep(3)
    SaraSpeak.SpeakChinese('這些是我推薦的電影~')
    time.sleep(2)
    print("以下是我推薦的電影 :")
    print(result.text.replace("\n",""))
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
    SearchingWeather()