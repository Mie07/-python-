"""
演示嵌套循环使用
"""

i = 1

for i in range(1, 101):
    print(f"今天是向小美表白的第{i}，坚持")
    for j in range(1,11):
        print(f"这是送给小美的第{j}朵玫瑰花。")
    print("小美我喜欢你")

print(f"第{1}天，表白成功")