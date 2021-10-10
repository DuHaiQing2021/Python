'''
房贷计算器
'''

# 选择贷款类型
goods = int(input("请选择贷款类型：（1商业贷款 or 2公积金贷款）>>>"))

# 输入借款金额
loanMoney = int(input("请输入贷款金额：（单位：/万）>>>"))

# 输入贷款期限
loanTime = int(input("请输入贷款期限：（单位：/年）>>>"))

# 请输入还款月数
repayTime =int(input("请输入还款月数：（单位：/月）>>>"))

# 判断贷款利率
loanRate = 0.0
if goods == 1:
    if loanTime <= 5:
        loanRate = 4.75/100
    else:
        loanRate = 4.90/100
elif goods == 2:
    if loanTime <= 5:
        loanRate=2.75/100
    else:
        loanRate=3.25/100
print("该贷款类型的年利率为：", loanRate*100, '%')
print("-----------—----------计算后------------------------")

# 计算每月月供
Repayment = (loanMoney*10000)*(loanRate/12*(1+loanRate/12)**repayTime)/((1+loanRate/12)**repayTime-1)
print("每月需要还款的金额为：(单位：/元)>>>%.2f"%Repayment)

# 需要还款总额
RepayMoney = Repayment*loanTime*12
print("需要还款的总金额为：（单位：/元）>>> %.2f"%RepayMoney)

# 需要支付的利息
repayRate = RepayMoney - loanMoney*10000
print("需要支付的利息为：（单位：/元）>>>%.2f"%repayRate)
