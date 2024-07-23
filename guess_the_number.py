# Guess the number

import random
correct_number = random.randint(1, 100)
attempts = 0
print('Try to guess the random number between 1 and 100 in as few attempts as you can')
while True:
    user_number = int(input())
    if user_number > correct_number:
        print('Your number is more than guessed')
        attempts += 1
    elif user_number < correct_number:
        print('Your number is less than guessed')
        attempts += 1
    else:
        print(f'Congratulations, you won! It took you {attempts} attemtps')
        break