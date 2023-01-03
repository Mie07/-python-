# 定义字母变量
count = 0
name = "itheima is a brand of itcast"

# for 循环统计
for x in name:
    # 分析name变量里有多少个a
    if x == "a":
        count += 1

print(f"被统计的字符串中有{count}个a")
