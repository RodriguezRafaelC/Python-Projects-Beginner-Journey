print("Welcome to Manga Recommendation!")
print("What Manga Genre are you Looking For?")
print("action, romance, horror")

genre = input("Search : ")

if genre.lower() == "action":
	print("You have selected", genre)
	duration = input("How long should the manga be? (short, medium, long) : ")
	if duration.lower() == "short":
		print("You have selected",genre, duration)
		decade = input("Which Decade? (2000s, 2010s) : ")
		if decade == "2000":
			print("Here is The Manga with Action, Short from 2000s : Alive, Akumetsu, Black Lagoon")

	elif genre.lower() == "action":
		print("You have selected", genre)
		if duration.lower() == "medium":
			print("You have selected",genre, duration)
			decade = input("Which Decade? (2000s, 2010s) : ")
			if decade == "2000":
				print("Here is The Manga with Action, Short from 2000s : Wolf Guy, Battle Royale, O-Parts Hunter")

	elif duration.lower() == "long":
		print("You have selected", genre)
		print("You have selected",genre, duration)
		decade = input("Which Decade? (2000s, 2010s) : ")
		if decade == "2000":
			print("Here is The Manga with Action, Short from 2000s : One Piece, Naruto, Bleach")


