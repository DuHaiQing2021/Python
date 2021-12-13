class Admin:
    adminU="123" #管理员账号
    adpwd="123" #管理员密码
    def printAdminView(self):
        print("**************************")
        print("***                    ***")
        print("***   欢迎登录银行系统   ***")
        print("***                    ***")
        print("**************************")
    def printsysFunctionView(self):
        print("********************************")
        print("***                          ***")
        print("***   1.开户(1)   2.查询(2)   ***")
        print("***   3.取款(3)   4.存款(4)   ***")
        print("***   5.解锁(5)   6.锁定(6)   ***")
        print("***   7.退出(Q)               ***")
        print("***                          ***")
        print("********************************")
    def adminOption(self):
        adminInput=input("请输入管理员账户：")
        if self.adminU != adminInput:
            print("管理员账号输入错误......")
            return -1
        adpwdInput=input("请输入管理员密码：")
        if self.adpwd != adpwdInput:
            print("管理员密码输入错误......")
            return -1
        else:
            print("操作成功，请稍后......")
            return 0