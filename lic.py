def f(n):
    return sum(int(str(n)[x]) for x in range(len(str(n))))


def g(n):
    return n + f(n)**2


print(g(2019))
