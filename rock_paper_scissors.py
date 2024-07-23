# rock paper scissors

import random
print("Let's play rock paper scissors")
variants = ['rock', 'paper', 'scissors']

while True:
    user_choice = input("Your choice: ")
    computer_choice = random.choice(variants)
    print(f'My choice is {computer_choice}')
    if user_choice.lower() == 'rock':
        if computer_choice == 'rock':
            print("Draw! Let's try again")
            continue
        elif computer_choice == 'paper':
            print("Haha, I won!")
            break
        elif computer_choice == 'scissors':
            print("Oops I lost :(")
            break
    elif user_choice.lower() == 'paper':
        if computer_choice == 'rock':
            print("Oops I lost :(")
            break
        elif computer_choice == 'paper':
            print("Draw! Let's try again")
            continue
        elif computer_choice == 'scissors':
            print("Haha, I won!")
            break
    elif user_choice.lower() == 'scissors':
        if computer_choice == 'rock':
            print("Haha, I won!")
            break
        elif computer_choice == 'paper':
            print("Oops I lost :(")
            break
        elif computer_choice == 'scissors':
            print("Draw! Let's try again")
            continue
    else:
        print('You should choice only rock, paper or scissors')
        continue