

# Create your views here.
from django.shortcuts import render
from bs4 import BeautifulSoup
from django.http import JsonResponse
from django.http import HttpResponse
from operator import eq
from django.db.models import Q
from .models import state1,title,KBS,SBS,MBC,JTBC,YTN,dailyEconomy,moneyToday,eDaily,seoulEconomy,koreaEconomy,naver,Emoticon,word,news_count,naver_count,daum_count
from .models import Signup
from random import *
import time, threading
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from django.shortcuts import  redirect
from .forms import UserForm, LoginForm
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
from django.template import RequestContext
from django.views import View
from django.utils.encoding import python_2_unicode_compatible
from .signup import *
from .blogview import *
from .daum_blog import *
from .naver_blog import *
from .news import *
from .Analysis import *
import numpy as np
import pandas as pd
import datetime
import os
import sys
import json
import math
import requests
import django
import re
import csv,codecs
import uuid
from time import sleep
from .forms import DocumentForm
from importlib import import_module
from .models import Document
from django.conf import settings
#from konlpy.utils import pprint
from multiprocessing import Pool
from datetime import datetime
from django.core.paginator import Paginator
from django.template import loader
django.setup()
global BC8
def index(request):
    return render(request, 'agri_crawler/index.html',{})
def kmeans(request):
    return render(request, 'agri_crawler/kmeans.html',{})
def loading(request):
    return render(request, 'agri_crawler/loading.html',{})
def login(request):
    return render(request, 'agri_crawler/login.html',{})
def signup(request):
    return render(request, 'agri_crawler/signup.html',{})
def practice(request):
    return render(request, 'agri_crawler/practice.html',{})
def logout(request):
    request.session.flush()
    return render(request, 'agri_crawler/login.html',{})

def positive(request):
    keyword = request.POST.get('keyword')
    nickname = request.POST.get('nickname')
    print(keyword)
    print(nickname)
    daumblog= daum_blog.objects.filter(keyword= keyword, nickname=nickname)
    naverblog=naver.objects.filter(keyword=keyword,nickname=nickname)
    kbs = KBS.objects.filter(keyword=keyword,nickname=nickname)
    mbc = MBC.objects.filter(keyword=keyword,nickname=nickname)
    sbs = SBS.objects.filter(keyword=keyword,nickname=nickname)
    jtbc = JTBC.objects.filter(keyword=keyword,nickname=nickname)
    ytn = YTN.objects.filter(keyword=keyword, nickname=nickname)
    daily = dailyEconomy.objects.filter(keyword= keyword, nickname=nickname)
    money = moneyToday.objects.filter(keyword=keyword, nickname=nickname)
    eday = eDaily.objects.filter(keyword=keyword, nickname=nickname)
    seoul = seoulEconomy.objects.filter(keyword=keyword, nickname=nickname)
    korea = koreaEconomy.objects.filter(keyword=keyword, nickname=nickname)
    f = open('output.txt', 'w', encoding='utf-8')
    for i in daumblog:
       f.write(str(i.sub_body.main_body))
    for i in naverblog:
       f.write(str(i.sub_body.main_body))
    for i in kbs:
       f.write(str(i.sub_body.main_body))
    for i in mbc:
       f.write(str(i.sub_body.main_body))
    for i in sbs:
       f.write(str(i.sub_body.main_body))
    for i in jtbc:
       f.write(str(i.sub_body.main_body))
    for i in ytn:
       f.write(str(i.sub_body.main_body))
    for i in daily:
       f.write(str(i.sub_body.main_body))
    for i in money:
       f.write(str(i.sub_body.main_body))
    for i in eday:
       f.write(str(i.sub_body.main_body))
    for i in seoul:
       f.write(str(i.sub_body.main_body))
    for i in korea:
       f.write(str(i.sub_body.main_body))
    f.close()

    return render(request, 'agri_crawler/positive.html',{})
def bloglist(request): # 개인 블로그 수집 현황 파악
       name = request.POST.get('User')
       wating = state1.objects.filter(type_state=1, login_id=str(name))
       return render(request, 'agri_crawler/waiting.html',{'waiting':wating})
def newslist(request): # 개인 뉴스 수집 현황 파악
       name = request.POST.get('User')
       wating = state1.objects.filter(type_state=0, login_id=name)
       return render(request, 'agri_crawler/waiting1.html',{'waiting':wating})
def alllist(request):
       wating = state1.objects.all()
       return render(request, 'agri_crawler/waiting2.html',{'waiting':wating})
from django.core.mail import send_mail
def sendmail(request):
     name = request.POST.get('name')
     email = request.POST.get('email')
     message = request.POST.get('message') 
     send_mail(name, message, email, ['thdtdmgus0@gmail.com'], fail_silently=False)
     return render(request, 'agri_crawler/index.html')
def waiting(request): # 뉴스 
    text = request.POST.get('text1')
    start_date = request.POST.get('start_date1')
    end_date = request.POST.get('end_date1')
    KBS = request.POST.get('KBS')
    MBC = request.POST.get('MBC')
    SBS = request.POST.get('SBS')
    JTBC = request.POST.get('JTBC')
    YTN = request.POST.get('YTN')
    Daily = request.POST.get('daily')
    Money = request.POST.get('money')
    eDaily = request.POST.get('eDaily')
    seoul = request.POST.get('seoul')
    korea = request.POST.get('korea')
    title = request.POST.get('t')
    date = request.POST.get('d')
    keyword = request.POST.get('k')
    body =  request.POST.get('b')
    emoticon = request.POST.get('e')
    comment = request.POST.get('c')
    recommend = request.POST.get('r')
    ID = request.POST.get('id')
    now = datetime.now() 
    today_date = str(now.year)+"."+str(now.month)+"."+str(now.day)
    State1 = state1()
    State1.keyword = text
    State1.start_date = start_date
    State1.end_date = end_date
    State1.today_date = today_date
    State1.login_id=ID
    State1.state = 0
    State1.type_state=2
    State1.save()
    condition = State1.state
    query = state1.objects.filter(login_id= ID)
    waiting = query
    #page_row_count = 5 
    #page_display_count = 5 # 화면에 보이는 display 개수   
    Users = state1.objects.filter(login_id=ID)

    
    data={'start_date': start_date, 'end_date':end_date, 'title':title, 'date':date, 'keyword':text, 'body':body, 'emoticon':emoticon, 'comment':comment, 'recommend':recommend}
    return render(
              request,
              'agri_crawler/waiting1.html',
              {  
                'waiting':waiting,
                'data':data,
                'Users':Users
               }
          )
def wating(request): #블로그
    text1 = request.POST.get('text1')#키워드
    start_date = request.POST.get('start_date1') #시작기간
    end_date = request.POST.get('end_date1') #종료기간
    naver_blog = request.POST.get('naver')
    daum_blog = request.POST.get('daum')
    title = request.POST.get('t')
    date = request.POST.get('d')
    keyword = request.POST.get('k')
    body = request.POST.get('b')
    emoticon = request.POST.get('e')
    comment  = request.POST.get('c')
    recommend = request.POST.get('r')
    ID = request.POST.get('id')
    now = datetime.now()
    today_date = str(now.year)+"."+str(now.month)+"."+str(now.day)
    State1 = state1()
    State1.keyword = text1
    State1.start_date = start_date
    State1.end_date = end_date
    State1.today_date = today_date
    State1.login_id=ID
    State1.state = 0
    State1.type_state=3
    State1.save()
    query = state1.objects.filter(login_id = ID)
    waiting = query
    data = {'daum_blog':daum_blog,'naver_blog': naver_blog,'text1': text1,'start_date': start_date,'end_date': end_date, 'title':title,'date': date, 'keyword':keyword,'body': body, 'emoticon':emoticon, 'comment':comment,'recommend': recommend}
    return render(request, 'agri_crawler/waiting.html',{'waiting':waiting, 'data':data})
    #def negative(request): # 긍/부정 판단하게 하는 부분
    #positive=0
    #negative=0
    #neutral=0
    #f = open('result.txt', 'r', encoding='utf8')
    #lines = f.readlines()
    #for i,line in enumerate(lines):
    #   if i==0:
    #     kw = line
    #     continue
    #   elif '동영상' in line:
    #     continue
    #   elif 'function' in line:
    #     continue
    #   elif '//' in line:
    #     continue
    #   elif len(line.split())==0:
    #    continue
    #   sort = classfier()
    #   if sort.naive_classfier(str(line)) == 1:
    #      positive = positive+1
    #   elif sort.naive_classfier(str(line))==0:
    #      negative = negative+1
    #   elif sort.naive_classfier(str(line))==-1:
    #      neutral = neutral+1
    #f.close()
    #data = {'positive':positive, 'negative':negative, 'kw' :kw, 'neutral':neutral}
    #return render(request, 'vegetable/googlechartnegative.html',{'data':data})
def idcheck(request):
    id = request.POST.get('id',None)
    data ={
     'is_taken':Signup.objects.filter(ID=id).exists()
    }
    return JsonResponse(data)
#def identify(request):
#    cits = Signup.objects.all().filter(ID="송진현")
#    return render(request, 'vegetable/identify.html',{})
def d3(request):
    id = request.POST.get('id')
    print(id)
    keys =[]
    values = []
    query  = word.objects.filter(user_id = id).order_by('-value')[:10]
    for i in query:
        key =i.key
        keys.append(key)
        print(keys)
        value = int(i.value)
        values.append(value)
        print(values)
    json_keys = json.dumps(keys)
    return render(request,'agri_crawler/d3.html', {'keys':json_keys, 'values':values})
def auth_login(request):
    id = request.POST.get('username',None)
    password = request.POST.get('password',None)
    if id =="admin" and password=="1234":
      State_model = state1.objects.all()
      Admin = request.POST['username']
      request.session['admin']=Admin
      return render(request, 'agri_crawler/admin.html',{'State':State_model})
    else:
    #is_id = Signup.objects.filter(ID=id).exists()
    #is_password = Signup.objects.filter(password=password).exists()
     is_id = Signup.objects.filter(ID =id).exists()
     is_password = Signup.objects.filter(password = password).exists()
     data= {'username':is_id, 'password':is_password}
     if is_id == True and is_password == True:
       username = request.POST['username']
       password = request.POST['password']
       request.session['username'] = username
       return redirect('index')
     else:
       return redirect('login')
def complete(request):
     sign = signUp()
     ID = request.POST.get('ID')
     password = request.POST.get('Password')
     email = request.POST.get('email')
     sign.post(ID, password, email)
     return render(request, 'agri_crawler/login.html',{})
class url_collector:
   def __init__(self):
      self.req_header = {
                'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36'}
      
      self.url = "https://search.naver.com/search.naver?ie=utf8&where=news"
   def add_property(self, Str, point_start_date, point_end_date, start):
       self.param = {
                'query': Str.encode('utf-8').decode('utf-8'),
                    'sm':'tab_pge',
                    'sort': '2',
                    'photo':'0',
                    'field':'0',
                    'pd':'3',
                    'ds': point_start_date,
                    'de': point_end_date,
                    'nso': 'so:r,p:',
                    'start': str(10*start+1)
            }
       return self.param
def login_session():
    with requests.Session() as s:
        req = s.get("https://nid.naver.com/nidlogin.login")
        html = req.text
        header = req.headers
        status = req.status_code
        is_ok = req.ok
def processing():
    start_time  = time.time()
    pool = Pool(precesses=32)
    pool.map(tests)
    print(time.time()-start_time)
def task(request):
    return render(request, 'agri_crawler/waiting1.html')
def state_save(Str, start_date, end_date, ID, type):
    now = datetime.now()
    today_date = str(now.year) + "." + str(now.month) + "." + str(now.day)
    State1 = state1()
    State1.keyword = Str
    State1.start_date = start_date
    State1.end_date = end_date
    State1.today_date = today_date
    State1.login_id = ID
    State1.state = 0
    if type == 0:
        State1.type_state=0
    elif type == 1:
        State1.type_state=1
    else:
        State1.type_state=2
    State1.save()
def tests(request):
    if request.method =='POST':
          Str = str(request.POST.get('text1'))  
          start_date = request.POST.get('start_date1')
          end_date = request.POST.get('end_date1')
          start = start_date.replace("-","")
          end = end_date.replace("-","")
          title = request.POST.get('t')
          main_body = request.POST.get('b')
          date = request.POST.get('d')
          keyword = request.POST.get('k')
          emoticon = request.POST.get('e')
          comment = request.POST.get('c')
          recommend = request.POST.get('l') 
          ID = request.POST.get('id')
          media={}
          if request.POST.get('KBS') == "KBS":     
             media['kbs']=True
          else:
             media['kbs']=False
          if request.POST.get('MBC') == "MBC":
             media['mbc']=True
          else:
             media['mbc']=False
          if request.POST.get('SBS') == "SBS":
             media['sbs']=True
          else:
             media['sbs']=False
          if request.POST.get('JTBC') == "JTBC":
             media['jtbc']=True
          else:
             media['jtbc']=False
          if request.POST.get('YTN') == "YTN":
             media['ytn']=True
          else:
             media['ytn']=False
          if request.POST.get('daily') == "daily":
             media['daily']=True
          else:
             media['daily']=False
          if request.POST.get('money') == "money":
             media['money']=True
          else:
             media['money']=False
          if request.POST.get('eDaily') == "eDaily":
             media['eDaily']=True
          else:
             media['eDaily']=False
          if request.POST.get('seoul') == "seoul":
             media['seoul']=True
          else:
             media['seoul']=False
          if request.POST.get('korea') == "korea":
             media['korea']=True
          else:
             media['korea']=False
          state_save(Str, start_date, end_date, ID,0)
          query = state1.objects.filter(login_id=ID, type_state=0)
          waiting = query
          name = state1.objects.filter(login_id=ID).order_by('-id').first()
          number = name.id
          news_collector = news_crawler(Str, start, end, ID,media, title, main_body, date, keyword, emoticon, comment, recommend,number)
          news_collector.start()
          data = {'text1': Str,'start_date': start,'end_date': end, 'title':title,'date': date, 'keyword':Str,'body': main_body}
    return render(request,'agri_crawler/waiting1.html',{'waiting':waiting,'data':data})
def product(request):
    return render(request, 'agri_crawler/product_0818.html',{})
def navertest(request):
    global bkw
    if request.method == 'POST': # 만약 POST 방식으로 전달이 되었으면
        if request.POST.get('naver'):
          Str = str(request.POST.get('text1'))
          start_date =  request.POST.get('start_date1')
          end_date = request.POST.get('end_date1')
          start = start_date.replace("-","")
          end = end_date.replace("-","")
          title = request.POST.get('t')
          main_body = request.POST.get('b')
          date = request.POST.get('d')
          keyword = request.POST.get('k')
          url = request.POST.get('url')
          ID = request.POST.get('id')
          state_save(Str, start_date, end_date, ID,1)
          print(Str)
          query = state1.objects.filter(login_id=ID, type_state=1)
          number = state1.objects.filter(login_id=ID).order_by('-id').first()
          naver_collector = naver_crawler(Str,start,end,title,main_body,date,keyword,url,ID,number)
          naver_collector.start()
          data = {'text1': Str, 'start_date': start, 'end_date': end, 'title': title, 'date': date, 'keyword': Str,
                  'body': main_body}
          return render(request, 'agri_crawler/waiting.html',{'waiting':query, 'data':data})
        if request.POST.get('daum'):
          Str = str(request.POST.get('text1')) # 검색어
          bkw = Str
          start_date = request.POST.get('start_date1') # 시작시간
          end_date = request.POST.get('end_date1') # 도착시간
          start = start_date.replace("-","") # -을 제거     
          end  = end_date.replace("-","")
          title = request.POST.get('t')
          main_body = request.POST.get('b')  
          date = request.POST.get('d')   
          key = request.POST.get('k')
          tag = request.POST.get('tag')
          comment = request.POST.get('comment')
          ID = request.POST.get('id')
          state_save(Str, start_date, end_date, ID,1)
          print(Str)
          print(ID)
          query = state1.objects.filter(login_id=ID, type_state=1)
          name = state1.objects.filter(login_id=ID).order_by('-id').first()
          print(name.id)
          waiting = query
          daum_collector = daum_crawler(bkw,start,end,ID,title,main_body,datetime,key,tag,comment)
          daum_collector.start()
          data = {'text1': Str,'start_date': start,'end_date': end, 'title':title,'date': date, 'keyword':Str,'body': main_body}
          return render(request, 'agri_crawler/waiting.html', {'waiting':waiting, 'data':data})
def soup_text(text): # 하루치만
    url = "https://search.daum.net/search?w=social&m=web&sort_type=socialweb&nil_search=btn&DA=STC&enc=utf8&q="+str(text)
    html = requests.get(url)
    soup = BeautifulSoup(html.content, "html.parser")
    return soup
def other_soup_text(text, nickname, content, time, ID):
    today = datetime.now()
    yesterday_day = today.day-1
    if yesterday_day<1:
        yesterday_day=31
    today_mon=today.month
    today_day=today.day
    today_hour=today.hour
    today_min=today.minute
    today_sec=today.second
    if today.month>=1 and today.month<10:
        today_mon = "0"+str(today.month)
    if today.day >=1 and today.day<10:
        today_day = "0"+str(today.day)
    if today.hour >=1 and today.hour<10:
        today_hour ="0"+str(today.hour)
    Today= str(today.year)+str(today_mon)+str(today.day)+str(today.hour)+str(today.minute)+str(today.second)
    yesterday = str(today.year)+str(today_mon)+str(yesterday_day)+str(today.hour)+str(today.minute)+str(today.second)
    print(Today)
    print(yesterday)
    url = "https://search.daum.net/search?w=social&m=web&sort_type=socialweb&nil_search=btn&DA=STC&enc=utf8&q="+str(text)+"&period=d&sd="+str(yesterday)+"&ed="+str(Today)
    html = requests.get(url)
    soup = BeautifulSoup(html.content, "html.parser")
    div_list = soup.findAll("div",{"class":"box_con"})
    for list in div_list:
        id = list.find("div",{"class":"wrap_tit"}).text
        content = list.find("span",{"class":"f_eb desc content_link"}).text
        time = list.find("span",{"class":"f_nb"}).text
        print(id)
        print(content)
        twitter_value = Twitter()
        if nickname !="nickname":
            id=""
        if content != "content":
            content=""
        if time != "time":
            time=""
        twitter_value.userId=ID
        twitter_value.id=id
        twitter_value.content=content
        twitter_value.time = time
        twitter_value.save()

def twitter(request):
    text = request.POST.get('text2')
    one_day =request.POST.get('one_day')
    all = request.POST.get('all')
    nickname = request.POST.get('nickname')
    content = request.POST.get('content')
    time = request.POST.get('time')
    ID= request.POST.get('id')
    print(ID)
    cnt= 0
    if all == "all":
        soup = soup_text(text)
        div_list = soup.findAll("div", {"class": "box_con"})
        for list in div_list:
            id = list.find("div", {"class": "wrap_tit"}).text
            content = list.find("span",{"class","f_eb desc content_link"}).text
            time = list.find("span",{"class":"f_nb"}).text
            twitter_value = Twitter()
            if nickname !="nickname":
               id= ""
            if content !="content":
               content=""
            if time !="time":
               time=""
            twitter_value.userId= ID
            twitter_value.Id = id
            twitter_value.content=content
            twitter_value.time= time
            twitter_value.save()
            cnt = cnt+1
            state_save(text, 1,1,ID,2)
            query = state1.objects.filter(login_id=ID, type_state=2)
    elif one_day == "one_day":
        other_soup_text(text, nickname, content, time, ID)
    name = state1.objects.filter(login_id=ID).order_by('-id').first()
    name.state = int(name.state) + cnt
    name.save()
    return render(request, 'agri_crawler/twitter.html',{'waiting':waiting})
def twitterlist(request):
    return render(request, 'agri_crawler/twitter.html',{'waiting':waiting})
from .models import Twitter
def admin(request):
    State_model = state1.objects.all()
    request.session['admin'] = "admin"
    daum_num = daum_blog.objects.all().count()
    naver_num = naver.objects.all().count()
    kbs_num = KBS.objects.all().count()
    mbc_num = MBC.objects.all().count()
    sbs_num = SBS.objects.all().count()
    jtbc_num = JTBC.objects.all().count()
    ytn_num = YTN.objects.all().count()
    money = moneyToday.objects.all().count()
    seoul = seoulEconomy.objects.all().count()
    edaily = eDaily.objects.all().count()
    korea = koreaEconomy.objects.all().count()
    every = dailyEconomy.objects.all().count()
    twit = Twitter.objects.all().count()
    return render(request,
                  'agri_crawler/admin.html',
                  {'State':State_model,
                   'daum':daum_num,
                   'naver':naver_num,
                   'kbs':kbs_num,
                   'mbc':mbc_num,
                   'sbs':sbs_num,
                   'jtbc':jtbc_num,
                   'ytn':ytn_num,
                   'money':money,
                   'seoul':seoul,
                   'edaily':edaily,
                   'korea':korea,
                   'every':every,
                   'twit':twit
                   })
def analysis(request):
    Bayes = BayesianFilter()
    total_sentence = 0
    print(total_sentence)
    username = request.POST.get('id')
    print(username)
    f = open('output.txt', 'r', encoding='utf-8')
    rline = f.readlines() # 전체 텍스트 읽어오기
    tline = f.read()
    for i in rline:
        print("기사:", i[:-1])
    results_list = Bayes.split(tline)
    all_count = Bayes.all_count(results_list)
    print(all_count)
    for key, value in all_count.items():
       Word = word()
       Word.user_id = username
       Word.key = key
       Word.value=value
       Word.save()
    return render(request, 'agri_crawler/product_0818.html',{})
def PNjudgment(request):
    Bayes = BayesianFilter()
    username = request.POST.get('id')
    print(username)
    f = open('output.txt', 'r', encoding='utf-8')
    while True:
        line = f.readline()
        print(line)
        if not line:
            break
        results_list = Bayes.split(line)
        print(results_list)
    Fit(Bayes)
    return render(request, 'agri_crawler/product_0818.html', {})
def Fit(Bayes):
    positive_read = open('positive1.txt', 'r', encoding='utf-8')
    negative_read = open('negetive.txt', 'r', encoding='utf-8')
    neutral_read = open('neutral.txt', 'r', encoding='utf-8')
    positive_data = positive_read.read()
    positive_list = Bayes.split(positive_data)
    for data in positive_list:
        Bayes.fit(data, "긍정")
    negative_data = negative_read.read()
    negative_list = Bayes.split(negative_data)
    for data in negative_list:
        Bayes.fit(data, "부정")
    neutral_data = neutral_read.read()
    neutral_list = Bayes.split(neutral_data)
    for data in neutral_list:
        Bayes.fit(data, "중립")
def blog_result(request):
    login_id = request.POST.get('login_id')
    id = request.POST.get('id')
    count1 = 0
    count2 = 0
    naver = naver_count()
    daum = daum_count()
    value = naver.objects.filter(login_id=login_id).order_by('-id').first()
    value.id = id
    count1 = value.naver_count
    value.save()
    value2 = daum.objects.filter(login_id=login_id).order_by('-id').first()
    value2.id = id
    count2 = value2.daum_count
    print(login_id)
    print(id)
    return render(request, 'agri_crawler/chart_blog.html',{'naver_count':value, 'daum_count':value2})
def news_result(request):
    login_id = request.POST.get('login_id')
    id = request.POST.get('id')
    keyword =request.POST.get('keyword')
    total = state1.objects.filter(login_id=login_id, id=id, type_state=0)
    for i in total:
        total_number = i.state
    print(keyword)
    query = news_count.objects.filter(login_id=login_id, id = int(id)-270)
    kbs=''
    mbc=''
    sbs=''
    jtbc=''
    ytn=''
    money=''
    edaily=''
    korea=''
    economy=''
    seoul=''
    for i in query:
        kbs = i.kbs_count
        mbc = i.mbc_count
        sbs = i.sbs_count
        jtbc = i.jtbc_count
        ytn = i.ytn_count
        money = i.money_count
        edaily = i.edaily_count
        korea = i.korea_count
        economy = i.dailyeconomy_count
        seoul = i.seouleconomy_count
    return render(request, 'agri_crawler/solution.html',{'kbs':kbs
                                                               ,'mbc':mbc,
                                                               'sbs':sbs,
                                                               'jtbc':jtbc,
                                                               'ytn':ytn,
                                                               'money':money,
                                                               'edaily':edaily,
                                                               'korea':korea,
                                                               'economy':economy,
                                                               'seoul':seoul,
                                                               'keyword':keyword,
                                                               'total_number':total_number,
                                                                })
def twitter_result(request):
    return render(request, 'agri_crawler/twitter_result.html',{})

