from collections import Counter

DIGITS = {
    # the meant-to-be pattern (sorted) for each digit
    "abcefg": 0,
    "cf": 1,
    "acdeg": 2,
    "acdfg": 3,
    "bcdf": 4,
    "abdfg": 5,
    "abdefg": 6,
    "acf": 7,
    "abcdefg": 8,
    "abcdfg": 9,
}


def mapwire(wire: str, freq: int, digit1: str, digit4: str) -> str:
    """
    Returns the meant-to-be segment position of a wire.
    Both the wire and the resulting position are symbolized by a one character
    string in (a, b, c, d, e, f, g).

    The following observations about frequencies and occurences fully determine
    the result (in this order):
    - f is the only position occuring in nine patterns (freq == 9)
    - a is in eight patterns; not in the pattern for 1 (digit1)
    - c is in eight patterns; including the 1
    - g in in seven patterns; not in the pattern for 4
    - d is in seven patterns; including the 4
    - b is the only position occuring in six patterns
    - e is the only position not adhering to any of the above
    """

    if freq == 9:
        return "f"
    elif freq == 8:
        if wire not in digit1:
            return "a"
        else:
            return "c"
    elif freq == 7:
        if wire not in digit4:
            return "g"
        else:
            return "d"
    elif freq == 6:
        return "b"
    else:
        return "e"


def decode(entry: list[list]) -> int:

    # sort all the strings so they can be compared
    patterns = ["".join(sorted(pat)) for pat in entry[0].split()]
    readings = ["".join(sorted(dig)) for dig in entry[1].split()]

    # identify the 1 and the 4
    patterns.sort(key=len)
    d1 = patterns[0]
    d4 = patterns[2]

    # translate patterns to the meant-to-be digits
    digits = {}
    freqs = Counter("".join(patterns))
    for pat in patterns:
        goodpat = "".join(sorted(mapwire(ch, freqs[ch], d1, d4) for ch in pat))
        digits[pat] = DIGITS[goodpat]

    # build the number from the readings
    number = "".join(str(digits[r]) for r in readings)
    return int(number)


def main(filename):
    with open(filename) as txt:
        numbers = (
            decode(line.strip().split(" | ")) for line in txt.readlines()
        )
    return sum(numbers)


if __name__ == "__main__":
    print(main("input.txt"))
