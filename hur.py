# https://sio2.mimuw.edu.pl/c/oij14-1/p/hur/

from datetime import datetime


def count(numbers):
    for number in range(numbers):
        if not number % 7 and not number % 11:
            print("Wiwat")
        elif not number % 7:
            print("Hurra")
        elif not number % 11:
            print("Super")
        else:
            print(number)


n = input("Ile liczy©?: ")
start = datetime.now()
count(int(n))
print(start)
print(datetime.now())
