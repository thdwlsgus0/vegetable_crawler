"""from konlpy.tag import *
from konlpy.utils import pprint
from konlpy.tag import Okt
class classfier():
    def __init__(self):
       self.positive = 0
       self.negative = 0
       self.list_positive = []
       self.list_negetive = []
       self.list_neutral = []
    def getting_list(self, filename, listname):
        okt = Okt()
        while 1:
          line = filename.readline()
          Str = str(line)
          line_parse = okt.morphs(Str)
          for i in line_parse:
                 listname.append(i)
          if not line:
              break
        return listname
    def naive_bayes_classifier(self,test, train, all_count):
        counter = 0
        list_count = []
        for i in test:
           for j in range(len(train)):
             if i == train[j]:
                counter = counter + 1
           list_count.append(counter)
           counter = 0
        list_naive = []
        for i in range(len(list_count)):
            list_naive.append((list_count[i]+1)/float(len(train)+all_count))
        result = 1
        for i in range(len(list_naive)):
           result *= float(round(list_naive[i], 6))
        return float(result)*float(1.0/3.0)
    def naive_classfier(self, text_line):
       f_pos = open('positive1.txt','r')
       f_neg = open('negetive.txt','r')   
       f_neu = open('neutral.txt','r')   
       okt = Okt()
       input_kkma = okt.morphs(str(text_line)) # 형태소 별로 토큰화
       test_output = []
       for i in input_kkma:
               test_output.append(i)
       list_pos = self.getting_list(f_pos,self.list_positive)
       list_neg = self.getting_list(f_neg,self.list_negetive)
       list_neu = self.getting_list(f_neu,self.list_neutral) 
       ALL = len(list_pos)+len(list_neg)+len(list_neu)
       result_pos = self.naive_bayes_classifier(test_output, list_pos, ALL)
       result_neg = self.naive_bayes_classifier(test_output, list_neg, ALL)   
       result_neu = self.naive_bayes_classifier(test_output, list_neu, ALL)
       if result_pos>result_neg and result_pos>result_neu:
           return 1
       elif result_pos<result_neg and result_neu<result_neg:
           return 0
       else:
           return -1 """
                
        
