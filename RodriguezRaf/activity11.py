temp = eval(input("Enter a Temperature : "))

if temp >=  1 and temp <= 21:
	print("The Temperature is Cold")
elif temp >= 21 and temp >= 30:
	print("The Temperature is Lukewarm")
elif temp >= 31 and temp >= 40:
	print("The Temperature is Warm")
elif temp >= 41 and temp >= 50:
	print("The Temperature is Hot")
elif temp >= 51:
	print("The Temperature is Boiling Hot")
else:
	print("Invalid Temperature")