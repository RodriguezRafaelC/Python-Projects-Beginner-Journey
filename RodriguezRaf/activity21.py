

isTired = True

while isTired == True:
    question = input("Do you want to continue? (yes/no) : ").lower()

    if question == "yes":
        print("Let's keep going!\nYou look tired")
        continue
    elif question == "no":
        print("It's okay, take a rest")
        break
    else:
        print("...")
        continue