# 编写程序用Print语句输出2000年至2500年间的所有闰年，要求每行输出8个
i = 0
for y in range(2000, 2500):  # 统计范围
    if y % 4 == 0 and y % 100 != 0:  # 闰年条件
        print(y, end=" ")
        i = i + 1
        if i % 8 == 0:  # 输出8个就换行
            print("\n")

# 爱因斯坦台阶问题
n = 0
while True:
    if n % 2 == 1 and n % 3 == 2 and n % 4 == 3 and n % 5 == 4 and n % 6 == 5 and n % 7 == 0:
        break
    else:
        n += 1
print("总台阶数：", n)

# 元组
mytup = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
print(mytup[:3])  # 输出前三个
print(mytup[1:3])  # 输出元组中检索顺序为1和2的元素
print(mytup[-1])  # 倒数第一个
print(max(mytup))  # 元组的最大长度值
print(len(mytup))  # 元组长度
print(mytup[1:9:2])  # 取元组

# 字典
numbers = {0: 'zero', 1: 'one', 2: 'two', 3: 'three', 4: 'four',
           5: 'five', 6: 'six', 7: 'seven', 8: 'eight', 9: 'nine'}#数字对应的英文单词
phone = input("enter your telephone number:")#输入阿拉伯数字形式的电话号码
for n in phone:#根据键输出电话号码对应的英文单词
    print(numbers[int(n)], end=" ")
print()#空行

# 莫尔斯电码
key = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
       'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0']#英文字母与阿拉伯数字列表
value = ['._', '_...', '_._.', '_..', '.', '.._.', '__.', '....', '..', '.___', '_._', '._..', '__', '_.', '___',
         '.__.', '__._', '._.', '...', '_', '.._', '..._', '.__', '_.._', '_.__', '__..', '.____', '..___', '...__',
         '...._', '.....', '_....', '__...', '___..', '____.', '_____']#与上列表元素对应的莫尔斯电码
mDic = dict(zip(key, value))#生成字典
s = input("Enter some uppercase letters or Numbers:")#提示输入
for i in s:
    print(mDic[i], end=" ")#根据数字键输出莫尔斯电码
print()

# 第六题4
Cstr = input("Enter some Chinese words：")
s = set(Cstr)
print(s)

# 第七题
vowels = ['a', 'e', 'i', 'o', 'u']
vowelStr = input("Enter some English words:")
count = 0
for i in vowelStr:
    if i in vowels:
        count += 1
print("Total vowels are: ", count)
