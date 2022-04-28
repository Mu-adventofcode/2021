with open("input.txt") as f:
    data = [[int(d) for d in row.strip()] for row in f]

(max_x, max_y) = (len(data[0]) - 1, len(data) - 1)
inf = float("inf")

risk_levels = [
    height + 1
    for y, row in enumerate(data)
    for x, height in enumerate(row)
    if height
    < min(
        data[y][x - 1] if x > 0 else inf,
        data[y][x + 1] if x < max_x else inf,
        data[y - 1][x] if y > 0 else inf,
        data[y + 1][x] if y < max_y else inf,
    )
]

print(sum(risk_levels))
