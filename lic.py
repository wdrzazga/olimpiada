from datetime import datetime


def f(n):
    return sum(int(str(n)[x]) for x in range(len(str(n))))


def g(n):
    return n + f(n) ** 2


print(g(18))

amount = int(input("Ile liczb?:\n"))

start = datetime.now()

numbers = []
for i in range(amount):
    numbers.append(int(input("Liczba: ")))

numbers_copy = numbers.copy()

i = 0
while i < 10 * 10 * 10 * 1000:
    result = g(i)
    if result in numbers:
        print("tak", i, result)
        numbers_copy.remove(result)

    i += 1

for number in numbers:
    if number in numbers_copy:
        print(number, "nie")
    else:
        print(number, "tak")

print(datetime.now() - start)
