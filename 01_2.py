def sliding_windows(iterable):
    """
    Yields the next three values from the input.
    """

    for idx in range(len(iterable) - 2):
        yield iterable[idx : idx + 3]


def count_increases(report):
    """
    Returns the number of times the depth increases in the sweep given by
    report.
    """

    ints = [int(s) for s in report.split()]
    sums = [sum(w) for w in sliding_windows(ints)]
    return sum(1 if x2 > x1 else 0 for x1, x2 in zip(sums[:-1], sums[1:]))


if __name__ == "__main__":
    with open("input.txt") as txt:
        print(count_increases(txt.read()))
