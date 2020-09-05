#Number Game
#Concept - assign number , enter number by user, check assigned==input, conditons

winning_number = 7

enter_num = int (input(print("Enter any number to win game: \n")))

if winning_number==enter_num:
    print("Congrats You won")

else:
        if enter_num>winning_number:
            print("Guess is TOO High")
        else:
            print("Guess is TOO Low")