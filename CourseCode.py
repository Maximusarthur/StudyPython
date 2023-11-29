"""
A = set("important")
A.remove("i")
print(A)

ls = ['a', 'a', 'c', 22]  # 列表
l = set(ls)  # 集合
s = list(l)
print(l)
print(s)

# 序列类型：字符串，元组，列表

元组：tuple()
列表：list()

s = "qwerty"
print(s[::-1])  # s[::-1]序列类型的倒叙操作
s = "qwerty121212"
print(s.count('1'))

# 元组一旦被创建就不能被修改，且小括号可有可无
s = [1, 2, 3]
t = s
print(t)
s.append(4)
print(s)
print(t)
print(s.reverse())  # s.reverse()无返回值，只进行操作
# 字典：数据元素——键值对

#return 可以放置在函数的任何一个位置，执行到第一个return时，程序返回值到调用函数
def fun():
    x=3
    count=2
    while count>0:
        print(x)
        count=count-1
fun()
print(x)

m=100
n=200
def f1():
    print(m+5)
    n+=10

def f2():
    print(m + 5)
    global n
    n += 10
    print(n,end=" ")
f1()

ls = ["F", "f"]
def func(a):
    ls = []
    ls.append(a)
    return
func("C")
print(ls)

def f(n):
    if n == 1 or n == 2:
        return 1
    else:
        return f(n-1)+f(n-2)
f(10)

class Cat:
    leg_num = 4
    def __init__(self, name, age, weight):
        self.name = name
        self.age = age
        self.__weight = weight

Cat1 = Cat("Tom", 2, 10)
print(Cat1.name)
print(Cat1._Cat__weight)
# print(Cat1.__weight) 报错
"""
# 类方法中访问对象实例属性会导致错误
# 类方法不对特定实例进行操作

from tkinter import *
import tkinter.messagebox
root = Tk()
btnSayHi = Button(root)
btnSayHi["text"] = "hello"
btnSayHi.pack()
def sayHi(e):
    tkinter.messagebox.showinfo("Message", "Hello,world!")
btnSayHi.bind("<Button-1>",sayHi)
root.mainloop()
