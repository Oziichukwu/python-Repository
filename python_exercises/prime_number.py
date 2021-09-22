number = int(input("Enter the number"))
count = 2
flag = False

if number == 1:
    print("number is not prime")
else:    
    while count <= number /2:
        if number % 2 == 0:
            flag = True
            break
        count +=1
    if not flag:
        print("number is prime")

    else:
        print("number is not prime")        