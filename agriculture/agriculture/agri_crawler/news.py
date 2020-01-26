from bs4 import BeautifulSoup
import requests, threading
import time
from .models import title, state1, KBS,SBS,MBC,JTBC,YTN, dailyEconomy, moneyToday, eDaily, seoulEconomy, koreaEconomy,Emoticon,news_count
class news_crawler(threading.Thread):
    def __init__(self,keyword, sd, ed, ID,media,t,b,d,k,e,c,l,number):
      threading.Thread.__init__(self)
      self.keyword = keyword
      self.sd = sd
      self.ed = ed
      self.ID = ID
      self.t = t
      self.b = b
      self.d = d
      self.k = k
      self.e = e
      self.c = c
      self.l = l
      self.media=media
      self.number = number
    def get_bs_obj(self, keyword, sd, ed, page): # beautifulsoup 객체 얻음
         url = "https://search.daum.net/search?nil_suggest=btn&w=news&DA=STC&cluster=y&q="+keyword+"&p="+page+"&sd="+sd+"000000&ed="+ed+"235959&period=u"
         result = requests.get(url)
         bs_obj = BeautifulSoup(result.content, "html.parser")
         return bs_obj
    def get_data_date(self, keyword, sd, ed, page): #날짜 확인하기
        bs_obj = self.get_bs_obj(keyword, sd, ed, page) 
        total_num = bs_obj.find("span",{"class":"txt_info"})
        total_num = self.get_total_num(total_num)
        return total_num
    def get_total_num(self,total_num): # 건수 예외처리하기 
         total_text = total_num.text
         split = total_text.split()
         length = len(split)
         if length == 4:
           text = split[3].replace(",","")
           text = text.replace("건","")
         else:
           text = split[2].replace(",","")
           text = text.replace("건","")
         text = int(text)
         return text
    def get_bs_incontent(self, url):
         result = requests.get(url)
         bs_obj = BeautifulSoup(result.content, "html.parser")
         return bs_obj
    def run(self):
        datevalue = self.get_data_date(self.keyword, self.sd, self.ed, "1")         
        print(datevalue)
        datevalue = int(datevalue/10)
        cnt=0
        count=[0,0,0,0,0,0,0,0,0,0]
        News = news_count()
        News.login_id= self.ID
        for i in range(0,datevalue):
            page = str(i)
            bs_obj = self.get_bs_obj(self.keyword, self.sd, self.ed, page)
            news_lists = bs_obj.findAll("div",{"class":"wrap_cont"})
            for li in news_lists:
                 time.sleep(2)
                 span_text = li.find("span",{"class":"f_nb date"}).text
                 span_split = span_text.split()
                 len_span = len(span_split)
                 if len_span == 3:
                   continue 
                 elif len_span == 5:
                       a_url = li.find("a",{"class":"f_nb"})
                       new_a_url = a_url['href']  
                       new_bs_obj = self.get_bs_incontent(new_a_url)
                       Title = new_bs_obj.find("h3",{"class":"tit_view"}).text
                       body = new_bs_obj.find("div",{"id":"mArticle"}).text
                       times = new_bs_obj.find("span",{"class":"txt_info"}).text 
                       print(self.k)
                       if self.k != "k":
                          self.keyword = ""
                       if self.b != "b":
                          body = ""
                       if self.d != "d":
                          times = ""
                       if self.t !="t":
                          Title = ""
                       contents = title(main_title = Title, main_body =body, datetime = times, media="서울경제", count=1)
                       print(Title)
                       print(span_split[2])
                       print(self.media['daily'])
                       if span_split[2] == "KBS" and self.media['kbs']==True:
                                 kbs = KBS()
                                 kbs.nickname=self.ID
                                 kbs.keyword = self.keyword
                                 kbs.sub_body = contents
                                 kbs.save()
                                 cnt = cnt+1
                                 count[0]=count[0]+1
                       elif span_split[2] == "MBC" and self.media['mbc'] ==True:
                                 mbc = MBC()
                                 mbc.nickname=self.ID
                                 mbc.keyword = self.keyword
                                 mbc.sub_body = contents
                                 mbc.save()
                                 cnt = cnt+1
                                 count[1]=count[1]+1
                       elif span_split[2] == "SBS" and self.media['sbs'] ==True:
                                 sbs = SBS()
                                 sbs.nickname=self.ID
                                 sbs.keyword = self.keyword
                                 sbs.sub_body = contents
                                 sbs.save()
                                 cnt = cnt+1
                                 count[2]=count[2]+1
                       elif span_split[2] == "JTBC" and self.media['jtbc']==True:
                                 jtbc = JTBC()
                                 jtbc.nickname=self.ID
                                 jtbc.keyword = self.keyword
                                 jtbc.sub_body = contents
                                 jtbc.save()
                                 cnt = cnt+1
                                 count[3]=count[3]+1
                       elif span_split[2] == "YTN" and self.media['ytn']==True:
                                 ytn = YTN()
                                 ytn.nickname=self.ID
                                 ytn.keyword = self.keyword
                                 ytn.sub_body = contents
                                 ytn.save()
                                 cnt = cnt+1
                                 count[4]=count[4]+1
                       elif span_split[2] == "매일경제" and self.media['daily']==True:
                                 dailyEco = dailyEconomy()
                                 dailyEco.nickname=self.ID
                                 dailyEco.keyword = self.keyword
                                 dailyEco.sub_body = contents
                                 dailyEco.save()
                                 cnt = cnt+1
                                 count[5]=count[5]+1
                       elif span_split[2] == "머니투데이" and self.media['money']==True:
                                 money = moneyToday()
                                 money.nickname=self.ID
                                 money.keyword = self.keyword
                                 money.sub_body = contents
                                 money.save()
                                 cnt = cnt+1
                                 count[6]=count[6]+1
                       elif span_split[2] == "이데일리" and self.media['eDaily']==True: 
                                 edaily = eDaily()
                                 edaily.nickname=self.ID
                                 edaily.keyword = self.keyword
                                 edaily.sub_body = contents
                                 edaily.save()
                                 cnt = cnt+1
                                 count[7]=count[7]+1
                       elif span_split[2] == "서울경제" and self.media['seoul']==True:    
                                 seoul = seoulEconomy()
                                 self.nickname=self.ID
                       	         seoul.keyword = self.keyword
                                 seoul.sub_body = contents
                                 seoul.save()
                                 cnt = cnt+1
                                 count[8]=count[8]+1
                       elif span_split[2] == "한국경제" and self.media['korea']==True:
                                 korea = koreaEconomy()
                                 korea.nickname=self.ID
                                 korea.keyword = self.keyword
                                 korea.sub_body = contents
                                 korea.save()
                                 cnt = cnt+1
                                 count[9]=count[9]+1
        name = state1.objects.filter(id=self.number, type_state=0).first()
        name.state= cnt
        name.save()
        News.kbs_count=int(count[0])
        News.mbc_count=int(count[1])
        News.sbs_count=int(count[2])
        News.jtbc_count=int(count[3])
        News.ytn_count=int(count[4])
        News.dailyeconomy_count=int(count[5])
        News.edaily_count=int(count[6])
        News.korea_count=int(count[7])
        News.money_count=int(count[8])
        News.seouleconomy_count=int(count[9])
        News.save()
        print("끝")