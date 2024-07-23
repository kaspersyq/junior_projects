# Lyrics generator

song1 = "Baby by Bieber\n\nYou know you love me (Yo), I know you care (Uh-huh)\nJust shout whenever (Yo), and I'll be there (Uh-huh)\nYou are my love (Yo), you are my heart (Uh-huh)\nAnd we will never, ever, ever be apart (Yo, uh-huh)..."
song2 = "Hotline Bling by Drake\n\nYou used to call me on my cell phone\nLate night when you need my love\nCall me on my cell phone\nLate night when you need my love..."
song3 = "Flawless by Beyonce\n\nI'm out that H, town coming coming down\nI'm coming down, drippin' candy on the ground\nH, Town, Town, I'm coming down, coming down\nDrippin' candy on the ground..."

print("Welcome, please select a song from this top 3 songs:\n1. Baby by Bieber\n2. Hotline Bling by Drake\n3. Flawless by Beyonce")

def print_lyrics(song_number):
    if song_number == 1:
        print(song1)
    elif song_number == 2:
        print(song2)
    else:
        print(song3)

select = int(input())
print_lyrics(select)