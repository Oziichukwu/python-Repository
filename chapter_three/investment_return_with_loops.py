principal = 1000
rate = 0.07

for year in range(1,31):
    amount = principal *  (1 + rate) ** year
    print("Investment returns for year:", year ,"=", amount)