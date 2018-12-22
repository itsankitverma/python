winner = 78
guess = 1
number = int(input("Enter a number between 1 to 100 : "))
game_end = False

while not game_end:
    if number == winner:
        print(f"Yo dude, you won the game in {guess} attempts")
        game_end = True
    else:
        if number < winner:
            print("Bro, number was lesser than winning number.. Try again")
            guess += 1
            number = int(input("Enter a number between 1 to 100 : "))
        else:
            print("Bro, number was higher than winning number.. Try again")
            guess += 1
            number = int(input("Enter a number between 1 to 100 : "))