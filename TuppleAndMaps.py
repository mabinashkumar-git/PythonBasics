# https://journaldev.com/14036/python-data-types

# The tuple is another data type which is a sequence of data similar to a list. But it is immutable. That means data in a tuple is write-protected.
# Data in a tuple is written using parenthesis and commas.

#Tuple
values = (1, 2, "Abinash", 4, 5, 6, 7)
print(values, type(values))

print ("********************** 1 *************************")

#Maps
name  = {1:31, 2:"Abinash", 3:"Kumar", "a":"Mallick"}
print(name[1])
print(name[2])
print(name[3])
print(name["a"])

print ("********************** 2 *************************")

name["Fistname"] = "Animesh"      # Adds to the list mentioned in line no 13
name["Lastname"] = "Saha"
print("Name -:", name)
print("Lastname -:", name["Lastname"])
