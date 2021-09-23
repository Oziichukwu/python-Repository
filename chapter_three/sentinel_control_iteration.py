total = 0
grade_counter = 0
count = 1

grade = int(input("Enter grade or -1 to exit\n"))

while grade !=-1:
    total += grade
    grade_counter+=1
    grade = int(input("Enter grade or -1 to exit\n") )
    
if grade_counter != 0:
    average = total / grade_counter
    print(f'class average is: {average: .2f}')

else:
    print("No grades were entered")     

