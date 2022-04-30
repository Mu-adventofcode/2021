from functools import reduce
from statistics import median

OPPOSITE = {"(": ")", "[": "]", "{": "}", "<": ">"}
POINT_VALUE = {")": 1, "]": 2, "}": 3, ">": 4}
CORRUPT = object()


def build_stack(line):
    stack = []
    for ch in line:
        if ch in OPPOSITE:
            stack.append(ch)
        else:
            if OPPOSITE[stack.pop()] != ch:
                return CORRUPT
    return stack


def char_score(subtotal, missing_char):
    return subtotal * 5 + POINT_VALUE[missing_char]


def completion_scores(lines):
    for line in lines:
        stack = build_stack(line)
        if stack != CORRUPT:
            completion = (OPPOSITE[ch] for ch in stack[::-1])
            yield reduce(char_score, completion, 0)


with open("input.txt") as f:
    lines = [line.strip() for line in f]
scores = list(completion_scores(lines))
middle = median(scores)
print(middle)
