class Person:
    count = 0  # 类属性，用于跟踪Person类的对象数量

    def __init__(self, name='', age=0, sex=''):
        self._name = name  # 私有属性，用于存储姓名
        self.age = age  # 实例属性，用于存储年龄
        self.sex = sex  # 实例属性，用于存储性别
        Person.count += 1  # 每次创建新的Person对象时，将对象数量加1

    def __del__(self):
        Person.count -= 1  # 对象被删除时，将对象数量减1

    def print_info(self):
        """打印Person实例的信息"""
        print(f"Name: {self._name}\nAge: {self.age}\nSex: {self.sex}")

    @property
    def name(self):
        """获取姓名属性"""
        return self._name

    @name.setter
    def name(self, value):
        """设置姓名属性"""
        if isinstance(value, str):
            self._name = value
        else:
            raise ValueError("Name must be a string.")

    @staticmethod
    def print_count():
        """静态方法，实时打印当前内存中的Person对象数量"""
        print(f"Current number of Person objects: {Person.count}")

    @classmethod
    def from_string(cls, info_string):
        """类方法，根据字符串实例化并返回一个Person对象"""
        info_list = info_string.split(',')
        if len(info_list) == 3:
            name, age, sex = [item.strip() for item in info_list]
            return cls(name, int(age), sex)
        else:
            raise ValueError("Invalid string format. Expected format: 'name, age, sex'")


person1 = Person("小明", 20, "男")
person2 = Person("Bob", 30, "男")

person1.print_info()
print()
person2.print_info()
print()
Person.print_count()
del person2  # 手动删除一个对象
Person.print_count()

