try:
    import random as rd
    a = int(input("Enter Your choice:\n 1)ROCK \n 2)PAPER \n 3)SCISSOR \n "))
    if a < 4:
        list = ["ROCK","PAPER","SCISSOR"]
        choice = rd.choice(list)
        print("The computer choice is:",choice)
        if choice == "ROCK" and a == 1:
            print("Your choice is ROCK ")
            print("Hurray you have won")
        elif choice == "PAPER" and a==2:
            print("Your choice is PAPER")
            print("Hurray you have won")
        elif choice == "SCISSOR" and a == 3:
            print("Your choice is SCISSOR")
            print("Hurray you have won")
        else:
            print("better luck next time")
    else:
        print("enter the valid choice")
except ValueError:
    print("Enter the valid value")
