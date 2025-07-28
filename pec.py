def check_unluckiness(n):
    digits = list(str(n))
    contains_13 = False
    previous = '-1'
    for digit in digits:
        if previous == '1' and digit == '3':
            contains_13 = True
        previous = digit
    digit_sum = 0
    for digit in digits:
        digit_sum += int(digit)
    return digit_sum == 13 and contains_13


to_be_tested = [139, 33133, 13, 553]

for n in to_be_tested:
    print(n, check_unluckiness(n))
