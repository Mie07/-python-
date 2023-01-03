age = int(input("请输入你的年龄:"))
year = int(input("请输入你的入职时间:"))
level = int(input("请输入你的级别："))
if age >= 18:
    print("你是成年人")
    if age < 30:
        print("你的年龄达标了")
        if year > 2:
            print("恭喜你，你的年龄和入职时间都达标了，可以领取礼物。")
        elif level > 3:
            print("恭喜你，你的年龄和级别都达标了，可以领取礼物。")
        else:
            print("不好意思，尽管年龄达标，但是入职时间和级别都不达标。")
    else:
       print("你的年龄太大了")
else:
    print("你不是成年人")