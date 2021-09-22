first_number = int(input("Enter the first number\n"))
second_number =  int(input("Enter the second number\n"))
third_number =  int(input("Enter the third number\n"))

sum = first_number+second_number+third_number
print("The sum is ", sum)

average = sum / 3
print("The average is ", average)

product = first_number*second_number*third_number
print("The product is ", product)

smallest = min(first_number,second_number,third_number)
print("The smallest is ", smallest)

largest = max(first_number,second_number,third_number)
print("The largest number is ", largest)