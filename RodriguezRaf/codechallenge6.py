num = int(input("Enter a Number : "))
a = 1

for i in range(num, 0, -1):
    a *= i

    print(i, "x",i, "=", a)