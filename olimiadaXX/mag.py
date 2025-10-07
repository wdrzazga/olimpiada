def magic(words):
    for x in range(5):
        print()
        for y in range(5):
            print(words[x][y], end='')


words = []
for i in range(5):
    words.append(input("Podaj slowo (5 liter): "))


magic(words)
