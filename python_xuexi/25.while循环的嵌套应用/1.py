# 外层：表白1000天的控制
# 内层：每天的表白都送10只玫瑰花的控制

i = 1
while i <= 100:
    print(f"今天是{i}天，准备表白....")

    # 内层循环控制变量
    j = 1
    while j <=10:
        print(f"送给小美第{j}只玫瑰花")
        j += 1

    print("小美，我喜欢你！")
    i += 1

print(f"坚持到第{i - 1}天，表白成功")