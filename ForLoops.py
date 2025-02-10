from List import values

obj = [1,2,3,4,5]
for i in obj:   #Syntax in pyhton for declaring loops
    print(i)
    print(i*4)

print ("***********************************************")

#print sum first 5 numbers
sum = 0
for j in range(1,6):     #for(int i=1; i<6; i++)
    sum = sum + j
    print(j)
print(sum)

print ("***********************************************")

for k in range(1,10,2):   #for(int i=1; i<10; i+2)
    print(k)

print ("***********************************************")

for m in range(5):   # Here loop will start from 0 and will run till 4
    print(m)