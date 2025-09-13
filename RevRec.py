def Reverse(word):
    if len(word) == 0 or len(word) == 1:
        return word
    return Reverse(word[1:]) + word[0]

print(Reverse("hello"))