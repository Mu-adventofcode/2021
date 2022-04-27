def parse_input(filename):
    with open(filename) as txt:
        string = txt.read().strip()
    return [int(s) for s in string.split(",")]


def main(filename, days=80):
    fishes = parse_input(filename)
    for _ in range(days):
        newborns = [8 for fish in fishes if fish == 0]
        elders = [6 if fish == 0 else fish - 1 for fish in fishes]
        fishes = elders + newborns
    return len(fishes)


if __name__ == "__main__":
    print(main("input.txt"))
