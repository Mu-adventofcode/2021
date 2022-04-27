def parse_input(filename):
    with open(filename) as fin:
        line = fin.read().strip()
    return [int(p) for p in line.split(",")]


def fuel_use(positions):
    return min(
        sum(abs(p - end_pos) for p in positions)
        for end_pos in range(min(positions), max(positions))
    )


if __name__ == "__main__":
    print(fuel_use(parse_input("input.txt")))
