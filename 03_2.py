from collections import Counter


def _filter_down(rows, criterium_type, idx=0):
    """Recursive function to eliminate rows until one is left. Only rows with
    the correct bit are kept. The criteria bit is evaluated from left to
    right by incrementing idx in the recursive calls."""

    column = tuple(zip(*rows))[idx]
    cnt = Counter(column)
    gamma_bit = "1" if cnt["1"] >= cnt["0"] else "0"
    if criterium_type == "gamma":
        criterium_bit = gamma_bit
    else:
        criterium_bit = "1" if gamma_bit == "0" else "0"

    filtered = []
    for row in rows:
        if criterium_bit == row[idx]:
            filtered.append(row)

    if len(filtered) == 1:
        return filtered[0]  # finish with the one remaining row
    elif len(filtered) == 0:
        return rows[-1]  # finish with last row from previous round
    else:
        return _filter_down(filtered, criterium_type, idx=idx + 1)


def life_support(rows):
    """Given a list of row strings, returns the life support rating."""

    filtered = _filter_down(rows, criterium_type="gamma")
    oxygen = int(filtered, base=2)
    filtered = _filter_down(rows, criterium_type="epsilon")
    scrubber = int(filtered, base=2)
    return oxygen * scrubber


if __name__ == "__main__":
    with open("input.txt") as txt:
        rows = txt.read().split()
    print(life_support(rows))
