# 菜单
menu = {
    "1": {"name": "地三鲜", "price": 20},
    "2": {"name": "玫瑰羹", "price": 18},
    "3": {"name": "酸菜肉沫", "price": 25},
    "4": {"name": "炒青菜", "price": 10},
    "5": {"name": "荷包蛋", "price": 10},
}

order = {}
while True:
    table_num = input("请输入桌号：") # 客人点单
    if table_num == "":
        break
    print("菜单：")
    for k, v in menu.items(): # 展示菜单
        print(f"{k}. {v['name']} ￥{v['price']}")
    print()

    while True:
        dish_num = input("请输入菜品编号（按回车键结束点单）：") # 点单
        if dish_num == "":
            break
        dish_count = input("请输入菜品份数：")
        if dish_count == "":
            break
        if dish_num not in menu:
            print("菜品不在本店的菜单里")
            continue
        dish_name = menu[dish_num]["name"]
        dish_price = menu[dish_num]["price"]
        if table_num not in order:
            order[table_num] = {} # 创建新的订单
        if dish_name not in order[table_num]:
            order[table_num][dish_name] = 0
        order[table_num][dish_name] += int(dish_count)

    print()
    print("当前桌子点单信息：")
    for k, v in order[table_num].items(): # 展示当前桌子点单信息
        print(f"{k} x {v}")

    print("后厨的电子屏")
    for table_num, table_order in order.items(): # 将点单信息发送到后厨的电子屏上
        print(f"桌号：{table_num}")
        print("点单信息：")
        for dish_name, dish_count in table_order.items():
            print(f"{dish_name} x {dish_count}")
