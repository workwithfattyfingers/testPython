import random
winning_number= random.randint(1,100)
guess=1
numberinput = int(input("Guess a number between 1 and 100:\t"))
game_over= False

while not game_over:
    if numberinput == winning_number:
        print(f"Congragulations! You Won! You guess this number in {guess} times")
        game_over= True
        print("Lucky number is:\t" + str(numberinput))
    else:
        if numberinput < winning_number:
            print("ahh! too low")
            guess += 1
            numberinput = int(input("Guess a number between 1 and 100\t"))
        else:
            print("Nooo!! Too High")
            guess += 1
            numberinput = int(input("Guess a number between 1 and 100\t"))


