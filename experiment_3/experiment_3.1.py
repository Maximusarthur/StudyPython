def twoNumberDivision( a, b):
    try:
        result = a / b
        print("a 除以 b 的结果是：", result)
    except ValueError:           # 数值类型错误
        print("输入值必须为数字，请重新输入。")
    except ZeroDivisionError:    # 除数为0错误
        print("除数不能为零，请重新输入。")
    except Exception as e:       # 其他错误
        print("发生了一个错误，请重试。错误信息：", e)

a = float(input("请输入被除数a："))
b = float(input("请输入除数b："))

twoNumberDivision(a, b)#执行除法函数
