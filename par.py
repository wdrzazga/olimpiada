# https://oij.edu.pl/oij14/etap1/zadania/
# https://sio2.mimuw.edu.pl/c/oij14-1/p/par/
from datetime import datetime

N = int(input('Ktora liczba pazystocyfowa ?: '))

start = datetime.now()


def digit_even(number):
    digits = list(str(number))
    for digit in digits:
        if int(digit) % 2:
            return False
    return True


greatest = 0

index = 0
i = 0

while index <= N:
    if digit_even(i):
        greatest = i
        index += 1

    i += 1

print(greatest, index, 'pozdrawiam')
print(datetime.now() - start)
