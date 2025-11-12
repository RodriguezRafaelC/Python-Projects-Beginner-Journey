import random

guess = random.randint(1, 100)

for i in range(1, 6):
    number = int(input("Enter a Number : "))
    if number == guess:
        print("Contrats ya nahulaan mo")
        break

    elif number > guess:
        print("Babaan nimo!\n")

    else:
        print("taasan nimo!\n")

else:
    print(f"ubos na load nimo and numero ay {guess}")