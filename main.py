import requests 
from bs4 import BeautifulSoup
import lxml
import threading
import sys
import os

url = 'https://www.pravda.com.ua/news/'

titles = []
def set_interval(func, sec):
    def func_wrapper():
        set_interval(func, sec)
        func()
    t = threading.Timer(sec, func_wrapper)
    t.start()
    return t

def printFeed():
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "lxml")
    news = []
    feed = soup.find(attrs={"id": "endless"})
    for article in feed.find_all('div', attrs={"class": "article"}):
        news.insert(0,  article)
    
    global titles
    titlesTemp = []
    for new in news:
        str = new.find('div', attrs={"class": "article__title"}).a.string
        if str:
            titlesTemp.append(str)
        else:
            str = new.find('div', attrs={"class": "article__title"}).a.contents[1]
            titlesTemp.append(str)
    
    if(titlesTemp != titles):
        os.system('CLS')
        for title in titlesTemp:
            print(' ', title, '\n')
        titles = titlesTemp

printFeed()
set_interval(printFeed, 5)
