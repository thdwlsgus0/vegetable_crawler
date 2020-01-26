import math, sys
from konlpy.tag import Twitter

class BayesianFilter:
    """ 베이지안 필터 """
    def __init__(self):
        self.words= set() # 출현한 단어 기록
        self.word_dict = {} # 카테고리마다의 출현 횟수 기록
        self.category_dict = {} #카테고리 출현 횟수 기록
        self.word_count={} #각각의 워드 카운트 기록
    def split(self, text):
        results = []
        twitter = Twitter()
        malist = twitter.pos(text, norm=True, stem=True)
        for word in malist:
           if not word[1] in ["Josa","Eomi","Punctuation"]:
               results.append(word[0])
        return results
    def all_count(self, text):
        word_list = text
        for word in word_list:
           if not word in self.word_count:
               self.word_count[word] = 1
           else:
               self.word_count[word] += 1
        return self.word_count
    def inc_word(self, word, category):
        if not category in self.word_dict:
            self.word_dict[category]={}
        if not word in self.word_dict[category]:
            self.word_dict[category][word]=0
        self.word_dict[category][word]+=1
        self.words.add(word)
    def inc_category(self,category):
        if not category in self.category_dict:
            self.category_dict[category]=0
        self.category_dict[category]+=1
    def fit(self, text, category):
        """ 텍스트 학습 """
        word_list = self.split(text)
        print(word_list)
        for word in word_list:
            self.inc_word(word, category)
        self.inc_category(category)
        print(self.category_dict)
        print(self.word_dict)