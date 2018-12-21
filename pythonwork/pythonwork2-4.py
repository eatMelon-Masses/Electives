s = "Sorting1234"
 
def sort_str(x):     # x 传入的每个元素
    if x.isdigit():
        if int(x) % 2 == 0:
            return (0,x)    # 返回的是元祖，元祖可进行排序
        return (1,x)
    elif x.islower():
        return (4,x)
    elif x.isupper():
        return (3,x)
 
li = sorted(s,key=sort_str)
#print(li)
# ['g', 'i', 'n', 'o', 'r', 't', 'S', '1', '3', '2', '4']
string = ''.join(li)
print(string)
# ginortS1324