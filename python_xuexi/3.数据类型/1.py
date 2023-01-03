# 方法1： 使用print直接输出类型信息
print(type("咩咩"))
print(type(666))
print(type(11.345))

# 方法2： 使用变量存储type()语句的结果
string_type = type("咩咩")
int_type = type(666)
float_type = type(11.345)
print(string_type)
print(int_type)
print(float_type)

# 方法3： 使用type()语句，查看变量中存储的数据类型信息
neme = "咩咩"
neme_type = type(neme)
print(neme_type)