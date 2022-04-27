VALID_DAYS = range(9)


def parse_input(filename):
    with open(filename) as txt:
        textline = txt.readline().strip()
    fishes = [int(days) for days in textline.split(",")]
    return [fishes.count(d) for d in VALID_DAYS]


def main(filename, days=80):
    counts = parse_input(filename)
    for _ in range(days):
        spawners = counts[0]
        counts = counts[1:]
        counts.append(spawners)  # each spawner produces one offspring
        counts[6] += spawners
    return sum(counts)


if __name__ == "__main__":
    print(main("input.txt", 256))
