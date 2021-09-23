principal = 1000
rate = 0.07

for year in range(1,31):
    amount = principal * (1 + rate)** year
    print("investment returns for year:", year,"at rate of ", rate, "is ", amount)
    rate += 0.01