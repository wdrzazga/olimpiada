from datetime import datetime

plus_minus = input("Enter niepusty ciag n znaków + i - bez zadnych odstepów.")
plus_minus = '-+-'*1000
begin = datetime.now()

exchanged = plus_minus.replace("--", "+")
plus_groups = exchanged.split("-")
lengths = [len(array) for array in plus_groups]
print(max(lengths))
print(datetime.now() - begin)
