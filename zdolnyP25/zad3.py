def sum_zad3(n):
    bit_length = len(str(bin(n)).replace('0b', ''))
    digits_sum = sum([int(digit) for digit in str(n)])
    return bit_length, digits_sum


n = int(input("N="))
print(sum_zad3(n))

print(bin(3))