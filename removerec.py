def remove(s, ch):
    if s == "":
        return ""
    if s[0] == ch:
        return remove(s[1:],ch)
    return s[0] + remove(s[1:], ch)

print(remove("bananas","a"))