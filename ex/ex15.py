# _*_ coding: utf-8 _*_
from sys import argv 
#从sys模块modules中使用argv函数function
script,filename = argv 
#使用函数argv将参数带入脚本
txt = open(filename) 
#打开参数文档
print "Here's your file %r:" % filename 
#显示文本
print txt.read() #读取文件并显示出来
txt.close()
# print "Type the filename again:" #提示输入文件名
# file_again = raw_input(">") #获取输入文件名
# txt_again = open(file_again) #打开输入文件名文档
# print txt_again.read() #读取文件并显示出来
# txt_again.close()
