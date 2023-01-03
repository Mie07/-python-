"""
演示嵌套调用函数
"""

# 定义函数func_b
def fuc_b():
    print("--2--")
# 定义函数func_a,并在内部调用func_b
def fuc_a():
    print("--1--")
    fuc_b()
    print("--3--")

# 调用函数func_a
fuc_a()