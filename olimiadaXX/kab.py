import functools
from datetime import datetime


def comparator(p1, p2):
    if p1[0] < p2[0]:
        return -1
    elif p1[0] > p2[0]:
        return 1
    else:
        if p1[1] < p2[1]:
            return -1
        elif p1[1] > p2[1]:
            return 1
        else:
            return 0


'''
N = 200_000
sockets = []
for i in range(N*2):
    sockets.append((i, i))
'''

N = int(input("Podaj ilosc kabelków)"))
sockets = []

for i in range(2*N):
    print("Podaj wspólrzedne gniazdka (oddzielone spacja): " + str(i))
    s1 = input(": ")
    nums = s1.split()
    point1 = int(nums[0]), int(nums[1])
    sockets.append(point1)


start = datetime.now()

sorted_points = sorted(sockets, key=functools.cmp_to_key(comparator))
for i in range(0, len(sorted_points), 2):
    print(sorted_points[i], sorted_points[i+1])
end = datetime.now()
print(end - start)

