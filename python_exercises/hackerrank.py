from collections import Counter

numbers = [1]

counter = Counter(numbers)

unique = [key for key, value in counter.items() if value == 1]
print(unique[])

