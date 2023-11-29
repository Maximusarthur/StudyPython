import csv

class Score:
    def __init__(self, name, id, score1, score2, score3):  # 姓名、学号，3门课程成绩
        self.name = name
        self.id = id
        self.score1 = score1
        self.score2 = score2
        self.score3 = score3
    def get_scores(self):
        return [self.score1, self.score2, self.score3]

def create_csv(): # 创建csv文件保存11名学生成绩
    scores = [
        Score('张', '001', 80, 85, 90),
        Score('李', '002', 70, 75, 80),
        Score('王', '003', 90, 95, 100),
        Score('赵', '004', 60, 65, 70),
        Score('钱', '005', 85, 90, 95),
        Score('孙', '006', 75, 80, 85),
        Score('周', '007', 95, 100, 95),
        Score('吴', '008', 65, 70, 75),
        Score('郑', '009', 85, 90, 85),
        Score('陈', '010', 80, 85, 80),
        Score('汪', '011', 55, 45, 65)
    ]
    with open('scores.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['姓名', '学号', 'python成绩', 'java成绩', 'C语言成绩'])
        for score in scores: # 成绩写入csv文件
            writer.writerow([score.name, score.id, score.score1, score.score2, score.score3])

def find_student_score(name): # 根据姓名查找成绩
    with open('scores.csv', newline='') as csvfile:
        reader = csv.reader(csvfile)
        headers = next(reader, None)
        for row in reader:
            if row[0] == name: # 查找每行第一个与需查找的名字相等的行
                return Score(row[0], row[1], int(row[2]), int(row[3]), int(row[4]))
    return None

def find_student_rank(name): #查找学生成绩排名
    scores = []
    with open('scores.csv', newline='') as csvfile:
        reader = csv.reader(csvfile)
        headers = next(reader, None)
        for row in reader:
            scores.append((row[0], [int(row[2]), int(row[3]), int(row[4])]))
    for student_scores in scores:
        if student_scores[0] == name:
            ranks = []
            for i, score in enumerate(student_scores[1]): # 查找学生的成绩排名与整列成绩相对比
                rank = 1 # 起始排名为1
                for other_scores in scores:
                    if other_scores[1][i] > score:
                        rank += 1 # 如果有成绩大于该成绩，则成绩排名数加1
                ranks.append(rank)
            return ranks
    return None


def main():
    try:
        create_csv()
        name = input("请输入同学姓名：")
        score = find_student_score(name)
        if score is None:
            print("找不到该学生的成绩记录！")
        else:
            print("姓名：{}".format(score.name))
            print("学号：{}".format(score.id))
            print("python成绩：{}，java成绩：{}，C语言成绩：{}".format(score.score1, score.score2, score.score3))
            ranks = find_student_rank(name)
            print("python成绩排名：{}，java成绩排名：{}，C语言成绩排名：{}".format(ranks[0], ranks[1], ranks[2]))
    except FileNotFoundError:
        print("找不到成绩记录文件！")
    except ValueError:
        print("输入的学生姓名不正确！")

if __name__ == '__main__':
    main()
