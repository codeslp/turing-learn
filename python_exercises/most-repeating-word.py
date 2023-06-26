words = ['this', 'is', 'an', 'elementary', 'aaaaaaaaaaaaa', 'test', 'example']
from collections import Counter

repeater = words[1]

for word in words[1:]:
    c = Counter(word).most_common(1)
    if c[0][1] > Counter(repeater).most_common(1)[0][1]:
        repeater = word
print(repeater)