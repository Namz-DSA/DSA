def LongestWord(s):
    split_s = [word.strip(',.') for word in s.split()]
    length = {}

    for s1 in split_s:
        if s1 not in length:
            length[s1] = len(s1)
    
    sort_len = list(sorted(length.items(), key = lambda x : x[1], reverse = True))
    return sort_len[0][0]

print(LongestWord("Keep coding, keep growing"))