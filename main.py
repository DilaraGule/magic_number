import random


def ask_number(nb_min, nb_max):
    number_int = 0
    while number_int == 0:
        number = input(f"What is the magic number (between {nb_min} and {nb_max}): ")
        try:
            number_int = int(number)
        except:
            print("ERROR: You must enter a number.")
        else:
            if number_int < nb_min or number_int > nb_max:
                print(f"ERROR: You must enter a number between {nb_min} and {nb_max}.")
                number_int = 0
    return number_int


min_number = 1
max_number = 10
magic_num = random.randint(min_number, max_number)
lives = 4

number = 0
while not number == magic_num and lives > 0:
    print(f"You have {lives} lives")
    number = ask_number(min_number, max_number)
    if number == magic_num:
        print("you won!!")
    elif number > magic_num:
        print("the magic number is lower")
        lives -= 1
    else:
        print("the magic number is greater")
        lives -= 1

if lives == 0:
    print(f"You lost! The magic number is {magic_num}")

"""
    win = False
    for i in range(0, lives):
        new_lives = lives - i
        print(f"You have {lives} lives")
        number = ask_number(min_number, max_number)
        if number == magic_num:
            print("you won!!")
            win = True
            break
        elif number > magic_num:
            print("the magic number is lower")
        else:
            print("the magic number is greater")

    if not win:
        print(f"You lost! The magic number is {magic_num}")
        
"""
