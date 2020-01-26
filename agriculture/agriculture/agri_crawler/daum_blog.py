from bs4 import BeautifulSoup
import requests, threading
import time # 시간을 주기 위함
from .models import title ,daum_blog, Emoticon, state1, daum_count # mongodb에 넣기 위함

class daum_crawler(threading.Thread):    # 페이지 
   def __init__(self,keyword, sd,ed,ID,t,b,d,k,tag,comment):
       threading.Thread.__init__(self)
       self.keyword = keyword
       self.sd = sd
       self.ed = ed
       self.ID = ID
       self.t = t
       self.b = b
       self.d = d
       self.k = k
       self.tag =tag
       self.comment =comment
   def get_bs_obj(self, keyword, sd, ed, page): # url 얻고 beautifulsoup 객체 얻을때 사용
       url ="https://search.daum.net/search?DA=STC&ed="+ed+"235959"+"&enc=utf8&https_on=on&nil_search=btn&q="+keyword+"&sd="+sd+"000000"+"&w=blog&period=u"+"&page="+page
       result = requests.get(url)
       bs_obj = BeautifulSoup(result.content, "html.parser")
       return bs_obj
   def get_bs_incontent(self, url): # 내부 콘텐츠 출력
       result = requests.get(url)
       bs_obj = BeautifulSoup(result.content, "html.parser")
       return bs_obj
   def get_data_date(self, keyword, sd, ed,page): # 총 몇 건인지 출력해줌
    bs_obj =  self.get_bs_obj(keyword, sd, ed,page)
    total_num = bs_obj.find("span",{"class":"txt_info"})
    total_text = total_num.text
    split = total_text.split()
    length = len(split)
    if length == 4:
        text = split[3].replace(",", "")
        text = text.replace("건", "")
    else:
        text = split[2].replace(",", "")
        text = text.replace("건", "")
    text = int(text)
    return text
   def run(self):
    datevalue = self.get_data_date(self.keyword, self.sd,self.ed,"1")
    print(datevalue)
    datevalue = int(datevalue/10)
    cnt=0
    for i in range(1,datevalue):
       page = str(i)
       bs_obj = self.get_bs_obj(self.keyword, self.sd, self.ed, page)
       a_url = bs_obj.findAll("a",{"class":"f_url"})
       for i in range(0,len(a_url)):
          li = a_url[i]['href']
          if "brunch" in li:
               time.sleep(2) # 시간 2초로 잡아놓음
               bs_obj = self.get_bs_incontent(li)
               Title = bs_obj.find("h1",{"class":"cover_title"}).get_text() # 제목
               print(Title)
               body = bs_obj.find("div",{"class":"wrap_body"}).get_text() # 본문
               times = bs_obj.find("span",{"class":"f_l date"}).get_text() # 기간
               tags = bs_obj.findAll("ul",{"class":"list_keyword"})
               tag_list=""
               comment = bs_obj.find("span",{"class":"txt_num"}).text
               comment_list=""
               if comment == '':
                   comment=0
               else:
                   comment=int(comment)
               print("comment_value:",comment)
               if comment >0:
                 comment_list  = comment_collector(li)
               for tag in tags:
                 tag_text = tag.text
                 print(tag_text)
                 tag_list +=tag_text
                 tag_list.rstrip()
               daum_Blog = daum_blog()
               if self.k != "k":
                  self.keyword = ""
               if self.b != "b":
                  body = ""
               if self.d != "d":
                  times = ""
               if self.t != "t":
                  Title = ""
               if self.tag != "tag":
                  tag_list= ""
               if self.comment !="comment":
                  comment_list=""
               daum_Blog.keyword = self.keyword
               daum_Blog.nickname=self.ID
               contents = title(main_title = Title,
                                main_body= body,
                                datetime=times,media="daum_blog",count=1)
               daum_Blog.sub_body = contents
               daum_Blog.tag = tag_list
               daum_Blog.comment = comment_list
               daum_Blog.save()
               cnt = cnt+1
               print(cnt)
    Daum_count = daum_count()
    Daum_count.login_id=self.ID
    Daum_count.daum_count=cnt
    Daum_count.save()
    name = state1.objects.filter(login_id = self.ID, type_state=1).order_by('-id').first()
    name.state = int(name.state) + cnt
    name.save()

def comment_collector(li):
    from selenium import webdriver
    from bs4 import BeautifulSoup
    from selenium.webdriver.common.keys import Keys

    driver = webdriver.Chrome('C:/Users/thdwlsgus0/Desktop/chromedriver_win32/chromedriver.exe')
    # driver = webdriver.PhantomJS('C:/Users/thdwlsgus0/Desktop/phantomjs-2.1.1-windows/phantomjs-2.1.1-windows/bin/phantomjs.exe')
    driver.implicitly_wait(3)
    driver.get('https://logins.daum.net/accounts/loginform.do?')
    driver.find_element_by_name('id').send_keys('thdwlsgus10')
    driver.find_element_by_name('pw').send_keys('operwhe123!')
    driver.find_element_by_xpath("//button[@class='btn_comm']").click()
    driver.get(li)
    html = driver.page_source
    soup = BeautifulSoup(html,'html.parser')
    notices = soup.findAll("p",{"class":"desc_comment"})
    comment_list=""
    for comment_div in notices:
        value = comment_div.text
        print("value: ", value)
        comment_list += value
    return comment_list

