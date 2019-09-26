from bs4 import BeautifulSoup

import requests

def parse():
    URL = 'http://base.garant.ru/10108000/'
    r= requests.get(URL)
    handle = open("articles.txt","w")
    soup = BeautifulSoup(r.content,'lxml')
    lis = soup.findAll("li", {"class": "no_img statya"})
    for li in lis:
        handle.write(li.find('a').contents[0]+'\n')
    handle.close()

def get():
    articles = []
    f = open('power.txt')
    for line in f.readlines():
        articles.append(line)
    print(articles)


articles = []
f = open('articles.txt')
for line in f.readlines():
    articles.append(line)
print(articles)