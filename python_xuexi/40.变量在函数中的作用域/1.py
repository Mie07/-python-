"""
演示在函数使用的时候，定义的变量作用域
"""

# 演示局部变量
def test_a():
    num = 100
    print(num)

test_a()
# 出了函数体，局部变量就无法使用了
# print(num)

# 演示全局变量
# num = 200
#
# def testA():
#     print(f"testA:{num}")
#
# def testB():
#     print(f"testB:{num}")
#
# testA()
# testB()
# print(num)

# 在函数内修改全局变量
# num = 200
#
# def testA():
#     num = 400
#     print(f"testA:{num}")
#
# def testB():
#     print(f"testB:{num}")
#
# testA()
# testB()
# print(num)

# global关键字，在函数内声明变量为全局变量
num = 200

def testA():
    num = 400
    print(f"testA:{num}")

def testB():
    global num #设置内部定义的变量成为全局变量
    num = 500
    print(f"testB:{num}")

testA()
testB()
print(num)