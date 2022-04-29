"""
This solution makes use of networkx's ability to split up graphs into connected
components. The script scans all matrix points. It locally connects points that
are lower than 9. The distinct networkx components will correspond to basins.
"""
import networkx as nx

with open("input.txt") as f:
    matrix = [[int(d) for d in row.strip()] for row in f]

walls = [[1 if d == 9 else 0 for d in row] for row in matrix]
walls = [[1] + row + [1] for row in walls]
dx = len(walls[0])
walls = [[1] * dx] + walls + [[1] * dx]
dy = len(walls)

connections = set()
for y in range(1, dy - 1):
    for x in range(1, dx - 1):
        if walls[y][x]:
            continue
        cross = set(((y, x), (y - 1, x), (y + 1, x), (y, x - 1), (y, x + 1)))
        notwall = set((v, u) for (v, u) in cross if not walls[v][u])
        llg = list(notwall)
        for conn in zip(llg, llg[1:]):
            connections.add(conn)

G = nx.Graph()
G.add_edges_from(connections)
basins = nx.connected_components(G)
basin_sizes = sorted([len(b) for b in basins], reverse=True)
print(basin_sizes[0] * basin_sizes[1] * basin_sizes[2])
