from collections import Counter
def firstUniqueChar(s):
    freq = Counter(s)
    lst = []

    for key, val in freq.items():
        if val == 1:
            lst.append(key)

    for ch in s:
        if ch in lst:
            return ch
    return None

print(firstUniqueChar("hello"))
print(firstUniqueChar("aabbcc"))
print(firstUniqueChar("leetcode"))