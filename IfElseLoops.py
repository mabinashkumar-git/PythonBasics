from List import values

value = "Abinash Mallick"

if value == "Abinash":
    print("In if block ", value)
else:
    print("Came to else block", "failure", value)
    print("Code failed")

print("First Loop completed")

if value == "Abinash Mallick":
    print("In if block ", value)
    print("Code Passed")
else:
    print("Came to else block", "failure", value)
    print("Code failed")

print("Second Loop completed")

print ("********************* 1 **************************")

obj = [1,2,3,4,5]
for i in obj:
    print(i)
    print(i*4)

print ("*********************** 2 ************************")

#print sum first 5 numbers
sum = 0
for j in range(1,6):     #for(int i=1; i<10; i++)
    sum = sum + j
    print(j)
print("Sum -:",sum)

print ("*********************** 3 ************************")

for k in range(1,10,2):   #for(int i=1; i<10; i+2)
    print(k)

print ("************************ 4 ***********************")

for m in range(5):   # Here loop will start from 0 and will run till 4
    print(m)