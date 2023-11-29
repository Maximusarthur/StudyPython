import random

class BankAccount:
    interest_rate = 0.04  # 类变量，利率设为0.04

    def __init__(self, username, id_number, password, balance):
        self.username = username  # 实例变量，用户名
        self.id_number = id_number  # 实例变量，身份证号
        self.password = password  # 实例变量，密码
        self.balance = balance  # 实例变量，存款数量

    def display_interest_rate(self):
        updated_rate = BankAccount.interest_rate + 0.01  # 增加1个百分点后的利率
        print("增加后的利率:", updated_rate)

    def change_password(self, new_password):
        self.password = new_password  # 修改实例的密码
        print("密码修改成功")

    def generate_transaction_number(self):
        transaction_number = random.randint(10000, 99999)  # 生成交易单号
        return transaction_number

    def deposit(self, amount):
        self.balance += amount  # 存款逻辑，将存款金额加到原有存款上
        if self.balance > 1000000:
            BankAccount.interest_rate += 0.02  # 如果存后账上余额大于100万，提高存款利率2%
        print("存款成功.当前余额:", self.balance)

    def check_creditworthiness(self):
        if self.balance >= 500000:  # 根据存款判断用户的偿付能力
            print("支持分期付款.")
        else:
            print("不符合分期付款条件.")


account = BankAccount("John", "1234567890", "password123", 500000)  # 开户
account.display_interest_rate()  # 显示利率
account.change_password("666666666")  # 修改密码
transaction_number = account.generate_transaction_number()  # 生成交易单号
print("交易单号:", transaction_number)
account.deposit(200000)  # 存款
account.check_creditworthiness()  # 判断信用能力
