# twitter를 사용해야할 것 같음.
from konlpy.tag import Twitter
file = open("output.txt","r",encoding="utf-8")
twitter = Twitter()
word_dic = {}
line = file.read()
lines = line.split("\r\n") #한줄한줄 분할
for line in lines:
    malist = twitter.pos(line)
    print(malist)
    for taeso,pumsa in malist:
        if pumsa == "Noun":
            if not (taeso in word_dic):
                word_dic[taeso]=0
            word_dic[taeso]+=1
keys = sorted(word_dic.items(), key=lambda x:x[1], reverse=True)
for word, count in keys[:50]:
    print("{0}({1}) ".format(word, count), end="")
print(word_dic)




