"""
This solution makes use of networkx's ability to split up graphs into connected
components. The script scans through the matrix of heights. It locally connects
points that will be the same basin. Eventually the networkx components will
correspond to basins.
"""
import networkx as nx
from functools import reduce


with open("input.txt") as f:
    data = [[int(d) for d in row.strip()] for row in f]
max_x = len(data[0]) - 1
max_y = len(data) - 1
connections = set()

# Scan all points in the data and create connections.
for y, row in enumerate(data):
    for x, height in enumerate(row):
        if height == 9:
            continue
        # Create a small set: 1 to 5 neighboring points around (y, x). Because
        # points at height 9 are excluded, this will be a subset of a basin.
        subset = set(
            point
            for point in [
                (y, x),
                (y, x - 1) if x > 0 else (y, x),
                (y, x + 1) if x < max_x else (y, x),
                (y - 1, x) if y > 0 else (y, x),
                (y + 1, x) if y < max_y else (y, x),
            ]
            if data[point[0]][point[1]] != 9
        )
        # Connect the points of the subset.  As a point will be in other
        # subsets too, eventually all points within one basin will become
        # (directly or indirectly) connected.
        llg = list(subset)
        for conn in zip(llg, llg[1:]):
            connections.add(conn)

# Create a graph and split it up into its distinct components (=basins).
G = nx.Graph()
G.add_edges_from(connections)
basins = nx.connected_components(G)
basin_sizes = [len(b) for b in basins]
basin_sizes.sort(reverse=True)
result = reduce(lambda x, y: x * y, basin_sizes[:3])
print(result)
