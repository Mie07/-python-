"""
演示判断语句的实战案例：究极猜数字
"""

# 1.构建一个随机的数字变量
import random
num = random.randint(1,10)
# print(num)

guess_num =int(input("请输入你要猜测的数字："))
if num == guess_num:
    print("恭喜你，一次就猜对了")
else:
    if guess_num > num:
        print("你猜测的数字大了")
    else:
        print("你猜测的数字小了")

    guess_num = int(input("请输入你要猜测的数字："))

    if guess_num == num:
        print("恭喜你，2次就猜对了")
    else:
        if guess_num > num:
            print("你猜测的数字大了")
        else:
            print("你猜测的数字小了")

        guess_num = int(input("请输入你要猜测的数字："))

        if guess_num == num:
            print("恭喜你，3次就猜对了")
        else:
            print("三次机会用完了")