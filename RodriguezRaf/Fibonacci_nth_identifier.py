fibonacci = [0, 1]
nth_term = int(input("Nth Term You're Looking For: "))
if nth_term == 1 or nth_term == 2:
    print(fibonacci[:nth_term])
else:
    x = 0
    for i in range(nth_term - 2):
        new_term = fibonacci[x] + fibonacci[x + 1]
        fibonacci += [new_term]
        x += 1
    print(fibonacci)