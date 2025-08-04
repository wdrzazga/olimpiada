import itertools

array = [1, 2, 3, 4, 5]
combinations_list = []


for r in range(2, len(array) + 1):
    combos = list(itertools.combinations(array, r))
    combinations_list.extend(combos)

for combo in combinations_list:
    print(combo)
