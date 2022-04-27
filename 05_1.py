import parse
from collections import Counter


def parse_input(filename):
    """
    Parse input file and return a list of vent lines.
    """

    lines = []
    with open(filename) as txt:
        for txtline in txt:
            result = parse.search("{x0:d},{y0:d} -> {x1:d},{y1:d}\n", txtline)
            p0 = (result["x0"], result["y0"])
            p1 = (result["x1"], result["y1"])
            lines.append((p0, p1))
    return lines


def linepoints(line):
    """
    Given a line (two endpoints), return the list all points on the line.
    """

    (x0, y0), (x1, y1) = sorted(line)
    if x0 == x1:
        return [(x0, y) for y in range(y0, y1 + 1)]
    elif y0 == y1:
        return [(x, y0) for x in range(x0, x1 + 1)]
    else:
        return []


def main(filename):
    lines = parse_input(filename)
    points = [pt for line in lines for pt in linepoints(line)]
    counts = Counter(points)
    duplicates = counts - Counter(counts.keys())
    print(len(duplicates))


if __name__ == "__main__":
    main("input.txt")
