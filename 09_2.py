"""
This solution for the 2nd part of day 9 makes use of networkx's ability to
split up graphs into its connected components.

First, the concept of 'wall points' is introduced: wall points are points of
height == 9, and extra wall points surrounding the data matrix are added. This
script scans the matrix and locally connects non wall points.

Connections will be edges for a networkx graph.  Eventually the individual
networkx connected components will correspond to the puzzle's basins.
"""
import networkx as nx

with open("input.txt") as f:
    matrix = [[int(d) for d in row.strip()] for row in f]

walls = [[1 if d == 9 else 0 for d in row] for row in matrix]
walls = [[1] + row + [1] for row in walls]
dx = len(walls[0])
walls = [[1] * dx] + walls + [[1] * dx]
dy = len(walls)

wall_points = set((y, x) for y in range(dy) for x in range(dx) if walls[y][x])
connections = set()

for y in range(1, dy - 1):
    for x in range(1, dx - 1):
        if (y, x) in wall_points:
            continue
        neighb = set(((y, x), (y - 1, x), (y + 1, x), (y, x - 1), (y, x + 1)))
        neighb -= wall_points
        for conn in zip(list(neighb), list(neighb)[1:]):
            connections.add(conn)

G = nx.Graph()
G.add_edges_from(connections)
basins = nx.connected_components(G)
basin_sizes = sorted([len(b) for b in basins], reverse=True)
print(basin_sizes[0] * basin_sizes[1] * basin_sizes[2])
