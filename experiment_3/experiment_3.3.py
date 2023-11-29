def filterList(numbers):
    filtered_numbers = list(filter(lambda x: x > 0, numbers))  # 过滤列表中小于和等于0的数，并将结果转换为列表
    return filtered_numbers  # 返回新产生的列表


numbers = [1, -1, 3, 0, -5, 5]
filtered_numbers = filterList(numbers)
print(filtered_numbers)  # [1, 3, 5]
