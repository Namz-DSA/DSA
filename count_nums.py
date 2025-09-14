def count(n):
    if n < 9:
        return 1
    return 1 + count(n // 10)

print(count(12345))