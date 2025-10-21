
def a(x):
    bit_length = len(str(bin(x)).replace('0b', ''))
    return bit_length


def b(x):
    digits_sum = sum([int(digit) for digit in str(x)])
    return digits_sum


n = int(input())
n = b(n)
n = a(n)
print(n)
