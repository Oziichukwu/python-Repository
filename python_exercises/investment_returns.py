from typing import Counter


counter = 10
number = 30

while counter <= number:
    amount = 1000*(1 + 0.07) ** counter
    print("The amount after ", counter, "years  is \n", amount)
    print() 
    counter += 10