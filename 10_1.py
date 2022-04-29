OPOSITE = {"(": ")", "[": "]", "{": "}", "<": ">"}
SCORE = {")": 3, "]": 57, "}": 1197, ">": 25137}


def score(line):
    stack = []
    for ch in line:
        if ch in "([{<":
            stack.append(ch)
        else:
            prev = stack.pop()
            if OPOSITE[prev] != ch:
                return SCORE[ch]
    return 0


with open("input.txt") as f:
    lines = [line.strip() for line in f]
scores = [score(line) for line in lines]
print(sum(scores))
