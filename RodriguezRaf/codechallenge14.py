

name = input("Hi! Enter your name : ")
print("-----------------------------------------------------------------------")
print("Welcome to Odd number compiler, enter '0' to terminate program.")

isContinue = True
number = 0

while isContinue == True:
    num = eval(input("Enter a number : "))
    if num % 2 == 1:
        print("Odd number detected")
        number += num
        continue
    elif num % 2 != 1:
        print("Even number detected")
        continue
    elif num == "r":
        print("Program Ended")
        print(f"The sum of odd numbers is {number}")
        break