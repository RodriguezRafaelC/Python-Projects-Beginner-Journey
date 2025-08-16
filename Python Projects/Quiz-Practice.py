from ast import Break


print("Welcome To ITCS101 Quiz!")

correct_answers = ["People","Procedure","Software","Hardware","Data"]
score = 0

while score <= 6:
    q1 = input("Important Part of Info Sys : ")
    if q1 == correct_answers[0]:
        score = score + 1
        print("Correct!, your score is", score)
    else:
        print("Wrong!")
    q2 = input("Manual for People : ")
    if q2 == correct_answers[1]:
        score = score + 1
        print("Correct!, your score is", score)
    else:
        print("Wrong!")
    q3 = input("Process Raw Data into useful info : ")
    if q3 == correct_answers[2]:
       score = score + 1
       print("Correct!, your score is", score)
    else:
        print("Wrong!")
    q4 = input("Physical Components of Computer : ")
    if q4 == correct_answers[3]:
        score = score + 1
        print("Correct!, your score is", score)
    else:
        print("Wrong!")
    q5 = input("Raw and Unprocessed Facts : ")
    if q5 == correct_answers[4]:
        score = score + 1
        print("Correct!, your score is", score)
        print("Your Overall score is :", score)
        break
        
    else:
        print("Wrong!")
        print("Your Overall score is :", score)
        break
