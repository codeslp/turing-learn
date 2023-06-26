words = ['this', 'is', 'an', 'elementary', 'aaaaaaaaaaaaa', 'test', 'example']
from collections import Counter

repeater = words[1]

for word in words[1:]:
    c = Counter(word).most_common(1)
    if c[0][1] > Counter(repeater).most_common(1)[0][1]:
        repeater = word
print(repeater)


# badass optimal example: 
from collections import Counter

WORDS = ['this', 'is', 'an', 'elementary', 'test', 'example']

def most_repeating_letter_count(word):                        
    return Counter(word).most_common(1)[0][1]                 

def most_repeating_word(words):
    return max(words, key=most_repeating_letter_count)

print(most_repeating_word(WORDS))