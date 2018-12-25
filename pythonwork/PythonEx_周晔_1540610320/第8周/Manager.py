#coding:utf-8
class Manager:
    name = ''
    pay = 0
    level = '初级'
    def __init__(self,name,pay,level):
        self.name = name
        self.pay = pay
        self.level = level
        
    def pay_raise(self, increase): #涨薪资
        if self.level == '初级':
            self.pay = self.pay*(increase+1)+500
        if self.level == '高级':
            self.pay = self.pay*(increase+1)+1000

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
    LiSi=Manager('李四',12000,"初级")
    print(LiSi.get_last_name())
    LiSi.pay_raise(0.3)
    print(round(LiSi.pay))
    WangWu=Manager('王五',15000,"高级")
    print(WangWu.get_last_name())
    WangWu.pay_raise(0.2)
    print(round(WangWu.pay))

 

