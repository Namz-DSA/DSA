def power(n, exp):
    if exp == 0:
        return 1
    if exp == 1:
        return n
    return n * power(n, exp-1)

print(power(2,5))