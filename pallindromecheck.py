def isPallindrome(s):
    s = ''.join(c.lower() for c in s if c.isalnum())
    return s == s[::-1]
print(isPallindrome("A man, a plan, a canal: Panama"))