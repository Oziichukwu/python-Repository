# result = int(input("Enter result"))

student = 10
count = 1
passed = 0
failed = 0
while count <= student:
    result = int(input("Enter result\n"))
    if result == 1:
        passed +=1

    elif result == 2:
        failed +=1
    count +=1
print(passed , "student(s) passed and", failed, "student(s) failed")

if passed > 8:
    print("Bonus to instructor")

