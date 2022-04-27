class Position:
    """
    The position of the vessel.
    """

    def __init__(self, horpos=0, depth=0):
        self.horpos = horpos
        self.depth = depth

    def step(self, string):
        direction, amount = string.split()
        if direction == "forward":
            self.horpos += int(amount)
        elif direction == "up":
            self.depth -= int(amount)
        elif direction == "down":
            self.depth += int(amount)
        else:
            raise ValueError("unknown direction")

    def result(self):
        return self.horpos * self.depth


if __name__ == "__main__":
    p = Position(0, 0)
    with open("input.txt") as txt:
        course = txt.readlines()
    for step in course:
        p.step(step)
    print(p.result())
