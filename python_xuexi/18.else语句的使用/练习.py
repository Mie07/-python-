"""
练习案例：我要买票吗
"""
print("欢迎来到黑马运动园。")
# 通过input语句获取键盘输入的身高
personal_height = int(input("请输入你的身高(cm):"))
# 通过if语句判断身高是否超过120cm，并通过print给出提示信息。
if personal_height > 120:
    print("您的身高超出120cm，游玩需要够票10元。")
else:
    print("您的身高未超出120cm，可以免费游玩。")
print("祝您游玩愉快！")