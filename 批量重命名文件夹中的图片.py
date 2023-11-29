import os

# 文件夹路径
folder_path = r'C:\Users\Administrator\Desktop\lll'

# 获取文件夹中的所有文件
files = os.listdir(folder_path)

# 确定基准文件名
base_filename = 'guide'

# 遍历文件夹中的所有文件
for i, filename in enumerate(files):
    # 获取文件的完整路径
    file_path = os.path.join(folder_path, filename)

    # 检查文件是否是图片文件
    if os.path.isfile(file_path) and filename.lower().endswith(('.jpg', '.jpeg', '.png', '.gif', 'webp')):
        # 构建新的文件名
        new_filename = f'{base_filename}_{i + 1}{os.path.splitext(filename)[1]}'

        # 构建新的文件路径
        new_file_path = os.path.join(folder_path, new_filename)

        # 重命名文件
        os.rename(file_path, new_file_path)
        print(f'Renamed: {filename} -> {new_filename}')
