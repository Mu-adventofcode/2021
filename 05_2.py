import parse
from collections import Counter


def parse_input(filename):
    """
    Parse input file and return a list of vent lines. Each vent line consists
    of two points: start point p0 and end point p1.
    """

    ventlines = []
    with open(filename) as txt:
        for txtline in txt:
            res = parse.search("{x0:d},{y0:d} -> {x1:d},{y1:d}\n", txtline)
            p0 = (res["x0"], res["y0"])
            p1 = (res["x1"], res["y1"])
            ventlines.append((p0, p1))
    return ventlines


def points_on_line(ventline):
    """
    Given a vent line (two endpoints), return the list all points on it.
    """

    (x0, y0), (x1, y1) = sorted(ventline)
    if x0 == x1:
        return [(x0, y) for y in range(y0, y1 + 1)]
    elif y0 == y1:
        return [(x, y0) for x in range(x0, x1 + 1)]
    elif y1 > y0:
        return [(x0 + k, y0 + k) for k in range(x1 - x0 + 1)]
    else:
        return [(x0 + k, y0 - k) for k in range(x1 - x0 + 1)]


def main(filename):
    ventlines = parse_input(filename)
    points = [pt for vl in ventlines for pt in points_on_line(vl)]
    counts = Counter(points)
    duplicates = counts - Counter(counts.keys())
    print(len(duplicates))


if __name__ == "__main__":
    main("input.txt")
