username = "RafaelTheGreat"
password = "akopogigamer11"

while True:
	user = input("Enter Username : ")
	pas = input("Enter Password : ")

	if user == username and pas == password:
		print("Access Granted!")
	else:
		print("Access Denied!")
		break