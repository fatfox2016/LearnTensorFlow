
# coding: utf-8


# In[18]:


import jieba
import re
from collections import Counter


# In[1]:

#read file
with open('/tensorflow/Chap0/happiness.txt','r') as f:
    text = f.read()


# In[3]:

import jieba
#words segmentation
words = jieba.cut(text)
words = " ".join(words)
print type(words)


# In[6]:

import re
#get words list
list = re.split(r'\s+',words)
wordsList = []
for r in list:
    if re.match(u'([\u4e00-\u9fff]+)',r):
        wordsList.append(r)


# In[10]:

from collections import Counter
#count word frequency
textList = Counter(wordsList)
top10 = textList.most_common(10)
for i in top10: 
    word = i[0]
    woer = word
    print word,i[1]


# In[ ]:



