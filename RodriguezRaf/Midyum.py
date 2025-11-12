column = eval(input("Enter Column : "))

for i in range(1, 11):
    for x in range(1, column+1, 1):
        result = i * x
        print(f"{x} x {i} = {result}", end="\t")
    print()
    
for i in range(1, 7, 1):
    for x in range(7, i, -1):
        print(" ", end="")
    for z in range(1, i+1, 1):
        print("* ", end="")
    print()