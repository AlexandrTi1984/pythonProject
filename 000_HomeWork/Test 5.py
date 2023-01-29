num1 = (1, 2, 3, 5, 8)
num2 = (8, 2, 5)
# print(num1[0:2] + num2 + num1[2:])

num1 = list(num1)
for x in num2[::-1]:
    num1.insert(2,x)
num1=tuple(num1)
print(num1)
