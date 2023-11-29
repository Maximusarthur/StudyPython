import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
from tkinter.font import Font

# 创建一个文本编辑器类
class TextEditor:
    def __init__(self, root):
        self.root = root
        self.root.title("Text Editor")  # 设置窗口标题
        self.file_path = None  # 当前文件的路径
        self.font = Font()  # 文本字体

        # 创建菜单栏
        self.menu_bar = tk.Menu(root)
        self.root.config(menu=self.menu_bar)

        # 创建文件菜单
        self.file_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.menu_bar.add_cascade(label="File", menu=self.file_menu)
        self.file_menu.add_command(label="New", command=self.new_file)  # 新建文件
        self.file_menu.add_command(label="New Window", command=self.new_window)  # 新建窗口
        self.file_menu.add_command(label="Open", command=self.open_file)  # 打开文件
        self.file_menu.add_command(label="Save", command=self.save_file)  # 保存文件
        self.file_menu.add_command(label="Save As", command=self.save_file_as)  # 另存为
        self.file_menu.add_separator()
        self.file_menu.add_command(label="Exit", command=self.exit)  # 退出

        # 创建编辑菜单
        self.edit_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.menu_bar.add_cascade(label="Edit", menu=self.edit_menu)
        self.edit_menu.add_command(label="Undo", command=self.undo)  # 撤销
        self.edit_menu.add_command(label="Redo", command=self.redo)  # 重做
        self.edit_menu.add_separator()
        self.edit_menu.add_command(label="Select All", command=self.select_all)  # 全选
        self.edit_menu.add_command(label="Underline", command=self.underline)  # 下划线
        self.edit_menu.add_command(label="Bold", command=self.bold)  # 粗体

        # 创建文本编辑区域
        self.text_area = tk.Text(root, wrap=tk.WORD, font=self.font)
        self.text_area.pack(expand=True, fill=tk.BOTH)

        # 创建撤销和重做堆栈
        self.undo_stack = []
        self.redo_stack = []

        # 监听键盘事件
        self.text_area.bind("<Control-z>", self.undo)  # Ctrl+Z 绑定撤销操作
        self.text_area.bind("<Control-y>", self.redo)  # Ctrl+Y 绑定重做操作

    def new_file(self):
        # 清空文本区域内容，并重置文件路径
        self.text_area.delete("1.0", tk.END)
        self.file_path = None

    def new_window(self):
        # 创建一个新窗口，并在其中打开一个新的文本编辑器
        new_root = tk.Tk()
        new_editor = TextEditor(new_root)
        new_root.mainloop()

    def open_file(self):
        # 打开文件对话框选择文件，并读取文件内容显示在文本编辑区域中
        file_path = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt")])
        if file_path:
            try:
                with open(file_path, "r") as file:
                    content = file.read()
                self.text_area.delete("1.0", tk.END)
                self.text_area.insert(tk.END, content)
                self.file_path = file_path
            except Exception as e:
                # 显示错误消息框，提示读取文件出错
                messagebox.showerror("Error", str(e))

    def save_file(self):
        # 如果有文件路径，则保存文件内容到指定路径；否则调用另存为操作
        if self.file_path:
            content = self.text_area.get("1.0", tk.END)
            try:
                with open(self.file_path, "w") as file:
                    file.write(content)
                # 显示成功消息框，提示文件保存成功
                messagebox.showinfo("Success", "File saved successfully.")
            except Exception as e:
                # 显示错误消息框，提示保存文件出错
                messagebox.showerror("Error", str(e))
        else:
            self.save_file_as()

    def save_file_as(self):
        # 另存为文件，弹出文件对话框选择保存路径，并保存文件内容
        file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt")])
        if file_path:
            self.file_path = file_path
            self.save_file()

    def undo(self, event=None):
        # 撤销操作，将当前内容保存到重做堆栈，然后从撤销堆栈中恢复之前的内容
        if self.undo_stack:
            content = self.text_area.get("1.0", tk.END)
            self.redo_stack.append(content)
            self.text_area.delete("1.0", tk.END)
            content = self.undo_stack.pop()
            self.text_area.insert(tk.END, content)

    def redo(self, event=None):
        # 重做操作，将当前内容保存到撤销堆栈，然后从重做堆栈中恢复之前撤销的内容
        if self.redo_stack:
            content = self.text_area.get("1.0", tk.END)
            self.undo_stack.append(content)
            self.text_area.delete("1.0", tk.END)
            content = self.redo_stack.pop()
            self.text_area.insert(tk.END, content)

    def select_all(self):
        # 选中全部文本
        self.text_area.tag_add(tk.SEL, "1.0", tk.END)

    def underline(self):
        # 设置选中文本的下划线样式，如果已经设置则取消下划线
        current_tags = self.text_area.tag_names("sel.first")
        if "underline" in current_tags:
            self.text_area.tag_remove("underline", "sel.first", "sel.last")
        else:
            self.text_area.tag_add("underline", "sel.first", "sel.last")
            self.text_area.tag_configure("underline", underline=True)

    def bold(self):
        # 设置选中文本的粗体样式，如果已经设置则取消粗体
        current_tags = self.text_area.tag_names("sel.first")
        if "bold" in current_tags:
            self.text_area.tag_remove("bold", "sel.first", "sel.last")
        else:
            self.text_area.tag_add("bold", "sel.first", "sel.last")
            self.text_area.tag_configure("bold", font=self.font.configure(weight="bold"))

    def exit(self):
        # 退出程序，关闭主窗口
        self.root.destroy()

# 创建主窗口并启动事件循环
root = tk.Tk()
editor = TextEditor(root)
root.mainloop()
