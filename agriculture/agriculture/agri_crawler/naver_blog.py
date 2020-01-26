from bs4 import BeautifulSoup
import requests, threading
import time
from .models import naver,title,state1,naver_count
class naver_crawler(threading.Thread):
   def __init__(self, keyword,sd,ed,t,b,d,k,url,ID,number):
       threading.Thread.__init__(self)
       self.keyword = keyword
       self.sd = sd
       self.ed = ed
       self.t = t
       self.b = b
       self.d = d
       self.k = k
       self.url = url
       self.ID = ID
       self.number = number
   def get_data_date(self,keyword, sd, ed, page):
       bs_obj = self.get_bs_obj(keyword, sd, ed, page)
       total_num = bs_obj.find("span",{"class":"title_num"})
       num_split = total_num.text.split()
       replace_total = num_split[2].replace(",","")
       replace_total = replace_total.replace("건","")
       replace_total = int(replace_total)
       return replace_total
   def get_bs_obj(self, keyword, sd, ed, page):
       url="https://search.naver.com/search.naver?where=post&query="+keyword+"&st=sim&sm=tab_opt&date_from="+sd+"&date_to="+ed+"&date_option=8&srchby=all&dup_remove=1&post_blogurl=&post_blogurl_without=&nso=from"+sd+"to"+ed+"&mson=0&start="+page
       result = requests.get(url)
       bs_obj = BeautifulSoup(result.content, "html.parser")
       return bs_obj
   def run(self):
       datevalue = self.get_data_date(self.keyword, self.sd, self.ed, "1")
       datevalue = int(datevalue/10)
       print(datevalue)
       cnt = 0
       for i in range(0,datevalue):
          page = str(i*10+1)
          time.sleep(2)
          bs_obj = self.get_bs_obj(self.keyword, self.sd, self.ed, page)
          lis = bs_obj.findAll("li",{"class":"sh_blog_top"})
          for li in lis:
              Title = li.find("a",{"class":"sh_blog_title"}).text
              datetimes = li.find("dd",{"class":"txt_inline"}).text
              short_body = li.find("dd",{"class":"sh_blog_passage"}).text
              main_url = li.find("a",{"class":"url"})
              main_url = main_url['href']
              print("ID:",self.ID)
              print("title: ", title)
              print("datetime: ", datetimes)
              print("short_body: ", short_body)
              print("main_url: ",main_url)
              Naver = naver()
              if self.k !="k":
                  self.keyword=""
              if self.b !="b":
                  short_body=""
              if self.d !="d":
                  datetimes=""
              if self.t !="t":
                  Title =""
              if self.url !="url":
                  main_url =""
              Naver.keyword = self.keyword
              Naver.nickname= self.ID
              contents = title(main_title=Title,
                               main_body=short_body,
                               datetime=datetimes,
                               media="naver_blog",
                               count="1")
              Naver.sub_body = contents
              Naver.main_url=main_url
              Naver.save()
              cnt = cnt+1
              print(cnt)
       Naver = naver_count()
       Naver.login_id=self.ID
       Naver.naver_count=cnt
       Naver.save()
       name = state1.objects.filter(id=self.number, type_state=1).order_by('-id').first()
       name.state= int(name.state) + cnt
       name.save()
       print("끝")