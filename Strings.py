
str = "Abinash Kumar Mallick"           #Syntax for declaring a string in Python, unlike in java like String variable name = "Value";
str1 = "Aakash Bhushan"
str2 = "Kumar"
str3 = "Kumar "
str4 = " Kumar"

print(str[0])
print(str[1])

print(str[0:5])

print(str, str1)
print(str + str1)

print(str2 in str)

print(str.split("K"))
print(str.split("Kumar"))
print(str.split("Kumar "))

var = str.split("Kumar ")
print(var[0])
print(var[1])

#strip removes the spaces
print(str3.strip())
print(str4.lstrip())
print(str3.strip())