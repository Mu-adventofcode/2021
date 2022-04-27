from collections import Counter

with open("input.txt") as txt:
    output_values = [line.split(" | ")[1].strip() for line in txt]
digit_lengths = [len(d) for val in output_values for d in val.split()]
counts = Counter(digit_lengths)
total = sum(counts[i] for i in (2, 4, 3, 7))  # lens of digits 1, 4, 7 resp 8
print(total)
