# Odd or even

answer = 'y'
while answer.lower() == 'y':
    print('What number are you thinking?')
    number = int(input())
    if number % 2 == 1:
        print("That's an odd number! Have another? y = yes, n = no")
    else:
        print("That's an even number! Have another? y = yes, n = no")
    answer = input()