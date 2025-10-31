def shortDistance(s,c):
    answer = []

    pos = [i for i,ch in enumerate(s) if ch == c]

    for i in range(len(s)):
        answer.append(min(abs(i-p) for p in pos))
    print(answer)

shortDistance("loveleetcode","e")