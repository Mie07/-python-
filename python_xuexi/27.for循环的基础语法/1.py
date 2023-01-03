"""
演示for循环的基础语法
"""

name = "itheima"

for x in name:
    # 将name的内容，挨个取出赋予x临时变量
    # 就可以在循环体内对x经行处理
    print(x)
    # for 临时变量 in 待处理数据集（序列）：
    # 循环满足条件时执行的代码