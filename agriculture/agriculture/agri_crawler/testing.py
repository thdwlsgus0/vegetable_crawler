# 네이버 주식 
import csv, codecs 
import urllib
import datetime
import time
import base64
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt
import requests
with codecs.open("jinhyun.csv","w", encoding='euc-kr') as fp: # 파일 입출력 대신 방지 오류 효과 탁월
  writer = csv.writer(fp, delimiter=",", quotechar='"') # writer를 선언하고 
  writer.writerow(["date", "final_price", "nomal_price", "high_price", "low_price","trade_cnt"])
# 헤더 정보 주입
header = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36'}
# url 마지막 부분
stockItem = '035810'

url = 'http://finance.naver.com/item/sise_day.nhn?code='+stockItem
request = urllib.request.Request(url, headers = header)
contents = urllib.request.urlopen(request)
#html = urlopen(url, headers= header)
source = contents.read()
source1 = source.decode('euc-kr')
print(source1)
soup = BeautifulSoup(source1, 'html.parser')
maxPage = soup.find_all("table", align="center")
mp = maxPage[0].find_all("td", class_="pgRR")
mpNum = int(mp[0].a.get('href')[-3:])
for page in range(1,300):
  url = 'http://finance.naver.com/item/sise_day.nhn?code='+stockItem+'&page='+str(page)
  request = urllib.request.Request(url, headers=header)
  contents = urllib.request.urlopen(request)
  source = contents.read()
  source1 = source.decode('euc-kr')
  soup = BeautifulSoup(source1, "html.parser")
  srlists=soup.find_all("tr")
  isCheckNone=None
  
  if((page%1)==0):
    time.sleep(1.5)
  for i in range(1,len(srlists)-1):
    if(srlists[i].span != isCheckNone):
      print(srlists[i].td.text)
      with codecs.open("jinhyun.csv", "a", encoding= "euc_kr ") as fp:   
        writer = csv.writer(fp, delimiter=",", quotechar='"')
        writer.writerow([
            srlists[i].find_all("td",align="center")[0].text
          , srlists[i].find_all("td",class_="num")[0].text
          , srlists[i].find_all("td",class_="num")[2].text
          , srlists[i].find_all("td",class_="num")[3].text
          , srlists[i].find_all("td",class_="num")[4].text
          , srlists[i].find_all("td",class_="num")[5].text
])
