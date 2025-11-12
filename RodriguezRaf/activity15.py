odd = 0

for i in range(1, 11, 1):
    num = eval(input("Enter a number : "))

    if num % 2 != 0:
        odd += num

print(f"The sum of odd number is {odd}")

firstname = eval(input("Enter your firstname : "))
lastname = eval(input("Enter your lastname : "))
age = eval(input("Enter your age : "))

print(f"{firstname} {lastname} {age}")