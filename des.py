# https://sio2.mimuw.edu.pl/c/oij14-1/p/des/
#

planks = [6, 3, 7, 6, 5, 8, 10]

def get4planks(planks):
    planks.sort()

    last = planks[len(planks)-4:len(planks)]
    return min(last)


print(get4planks(planks)**2)
