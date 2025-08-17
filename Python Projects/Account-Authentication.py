username = ["akopogigamer","johnmarston32","carljohnson22"]
password = ["pogiako123","itsjohnmarston123","icantfollowthetrain"]

user = input("username : ")
pas = input("password : ")

for i in range(len(username)):
    if user == username[i] and pas == password[i]:
        print("welcome", username[i])
        break
else:
    print("account not found")