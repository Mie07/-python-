# 规则1： 内容限定，限定只能使用：中文、英文、数字、下划线，注意：不能数字开头
# 错误示范：1_name = "张三"
# 错误示范：name_! = "张三"
name_ = "张三"
_name = "张三"
name_1 = "张三"


# 规则2：大小写敏感
Miemie = "咩咩"
miemie = "123"
print(Miemie)
print(miemie)

# 规则3：不可以使用关键字
# 错误的示例class = 1
# 错误的示例def = 1
Class = 1