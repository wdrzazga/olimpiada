def count_needed_exercises(dream):
    needed_exercises = []
    for i in range(len(exercises)):
        needed_exercises.append(exercises[i])
        total = sum(needed_exercises)
        if total >= dream:
            return i + 1


exercises = []
exercises_amount = int(input("Podaj ilosc zadan: "))

for i in range(exercises_amount):
    exercises.append(int(input(f"Podaj punktacje {i+1} zadania: ")))
exercises.sort(reverse=True)

dreams = []
dreams_amount = int(input("Podaj ilosc snów: "))
for i in range(dreams_amount):
    dreams.append(int(input(f"Podaj wartosc {i+1} snu: ")))


for dream in dreams:
    print(count_needed_exercises(dream))
