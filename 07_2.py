def crab_cost(end_pos, pos):
    # Uses this trick: 1+2+...+7+8 = (1+8)+(2+7)+... = 9+9+9+9 = 9*4
    delta = abs(end_pos - pos)
    cost = (1 + delta) * (delta // 2)
    if delta % 2:
        cost += (delta // 2) + 1  # add middle value
    return cost


def total_cost(end_p, crab_positions):
    return sum(crab_cost(end_p, cp) for cp in crab_positions)


crab_positions = [
    int(p) for p in open("input.txt").read().strip().split(",")
]
totals = [
    total_cost(end_p, crab_positions)
    for end_p in range(min(crab_positions), 1 + max(crab_positions))
]
print(min(totals))
