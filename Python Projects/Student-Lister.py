students = [
    ["1A",[]],
    ["1B",[]],
    ["1C",[]]
]

isContinue = True

while isContinue == True:
    name = input("\nEnter Student's Name : ")
    
    if name == "exit":
        break

    section = input("Enter Student's Section : ").upper()

    if section == "1A":
        students[0][1].append(name)
        print(f"{name} has been added to 1A")

    elif section == "1B":
        students[1][1].append(name)
        print(f"{name} has been added to 1B")

    elif section == "1C":
        students[2][1].append(name)
        print(f"{name} has been added to 1C")

    else:
        print("Invalid Section!")

for i in students:
    print(i[0])
    for x in i[1]:
        print(f"- {x}")
    print()