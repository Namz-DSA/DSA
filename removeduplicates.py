def RemoveDuplicates(s):
    seen = set()
    word = ""
    for ch in s:
        if ch not in seen:
            seen.add(ch)
            word += ch
    return word

print(RemoveDuplicates("programming"))