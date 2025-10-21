dane = input().split()
a = int(dane[0])
b = int(dane[1])
wynik, i = 0, 0

while i < b:
    wynik += a + i
    i += 1
print(wynik)
