#!/usr/bin/env python
# -*- coding: utf-8, euc-kr -*-
# 다른 포털 기사도 크롤링 할 수 있도록 시도해봤는데 생각보다 잘 안돼서 특정 포털의 모든 언론사를 크롤링 하는 코드를 만들어 봤습니다.

from bs4 import BeautifulSoup
from urllib.request import urlopen
import csv
import platform

class Press(object):
    def __init__(self):
        pass

    def crawling(self, press):
        URL = ""
        ul= ""
        pressList=[]
        user_operating_system = str(platform.system())
            
        # 다음 언론사 크롤링
        if press == "다음":
            URL = "https://media.daum.net/cp/"
            ul = "list_cp"

        # 네이버 언론사 크롤링 (링크를 모두 맞게 했는데 정상작동이 안되는 상황)
        elif press == "네이버":
            URL = "https://news.naver.com/main/officeList.nhn"
            ul = "group_list"
        
        # 크롤링한 언론사들 리스트에 저장
        url = urlopen(URL)
        document = BeautifulSoup(url, 'html.parser')
        for link in document.find_all("ul", {"class": ul}):
            for li in link.find_all("li"):
                pressList.append(li.find("a").get_text())

        #csv 작성
        if user_operating_system == "Windows":
            f = open(press+'_언론사_목록.csv','w', encoding='euc-kr',newline='')
        else: #다른 OS는 utf-8 이용.
            f = open(press+'_언론사_목록.csv','w', encoding='utf-8',newline='')
        wr = csv.writer(f)
        for i in pressList:
            wr.writerow([i])
        f.close()

if __name__ == "__main__":
    Crawler = Press()
    press = input("언론사 입력(네이버 / 다음) : ")
    Crawler.crawling(press)
