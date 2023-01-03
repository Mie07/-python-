"""
练习
"""
name = "传智博客"
stock_price = 19.99
stock_code = "003032"
stock_price_daily_gtowth_factor = 1.2
growth_days = 7
print(f"公司：{name}，股票代码：{stock_code}，当前股票：{stock_price}")
print("每日增长系数为%.1f,经过%d天的增长后，股价达到了%5.2f"%(stock_price_daily_gtowth_factor,growth_days,stock_price*1.2**7))
