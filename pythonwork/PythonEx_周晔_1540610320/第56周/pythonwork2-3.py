# 使用yield，生成前小于100的斐波那契数列
 
 
# 求fibonacci数列的方法
def fibonacci(num):
    # 记录前面两个数
    a = 0
    b = 1
    # 设置限制斐波那契数列的条件
    condition = 0
    # 循环判断条件是否成立
    while condition <= num:
        result = a
        a, b = b, a+b    # 核心点
        condition=b
        yield result
    yield a
# 调用方法
fibo1 = fibonacci(100) # 生成器
print(fibo1)
 
# 使用for循环遍历生成器
for value in fibo1:
    print(value,end=' ')
