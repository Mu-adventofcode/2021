from collections import Counter


def _most_commons(cols):
    """Given a list of column strings, returns a list of most common values."""

    return [Counter(col).most_common(1)[0][0] for col in cols]


def _complement(b):
    return "1" if b == "0" else "0"


def power_consumption(rows):
    """Given a list of row strings, returns the power consumption."""

    columns = ["".join(tpl) for tpl in zip(*rows)]
    gamma_bits = "".join(_most_commons(columns))
    epsil_bits = "".join(_complement(bit) for bit in gamma_bits)
    gamma_value = int(gamma_bits, base=2)
    epsil_value = int(epsil_bits, base=2)
    return gamma_value * epsil_value


if __name__ == "__main__":
    with open("input.txt") as txt:
        rows = txt.read().split()
    print(power_consumption(rows))  # 2743844
