# 定义一个数字变量num,内容随意
num = 0
for x in range(1, 100):
    if x%2 == 0:
        num += 1
print(f"1到100(不含100本身)范围内，有{num}个偶数。")