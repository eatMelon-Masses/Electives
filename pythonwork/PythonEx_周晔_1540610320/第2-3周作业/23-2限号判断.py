import re,os,sys
num = input('请输入车牌号：')

str1 = num[-1]
if str1 == '1'or str1 == '6':
    print ("该车牌限号是星期一")
if str1 == '2'or str1 == '7':
    print ("该车牌限号是星期二")
if str1 == '3'or str1 == '8':
    print ("该车牌限号是星期三")
if str1 == '4'or str1 == '9':
    print ("该车牌限号是星期四")
if str1 == '5'or str1 == '0':
    print ("该车牌限号是星期五")
             
