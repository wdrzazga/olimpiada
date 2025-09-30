import math
from datetime import datetime

N = 6

coord = [(0, 1), (10, 0), (0, 0), (20, 1), (1, 11), (1, 2)]
coord2 = 33333 * coord
print(len(coord2))
start = datetime.now()


def find_nearest_socket(point):
    coord.remove(point)
    distances = []
    for socket in coord2:
        a = abs(point[0] - socket[0])
        b = abs(point[1] - socket[1])
        distances.append(a ** 2 + b ** 2)

    return distances.index(min(distances)), min(distances)


def orient(P, Q, R):
    return (Q[0] - P[0]) * (R[1] - P[1]) - (Q[1] - P[1]) * (R[0] - P[0])


def intersect(s1, s2):
    A = s1[0]
    B = s1[1]
    C = s2[0]
    D = s2[1]

    return (orient(C, D, A) * orient(C, D, B) < 0) and (orient(A, B, C) * orient(A, B, D) < 0)


socket = (20, 1)
nearest_socket = find_nearest_socket(socket)

end = datetime.now()
print(end - start)
