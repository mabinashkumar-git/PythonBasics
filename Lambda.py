def add(x,y):
    return x + y

add = lambda x, y: x + y

num = [1, 2, 3, 4, 5]
squared_num = map(lambda  x : x*2, num)
print("list(squared_num) --->", list(squared_num))

filterVar = filter(lambda x : x%2==0, num)
even_num = list(filterVar)
print("even_num ---> ", even_num)

number = [3, 6, 2, 1]
print("sorted(num)--->", sorted(number))

print("Last digit reveresed no -: ", number[::-1])
