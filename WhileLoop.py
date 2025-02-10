value = 2
value1 = 3
value2 = 3
value3 = 10

while value<10:
    print("True", value)
    value = value + 1

print ("***********************************************")

while value1<10:
    if value1 != 7:
        print("True", value1)
    value1 = value1 + 1

print ("***********************************************")

while value2<10:
    if value2 == 6:
        print("True for value2", value2)
        break
    else:
        print("In else loop for value2", value2)
    value2 = value2 + 1

print ("***********************************************")

while value3<10:
    if value3 == 9:
        print("Continue for value3", value3)
        value3 = value3 - 1
        continue
    if value3 == 6:
        print("True for value3", value3)
        break
    else:
        print("In else loop for value3", value3)
    value3 = value3 + 1