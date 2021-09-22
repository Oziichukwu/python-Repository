number = 5
cube = 0
square = 0
count = 0
print ("number\tsquare\tcube")
while count <= number:
    square = count * count
    cube = count * count * count 
    print(count, "\t" , square , "\t" , cube)
    count += 1
