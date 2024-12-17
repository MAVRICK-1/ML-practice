import heapq
from collections import Counter

s = 'abracadabra'

# Count the frequency of each character in the string
c = Counter(s)

print(c)

sorted_chars = sorted(c.items(), reverse=True)
print(sorted_chars)
        