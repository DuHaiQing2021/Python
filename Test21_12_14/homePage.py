from admin import Admin
from atm import ATM
import time
class HomePage:
    def __init__(self):
        self.allUserD={}
        self.atm=ATM(self.allUserD)
        self.admin=Admin()
    def saveUser(self):
        self.allUserD.update(self.atm.alluser)
        print("数据保存成功")
    def main(self):
        self.admin.printAdminView()
        ret=self.admin.adminOption()
        if not ret:
            while True:
                self.admin.printsysFunctionView()
                option=input("请输入您得操作：")
                if option not in("1","2","3","4","5","6","Q","q","A"):
                    print("输入操作项有误，请仔细确认！")
                    time.sleep(2)
                if option=="1":
                    self.atm.creatUser()
                elif option=="2":
                    self.atm.searchUser()
                elif option=="3":
                    self.atm.getMoney()
                elif option=="4":
                    self.atm.saveMoney()
                elif option=="5":
                    self.atm.unlockCard()
                elif option=="6":
                    self.atm.lockCard()
                elif option=="Q" or option=="q":
                    if not (self.admin.adminOption()):
                        self.saveUser()
                        print("退出系统")
                elif option=="A":
                    self.saveUser()
                    for i in self.allUserD:
                        print("账号：{}\t手机号：{}\t身份证号：{}".format(i,self.allUserD[i].phone,self.allUserD[i].id))