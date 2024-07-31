# What's my acronym?

print('please enter the full meaning of an organization or concept')
meaning = input()
words_list = meaning.split()
acronym = ''
for i in range(len(words_list)):
    acronym += words_list[i][0].upper()
print(acronym)