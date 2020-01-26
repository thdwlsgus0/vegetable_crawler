import math,sys
from konlpy.tag import Twitter

class Bayes:
    def __init__(self):
        self.words = set() #,출현한 단어 기록
        self.word_dict = {} # 카테고리마다 출현 횟수 기록
        self.category_list = {} # 카테고리 출현 횟수 기록
    # 형태소 분석하기
    def split(self, text):
        results = []
        twitter = Twitter()
        malist = twitter.pos(text, norm=True, stem=True)
        for word in malist:
            if not word[1] in ["Josa", "Eomi","Punctuation"]:
                results.append(word[0])
        return results

