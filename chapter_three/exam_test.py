passed = 0
failed = 0

for student in range(10):
    result = int(input("Enter result: "))
    if result == 1:
        passed += 1

    elif result == 2:
        failed += 1

print(f'students that passed: {passed}')       
print(f'students that failed: {failed}')

if  passed > 8:
    print("Bonus to instructor")