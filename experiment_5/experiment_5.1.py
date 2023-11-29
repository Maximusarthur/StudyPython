import tkinter as tk
import math
def calculate():
    # 从文本输入框中获取表达式
    expression = entry.get()
    try:
        # 使用自定义函数计算表达式的结果
        result = evaluate_expression(expression)
        # 清空文本输入框
        entry.delete(0, tk.END)
        # 将计算结果显示在文本输入框中
        entry.insert(tk.END, str(result))
    except Exception as e:
        # 如果计算出错，清空文本输入框并显示错误消息
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")
def evaluate_expression(expression):
    if '+' in expression:
        numbers = expression.split('+')
        return sum((number) for number in numbers)
    elif '-' in expression:
        numbers = expression.split('-')
        return (numbers[0]) - sum((number) for number in numbers[1:])
    elif '*' in expression:
        numbers = expression.split('*')
        return math.prod((number) for number in numbers)
    elif '/' in expression:
        numbers = expression.split('/')
        return float(numbers[0]) / float(numbers[1])
    # 幂运算
    if '^' in expression:
        base, exponent = expression.split('^')
        return (base) ** (exponent)
    # 开方和平方根
    elif '√' in expression:
        number = expression[1:]
        return math.sqrt(float(number))
    # 对数运算
    elif 'log' in expression:
        base, number = expression[3:].split('.')  # 点号分隔对数的两个数字
        return math.log(float(number), float(base))
    # 三角函数
    elif expression.startswith(('sin', 'cos', 'tan')):
        func = expression[:3]
        angle = expression[3:]
        if angle.endswith('.'):  # 点代替度数符号
            angle = angle[:-1]
            angle = math.radians(float(angle))
        else:
            angle = float(angle)
        if func == 'sin':
            return math.sin(angle)
        elif func == 'cos':
            return math.cos(angle)
        elif func == 'tan':
            return math.tan(angle)
    # 绝对值
    elif expression.startswith('|') and expression.endswith('|'):
        number = expression[1:-1]
        return abs(float(number))
    # 阶乘
    elif '!' in expression:
        number = int(expression[:-1])
        return math.factorial(number)
    else:
        # 如果表达式不匹配任何支持的运算，引发异常
        raise ValueError("Invalid expression")

def clear():
    # 清空文本输入框
    entry.delete(0, tk.END)

def add_to_entry(text):
    # 将按钮上的文本添加到文本输入框中
    entry.insert(tk.END, text)

root = tk.Tk()
root.title("Scientific Calculator")

# 创建文本输入框
entry = tk.Entry(root, width=80)
entry.grid(row=0, column=0, columnspan=20)
buttons = [
    ("C", 1, 0),
    ("√", 2, 0),
    ("^", 3, 0),
    ("log", 4, 0),
    ("sin", 1, 1),
    ("cos", 2, 1),
    ("tan", 3, 1),
    ("|x|", 4, 1),
    ("!", 1, 2),
    ("π", 2, 2),
    ("e", 3, 2),
    ("%", 4, 2),
    ("7", 1, 3),
    ("8", 1, 4),
    ("9", 1, 5),
    ("/", 1, 6),
    ("4", 2, 3),
    ("5", 2, 4),
    ("6", 2, 5),
    ("*", 2, 6),
    ("1", 3, 3),
    ("2", 3, 4),
    ("3", 3, 5),
    ("-", 3, 6),
    ("0", 4, 3),
    (".", 4, 4),
    ("=", 4, 5),
    ("+", 4, 6)
]

for button_text, row, col in buttons:
    # 创建按钮，并绑定add_to_entry函数作为点击事件的回调函数
    button = tk.Button(root, text=button_text, width=10, command=lambda text=button_text: add_to_entry(text))
    button.grid(row=row, column=col)
    # 设置按钮的背景色和前景色
    button.config(bg="white", fg="black")

equal_button = tk.Button(root, text="=", width=10, command=calculate)
equal_button.grid(row=4, column=5)
equal_button.config(bg="lightblue", fg="black")

clear_button = tk.Button(root, text="C", width=10, command=clear)
clear_button.grid(row=1, column=0)
clear_button.config(bg="red", fg="white")

root.mainloop()
