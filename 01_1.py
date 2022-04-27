def count_increases(report):
    lst = [int(n) for n in report.split()]
    return sum(1 if x2 > x1 else 0 for x1, x2 in zip(lst[:-1], lst[1:]))


if __name__ == "__main__":
    with open("input.txt") as f:
        print(count_increases(f.read()))
