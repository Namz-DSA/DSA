def SumOfNumbers(n):
    if n == 0:
        return 0
    return n + SumOfNumbers(n-1)

print(SumOfNumbers(5))