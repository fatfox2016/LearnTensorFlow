# -*- encoding=utf-8 -*-
import jieba
import re
from collections import Counter

#read file
with open('/tensorflow/Chap0/happiness.txt','r') as f:
    text = f.read()

#words segmentation
words = jieba.cut(text)
words = " ".join(words)
print type(words)

#get words list
list = re.split(r'\s+',words)
wordsList = []
for r in list:
    if re.match(u'([\u4e00-\u9fff]+)',r):
        wordsList.append(r)

#count word frequency
textList = Counter(wordsList)
top10 = textList.most_common(10)
for i in top10: 
    word = i[0]
    print word,i[1]