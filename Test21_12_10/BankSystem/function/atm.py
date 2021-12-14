import random

from BankSystem.function.user import User
from BankSystem.function.card import Card


class ATM:
    def __init__(self,alluser):
        self.alluser=alluser

    def randomiCardId(self):
        while True:
            date=''  #存储卡号
            for i in range(6):  #随机生成6位卡号
                ch=chr(random.randrange(ord('0'),ord('9')+1))
                date+=ch
            if not self.alluser.get(str): #判断卡号是否重复
                return date
    def creatUser(self):
        name=input("请输入姓名：")
        Uid=input("请输入身份证号：")
        phone=input("请输入手机号：")
        prestMoney=float(input("请输入金额："))
        if prestMoney <= 0:
            print("输入有误")
            return -1
        oncePwd=input("请输入密码：")
        passWord=input("请再次确认密码：")
        if passWord != oncePwd:
            print("两次输入的密码不一致......")
            return -1
        print("密码设置成功，您的密码：%s" %passWord)
        cardId=self.randomiCardId()
        card=Card(cardId,oncePwd,prestMoney)
        user=User(name,Uid,phone,card)
        self.alluser[cardId] =user
        print("您的开户已完成，您的账号：%s"%cardId)

    def checkpwg(self,realPwd):
        for i in range(3):
            psd2=input("请输入密码：")
            if realPwd==psd2:
                return True
        print("密码输入错三次，系统自动退出......")
        return False
    def lockCard(self):
        inptcardId=input("请输入您的卡号：")
        user=self.alluser.get(inptcardId)
        if not self.alluser.get(inptcardId):
            print("此卡号不存在,锁定失败！")
        if user.card.cardLock:
            print("该卡已经被锁定，无需再次锁定！")
            return -1
        if not self.checkpwg(user.card.cardPwd):
            print("密码错误，锁定失败！！")
            return -1
        user.card.cardLock=True
        print("该卡锁定成功！")
    def searchUser(self):
        inptcardId=input("请输入您的卡号：")
        user =self.alluser.get(inptcardId)
        if not user:
            print("此卡号不存在！")
            return -1
        if user.card.cardLock:
            print("该用户已经被锁定，请解卡后使用！")
            return -1
        if not self.checkpwg(user.card.cardPwd):
            print("密码错误过多,卡已经被锁定，请解卡后使用")
            user.card.cardLock=True
            return -1
        print("账户：%s 余额：%.2f"%(user.card.cardId,user.card.money))
        return user
    def getMoney(self):
        userTF=self.searchUser()
        if userTF !=-1:
            if userTF.card.cardId != '':
                inptMoney=float(input("请输入取款金额："))
                if inptMoney>int(userTF.card.money):
                    print("取款的金额大于余额，请先查询余额！")
                    return -1
                userTF.card.money=float(userTF.card.money)-inptMoney
                print("取款成功！ 账户：%s 余额：%.2f "%(userTF.card.cardId,userTF.card.money))
        else:
            return -1
    def saveMoney(self):
        userTF=self.searchUser()
        if userTF != -1:
            if not userTF.card.cardLock==True:
                if userTF.card.cardId !='':
                    inptMoney=float(input("请输入要存入得金额："))
                    if inptMoney<0:
                        print("存入金额低于0，存入失败")
                    else:
                        userTF.card.money+=inptMoney
                        print("存款成功！ 账户：%s  余额：%.2f"%(userTF.card.cardId,userTF.card.money))
            else:
                return -1
    def unlockCard(self):
        while 1:
            inptcardId = input("请输入您得卡号：")
            user = self.alluser.get(inptcardId)
            if not self.alluser.get(inptcardId):
                print("此卡号不存在，解锁失败！")
                return -1
            elif not user.card.cardLock:
                print("该卡未被锁定，无需解锁！")
                break
            elif not self.checkpwg(user.card.cardPwd):
                print("密码错误，解锁失败")
                return -1
            user.card.cardLock = False
            print("该卡解锁成功")
            break



