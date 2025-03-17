# https://journaldev.com/14036/python-data-types

#List
values = [1, 2, "Abinash", 4, 5, 6, 7]
print(values, type(values))
print(values[0])
print("last value -:", values[-1])
print("Value -:",values[1:4])

print ("******************** 1 ***************************")

values.insert(3, "Kumar")
values.insert(4, "Mallick")
print(values)

print ("********************* 2 **************************")

values.remove("Kumar")
print(values)

print ("********************* 3 **************************")

values.append("Append")
print(values)

print ("********************* 4 **************************")

values[2] = "ABINASH"
values[3] = "MALLICK"
print(values)

print ("********************* 5 **************************")

values[3] = "ABINASH"
values[4] = "MALLICK"
print(values)

print ("********************** 6 *************************")

values.reverse()
print(values)

print ("********************** 7 *************************")
data = [{"name":"Abinash", "Age":34}, {"Name":"Aakash", "age":33}]
print(data[1]["Name"])
