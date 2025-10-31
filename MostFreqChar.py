from collections import Counter 
def MostfreqChar(s):
    s = ''.join(c.lower() for c in s if c != " ")

    freq = Counter(s)

    max_val = 0
    arr = []

    # sort_freq = dict(sorted(freq.items(), key = lambda x: x[1], reverse = True))

    for key, val in freq.items():
        if val > max_val:
            max_val = val
        
    for key, val in freq.items():
        if max_val == val:
            arr.append(key)
    
    return arr[0]


print(MostfreqChar("Python"))