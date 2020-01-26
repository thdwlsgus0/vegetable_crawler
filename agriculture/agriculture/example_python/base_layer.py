rom bayes import BayesianFilter
from practice_bayes import Bayes
bf = BayesianFilter()

# 텍스트 학습
bf.fit("쿠폰 선물 & 무료 배송", "광고")
print(bf.category_dict)
print(bf.word_dict)
print(bf.words)
print("-=-=-=-=-=-=-=-=-=-=")

# 예측
pre, scorelist = bf.predict("재고 정리 할인, 무료 배송")
print("결과 = ", pre)
print(scorelist)