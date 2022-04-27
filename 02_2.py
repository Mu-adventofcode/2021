class Position:
    def __init__(self, horpos=0, depth=0, aim=0):
        self.horpos = horpos
        self.depth = depth
        self.aim = aim

    def step(self, string):
        direction, amount = string.split()
        if direction == "forward":
            self.horpos += int(amount)
            self.depth += self.aim * int(amount)
        elif direction == "up":
            self.aim -= int(amount)
        elif direction == "down":
            self.aim += int(amount)
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
