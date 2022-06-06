# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse
import time 
import os

url = "https://dena.com/jp/"

#TODO:void(0)の対策を入れる
def crawl(url:str,org:list,accessed:list,unaccessed:list,times:int = 0,fqdn:str = None) :
    if times > 0 :
        print(unaccessed[0])
    html = requests.get(url) 
    soup = BeautifulSoup(html.content, "html.parser")
    # print(soup)
    for element in soup.find_all("a"):
        link = str(element.get("href"))

        if "void(0)" in link or "?" in link:
            continue
        if "#" == link:
            continue
        if "/" == link:
            continue
        if link not in org and times == 0:
            fqdn = urlparse(url).netloc
            if link[0:4] != "http":
                parsed = urlparse(url)
                link = "{}://{}{}".format(parsed.scheme,parsed.netloc,link)
                org.append(link)
                unaccessed.append(link)
            else:
                org.append(link)
                unaccessed.append(link)

            if fqdn == urlparse(link).netloc:
                org.append(link)
                unaccessed.append(link)

        elif link not in org and urlparse(link).netloc == fqdn:
            if link[0:4] != "http":
                parsed = urlparse(url)
                link = "{}://{}{}".format(parsed.scheme,parsed.netloc,link)
                org.append(link)
                unaccessed.append(link)
            else:
                org.append(link)
                unaccessed.append(link)

            


    if len(unaccessed) == 0:
        return org

    next_url = unaccessed.pop(0)
    accessed.append(link)
    times += 1

    time.sleep(0.1)
    if times == 1:
        fqdn = urlparse(url).netloc
        os.mkdir(fqdn)
        f = open('./{}/{}.txt'.format(fqdn,soup.head.title.string.strip()), 'w')

    f = open('./{}/{}.txt'.format(fqdn,soup.head.title.string.strip()), 'w')
    f.write(str(soup.body.text))
    f.close()
    if times == 1:
        return crawl(next_url,org,accessed,unaccessed,times,urlparse(url).netloc)
    return crawl(next_url,org,accessed,unaccessed,times,fqdn)    

print(crawl(url,[],[],[]))