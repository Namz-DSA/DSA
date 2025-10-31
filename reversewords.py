def reverseWords(s):
    split_s = s.split()
    return ' '.join(split_s[::-1])

print(reverseWords("Python is fun"))
print(reverseWords(" Hello  world  "))