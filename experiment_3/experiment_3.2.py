def open_file():
    while True:
        file_path = input("请输入文件路径:")
        try:
            file = open(file_path, "r") # 只读模式下打开文件
            content = file.read()       # 获取文件内容
            file.close()                # 关闭文件
            print("文件内容:", content)
            break                       # 正确打开文件退出循环
        except IOError:                 # 报错提示后继续循环
            print("文件路径错误，请重新输入。")


open_file()
# 文件地址experiment_2.txt