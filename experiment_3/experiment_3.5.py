import random

def Lottery():
    number = random.randint(1, 100) # 获取随机数
    return number

results = []
rounds = 3  # 抽奖轮数
print("你有三次抽奖机会:\n"
      "如果抽奖号码为1，则你将获得特等奖;\n"
      "如果抽奖号码在2至10之间（包括2和10）,则你将获得一等奖;\n"
      "如果抽奖号码在11至30之间（包括11和30）,则你将获得二等奖;\n"
      "如果抽奖号码在31至70之间（包括31和70）,则你将获得三等奖;\n"
      "如果抽奖号码是其他的数字，很遗憾你没有获奖.")

for i in range(rounds):
    result = Lottery()
    print("第{}次抽奖结果为：{}".format(i+1, result))
    if result == 1:
        print("特等奖")
    elif 2 <= result <= 10:
        print("一等奖")
    elif 11 <= result <= 30:
        print("二等奖")
    elif 31 <= result <= 70:
        print("三等奖")
    else:
        print("很遗憾，你未获奖")
    results.append(result)

print("抽奖结束，所有抽奖结果为：", results)
