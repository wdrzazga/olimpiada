import itertools
from datetime import datetime

homes_count = int(input("Enter liczbe domow"))

homes = []

for i in range(homes_count):
    candies = int(input('Ile cukierkow w domu ' + str(i + 1) + ' '))
    homes.append(candies)

begin = datetime.now()

combinations_list = []
for r in range(2, len(homes) + 1):
    combos = list(itertools.combinations(homes, r))
    combinations_list.extend(combos)

result = 0
for c in combinations_list:
    if not sum(c) % 2:
        result += 1

print(datetime.now() - begin)
print(result)
