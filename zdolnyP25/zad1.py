napis = input()
wynik = 0
i = 0
while True:
    if i < len(napis):
        if napis[i] == 'a':
            wynik += 1
        else:
            wynik *= 2
        i += 1
    else:
        print(wynik)
        break
