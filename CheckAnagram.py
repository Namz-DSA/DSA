from collections import Counter
def CheckAnagram(s,t):
    s = ''.join([word.strip(',.') for word in s.split()])
    t = ''.join([word.strip(',.') for word in t.split()])

    return Counter(s) == Counter(t)

print(CheckAnagram("listen","silent"))
print(CheckAnagram("hello","world"))
print(CheckAnagram("Dormitory", "Dirty room"))