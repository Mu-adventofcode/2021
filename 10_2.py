from functools import reduce
from statistics import median

OPENERS = "([{<"
OPPOSITE = {"(": ")", "[": "]", "{": "}", "<": ">"}
POINTS = {")": 1, "]": 2, "}": 3, ">": 4}
CORRUPT = object()


def short_stack(line):
    stack = []
    for ch in line:
        if ch in OPENERS:
            stack.append(ch)
        else:
            prev = stack.pop()
            if OPPOSITE[prev] != ch:
                return CORRUPT
    return stack


def scores(lines):
    def ch_score(cs, ch):
        return cs * 5 + POINTS[ch]

    for line in lines:
        stack = short_stack(line)
        if stack != CORRUPT:
            completion = (OPPOSITE[ch] for ch in stack[::-1])
            yield reduce(ch_score, completion, 0)


with open("input.txt") as f:
    lines = [line.strip() for line in f]
middle = median(scores(lines))
print(middle)
