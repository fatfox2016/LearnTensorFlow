
import re
def getText(fileName):
    '''获取文档内容'''
    with open(fileName,'r',encoding = "utf8") as file:
      text = file.read()   #输出文档
    return text

def getTextList(fileName):
    '''以空格区分，获得列表'''
    t = getText(fileName)  #'text.txt'
    initList = re.split(r'\s+',t)
    list = []
    for r in initList:
        if re.match(u'([\u4e00-\u9fff]+)',r):
            list.append(r)
    # print(list)
    return list

def BinaryPhrase(fileName):
    '''获得二元词组'''
    list=[]
    initList = getTextList(fileName)
    countListlen = len(initList)
    n = countListlen

    for n in range(countListlen):
        l = initList[n-2] + ' ' + initList[n-1]
        list.append(l)
        n = n-1
    # print(list)
    return list

def countDict(fileName):
    '''记录词频输出到字典，key为词组，value为次数'''
    dict = {}
    initList = BinaryPhrase(fileName)
    for r in initList:
        if r not in dict:
            dict[r] = 1
        else:
            dict[r] = dict[r] + 1

    # print(dict)
    return dict

def sort_by_value(fileName):
    dict = countDict(fileName)
    items=dict.items()
    backitems=[[v[1],v[0]] for v in items]
    backitems.sort()

    return backitems #[ backitems[i][1] for iew in range(0,len(backitems))]

result = sort_by_value('text.txt')
lenR = len(result) 
r = result[lenR-10:lenR] #取10个词频最高的二元词组
print(r)