from experiment_41 import Person  # 导入person.py文件中的Person类
class Student(Person):
    def __init__(self, name='', age=0, sex='', stuNo=0):
        super().__init__(name, age, sex)
        self.stuNo = stuNo

    def print_info(self):
        super().print_info()
        print(f"Student ID: {self.stuNo}")

student1 = Student("小明", 20, "男", 2023)
student1.print_info()