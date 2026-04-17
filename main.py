from collections import Counter

def count_keys_freq(lst):
    return dict(Counter(lst))

def unique_keys(lst):
    freq = Counter(lst)
    return [k for k, v in freq.items() if v == 1]

# test (list ishlatamiz)
inventory = ['apple', 'banana', 'apple', 'orange']

print(count_keys_freq(inventory))
print(unique_keys(inventory))
