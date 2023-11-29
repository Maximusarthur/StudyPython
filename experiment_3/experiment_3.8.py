import pyodbc

# 数据库连接参数
server = 'SD-20220201KPRR' # 服务器名称
database = 'testdb' # 数据库名称
username = 'Elm' # 用户名
password = '' # 密码
cnxn = pyodbc.connect(f'DRIVER={{SQL Server}};SERVER={server};DATABASE={database};UID={username};PWD={password}')

def read_data(sql): # 从数据库读取数据
    try:
        cursor = cnxn.cursor()
        cursor.execute(sql)
        rows = cursor.fetchall() # 获取所有查询结果
        return rows
    except pyodbc.Error as e:
        print(f'读取数据失败: {e}')
        return None

def execute_sql(sql): # 执行SQL语句
    try:
        cursor = cnxn.cursor()
        cursor.execute(sql) #执行SQL语句
        cnxn.commit()
        return True
    except pyodbc.Error as e:
        print(f'执行SQL语句失败: {e}')
        return False


print("数据库现有的数据：")
rows = read_data('SELECT * FROM TestTable') # 读取数据函数
if rows:
    for row in rows:
        print(row)


if int(input("是否要执行SQL语句(1|0):")) == 1:
    sql = input("输入SQL语句:")  # 测试执行 SQL 语句函数
    result = execute_sql(sql)
    if result:
        print("SQL语句执行成功！")
    else:
        print("请重新输入:")


