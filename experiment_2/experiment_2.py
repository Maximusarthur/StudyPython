
# 第一题
import sys
import subprocess
# 以空格分离字符串从标准输入读取两个数字，计算它们的和
x, y = map(int, sys.stdin.readline().split())
result = x + y
# 输出结果到标准输出
print(result)
# 使用 sort 和 more 过滤器对输出进行处理
cmd = 'sort | more'
proc = subprocess.Popen(cmd, shell=True, stdin=subprocess.PIPE)
# proc.communicate(input=str(result).encode())

#第二题
import os
# 使用标准输入并使用管道命令将输出传递给sort和more过滤器
os.system('sort | more')

# 第三题
# 打开原始文件和目标文件(省去了文件可以正常打开时的文件关闭)
with open('input.txt', 'r') as input_file, open('output.txt', 'w') as output_file:
    for line in input_file:
        for char in line:
            # 如果是大写字母，将其加密为下一个字母，如果是Z，则加密为A
            if char.isupper():
                encrypted_char = chr((ord(char) - 65 + 1) % 26 + 65)
            # 如果是小写字母，将其加密为下一个字母，如果是z，则加密为a
            elif char.islower():
                encrypted_char = chr((ord(char) - 97 + 1) % 26 + 97)
            # 否则，保持不变
            else:
                encrypted_char = char
            # 将加密后的字符写入目标文件
            output_file.write(encrypted_char)
    print("加密并写入成功！")

#第四题
import os
def main():
    student_list = read_student_info()  # 读取学生信息
    while True:
        choice = input("请选择操作：1.添加 2.删除 3.修改 4.显示 5.退出\n")
        if choice == '1':
            add_student_info(student_list)  # 添加学生信息
            write_student_info(student_list)  # 写入文件
        elif choice == '2':
            delete_student_info(student_list)  # 删除学生信息
            write_student_info(student_list)  # 写入文件
        elif choice == '3':
            modify_student_info(student_list)  # 修改学生信息
            write_student_info(student_list)  # 写入文件
        elif choice == '4':
            show_student_info(student_list)  # 显示学生信息
        elif choice == '5':
            break  # 退出程序
        else:
            print("输入有误，请重新选择操作。")

def read_student_info():
    student_list = []
    if os.path.exists('student_info.txt'):
        with open('student_info.txt', 'r') as f:
            lines = f.readlines()
            for line in lines:
                student_info = line.strip().split(',')
                student_list.append({
                    'name': student_info[0],
                    'gender': student_info[1],
                    'phone': student_info[2]
                })
    return student_list

def write_student_info(student_list):
    with open('student_info.txt', 'w') as f:
        for student in student_list:
            f.write("{},{},{}\n".format(student['name'], student['gender'], student['phone']))

def add_student_info(student_list): # 根据输入信息创建字典
    name = input("请输入学生姓名：")
    gender = input("请输入学生性别：")
    phone = input("请输入学生手机号：")
    student_list.append({
        'name': name,
        'gender': gender,
        'phone': phone
    })
    print("学生信息添加成功！")

def delete_student_info(student_list):
    name = input("请输入要删除的学生姓名：")
    for student in student_list:
        if student['name'] == name:
            student_list.remove(student)
            print("学生信息删除成功！")
            break
    else:
        print("未找到该学生信息，请检查姓名是否正确。")

def modify_student_info(student_list):
    name = input("请输入要修改的学生姓名：")
    for student in student_list:
        if student['name'] == name:
            gender = input("请输入学生性别：")
            phone = input("请输入学生手机号：")
            student['gender'] = gender
            student['phone'] = phone
            print("学生信息修改成功！")
            break
    else:
        print("未找到该学生信息，请检查姓名是否正确。")

def show_student_info(student_list):
    print("{:<10}{:<10}{:<15}".format("姓名", "性别", "手机号")) # 左对齐格式化输出信息
    for student in student_list:
        print("{:<10}{:<10}{:<15}".format(student['name'], student['gender'], student['phone']))

if __name__ == '__main__':
    main()

# 第五题
import jieba
import re
from collections import Counter
# 中文
def chinese_text_analysis(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        text = f.read()
    # 使用jieba分词对文本进行处理
    words = list(jieba.cut(text))
    # 定义无用词列表，过滤出现频率较高但无实际意义的词汇
    stopwords = ['，', '。', '！', '？', '：', '；', '、', '的', '了', '在', '是', '和', '有', '我', '你', '他', '她', '它',
                 '我们', '你们', '他们', '她们', '它们']
    # 对分词结果进行无用词过滤，并计算每个人物出现的次数
    characters = [w for w in words if w not in stopwords and len(w) > 1]
    counts = Counter(characters)
    # 输统计元素出现次数并按照出现次数从高到低排序，返回前 10 个出现次数最多的元素和它们的出现次数
    top_10 = counts.most_common(10)
    print('西游记排名前十的人物及出现次数：')
    for i, (name, count) in enumerate(top_10):
        print(f'{i+1}.{name}: {count} 次')
# 英文
def english_text_analysis(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        text = f.read()
    # 去除标点符号（替换非字母和空格的字符为空字符串）
    text = re.sub(r'[^\w\s]','',text)
    # 去除无用词,用正则表达式中的\b表示单词边界,|符号连接起来表示匹配其中任意一个词语,flags=re.IGNORECASE来表示忽略大小写。
    text = re.sub(r'\b(the|and|of|to|in|a|that|was|he|she|it)\b', '', text, flags=re.IGNORECASE)
    # 统计人物出现次数
    character_dict = {}
    for line in text.split('\n'):
        for word in line.split():
            if word.istitle() and len(word) > 1:
                character_dict[word] = character_dict.get(word, 0) + 1
    # 排序并输出前十（key=lambda x: x[1], reverse=True表示对列表中的元素按照其第二个值（出现次数）从大到小排序，Ture表示逆序）
    sorted_characters = sorted(character_dict.items(), key=lambda x: x[1], reverse=True)
    print('悲惨世界排名前十的人物及出现次数：')
    for character, count in sorted_characters[:10]:
        if count >= 2:
            print(f'{character}: {count}')
chinese_file_path = "西游记.txt"
english_file_path = "悲惨世界.txt"
# 分别进行中文和英文文本分析
chinese_text_analysis(chinese_file_path)
english_text_analysis(english_file_path)

#第六题
import csv
# 创建CSV文件并写入学生信息
with open('students.csv','w', newline='') as file:
    writer = csv.writer(file)
    while True:
        student_info = input("请输入学生信息（格式：姓名,性别,年龄,语文成绩,数学成绩,英语成绩），输入-1结束：")
        if student_info == '-1':
            break
        writer.writerow(student_info.split(','))
# 从CSV文件中读取学生信息并统计排序
students = []
with open('students.csv','r') as file:
    reader = csv.reader(file)
    for row in reader:
        students.append({
            'name': row[0],
            'gender': row[1],
            'age': int(row[2]),
            'chinese': int(row[3]),
            'math': int(row[4]),
            'english': int(row[5])
        })
students.sort(key=lambda x: x['chinese'] + x['math'] + x['english'], reverse=True)
# 将统计结果写入新文件
with open('students_rank.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['姓名', '性别', '年龄', '语文成绩', '数学成绩', '英语成绩', '总成绩'])
    for student in students:
        writer.writerow([
            student['name'],
            student['gender'],
            student['age'],
            student['chinese'],
            student['math'],
            student['english'],
            student['chinese'] + student['math'] + student['english']
        ])


