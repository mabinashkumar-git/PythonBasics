# https://journaldev.com/14036/python-data-types

#List
values = [1, 2, "Abinash", 4, 5, 6, 7]
print(values, type(values))
print(values[0])
print("last value", values[-1])
print(values[1:4])

print ("***********************************************")

values.insert(3, "Kumar")
values.insert(4, "Mallick")
print(values)

print ("***********************************************")

values.remove("Kumar")
print(values)

print ("***********************************************")

values.append("Append")
print(values)

print ("***********************************************")

values[2] = "ABINASH"
values[3] = "MALLICK"
print(values)

print ("***********************************************")

values.reverse()
print(values)