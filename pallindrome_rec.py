def isPallindrome(num):
    n = str(num)

    if len(n) == 0 or len(n) == 1:
        return True
    if n[0] == n[-1]:
        return isPallindrome(n[1:len(n)-1])
    return False

print(isPallindrome(12321))