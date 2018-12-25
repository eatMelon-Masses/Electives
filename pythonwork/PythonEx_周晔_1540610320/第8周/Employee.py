#coding:utf-8
class Employee:
    name = ''
    pay = 0
    def __init__(self,name,pay):
        self.name = name
        self.pay = pay
        
    def pay_raise(self, increase): #涨薪资
        self.pay = self.pay *(increase+1)

        
    def update_raise(self, pay): #修改薪资
        self.pay = pay
        print("修改后工资:",self.pay)

    def get_last_name(self): #获取姓
        if len(self.name)<=3:
            return self.name[0]
        else:
            return self.name[0:2]

        #测试
if __name__=="__main__":
    ZhangSan=Employee('张三',8000)
    print(ZhangSan.get_last_name())
    ZhangSan.pay_raise(0.1)
    print(ZhangSan.pay)
    Dongfangbubai=Employee('东方不败',5000)
    print(Dongfangbubai.get_last_name())
    Dongfangbubai.pay_raise(-0.2)
    print(Dongfangbubai.pay)
 

