import re,os,sys

#回文判断
def isPalindrome(s):
    if len(s) < 2: 
        return True
    if s[0]!=s[-1]: 
        return False
    return isPalindrome(s[1:-1]) 

for num in range(100000,999999):
    str11=str(num)
    if isPalindrome(str11[2:]):
        num = num+1
        str22=str(num)
        if isPalindrome(str22[1:]):
             num = num+1
             str33=str(num)
             if isPalindrome(str33[1:5]):
                 num=num+1
                 str44=str(num)
                 if isPalindrome(str44):
                     num=num-3
                     print ("里程数：",num)
             
