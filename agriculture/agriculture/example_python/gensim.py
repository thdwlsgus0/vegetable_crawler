from gensim.models import Word2Vec
from konlpy.tag import Twitter


file = open("output.txt", "r", encoding="utf-8")
line = file.read()
lines = line.split("\r\n")
results = []
twitter = Twitter()
for line in lines:
    r = []
    malist = twitter.pos(line, norm=True, stem=True)
    for (word, pumsa)  in malist:
        if not pumsa in ["Josa", "Eomi", "Punctuation"]:
            r.append(word)
    results.append((" ".join(r)).strip())
output = (" ".join(results)).strip()
with  open("toji.wakati", "w", encoding="utf-8") as fp:
    fp.write(output)
data = word2vec.LineSentence("toji.wakati") # 어떤 문장들을 넣어서 분리
model = word2vec.Word2Vec(data, size=200, window=10, hs=1 , min_count=2, sg=1)
model.save("toji.model")
