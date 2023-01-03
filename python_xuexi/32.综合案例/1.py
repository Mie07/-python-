# 定义一个公司余额
company_balance = 10000
# 利用for语句进行循环,i变量生成员工,
for i in range(1,21):
    # 生成绩效分
    import random
    score = random.randint(1,10)

    # 利用if语句进行判断，员工是否达到绩效分
    if score < 5:
        print(f"员工{i}绩效分{score},绩效分少于5,不予发工资")
        # 跳过发放
        continue
    # 要判断余额够不够
    if company_balance >= 1000:
        company_balance -= 1000
        print(f"员工{i}，满足条件发放工资，公司余额{company_balance}")
    # 余额不足的情况下
    else:
        print(f"当前余额剩下{company_balance}元,结束发工资")
        # break结束发放
        break
