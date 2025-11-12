from activity1 import *

def activity1():
    print(activity1)

# def activty10()

isContinue = True

while isContinue == True:
    print("\nSelect Program")
    print("A = Activity1 \nB = Activity 10 \nC = Activity 20 \nE = Exit")
    
    choose = input("What program / code would you like to choose : ").upper()

    if choose == "A":
        activity1()
        continue
    pass

    # elif choose == "B":
    #     actti