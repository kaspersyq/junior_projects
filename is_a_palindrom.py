# is a palindrom

words_list = input('Give me 5 words: ').split()
for word in words_list:
    if word.lower() == word.lower()[::-1]:
        print(f'{word} is a palindrom!')