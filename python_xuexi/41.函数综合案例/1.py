"""
演示ATM
"""
# 定义一个全局变量：money，用于记录银行卡余额(默认5000000)
money1 = money = 5000000.00
# 定义一个全局变量：name，用于记录客户姓名(启动程序时输入)
name = input("请输入您的名字:")
# 要求客户输入姓名
# 查询余额函数
def inquire(show_header):
    """

    :param show_header: 利用布尔形式 False:为不输出 True:为输出
    :return:输出余额
    """
    if show_header:
        print("------------查询余额-------------")
    print(f"{name}，您好，您的余额剩余：{money}元")
# 存款函数
def deposit(num):
    print("-------------存款---------------")
    global money    # money在函数内部定义为全局变量
    money += num
    print(f"{name}，您好，您存款{num}元成功")

    # 调用inquire函数查询余额
    inquire(False)
# 取款函数
def withdrawal(num):
    print("-------------取款---------------")
    if num <= money1:
        global money    # money在函数内部定义为全局变量
        money -= num
        print(f"{name}，您好，您取款{num}元成功")
        # 调用inquire函数查询余额
        inquire(False)
    else:
        print("余额不足")
# 主菜单函数
def main_menu():
    print("------------主菜单--------------")
    print(f"{name}，您好，欢迎来到牛马银行ATM。请选择操作：")
    print("查询余额\t[输入1]")
    print("存款\t\t[输入2]")
    print("取款\t\t[输入3]")
    print("退出\t\t[输入4]")
    return input("请输入您的选择：")

# 设置无限循环，确保程序不会退出
while True:
    key_input = main_menu()
    if key_input == "1":
        inquire(True)
        continue    #通过continue继续下一个循环,一进来计算主菜单
    elif key_input == "2":
        deposit(float(input("请输入你要存款的金额：")))
        continue
    elif key_input == "3":
        withdrawal(float(input("请输入你要取款的金额：")))
        continue
    elif key_input == "4":
        print("欢迎下次使用，程序退出啦!!!")
        break