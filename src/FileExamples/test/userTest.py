from collections import deque

# TASK 1
graphFile = {}  # or use defaultdict(list)
with open('input.txt', 'r') as f:
    for l in f:
        n1, n2 = l.split()
        graphFile.setdefault(n1, set([])).add(n2)


# TASK 2
def bfs(graph, start):
    """Return the shortest distance from start to end in graph, which is
    represented as a mapping from a vertex to a list of adjacent
    vertices. If there is no path from start to end, raise NotFound.
    """
    # Mapping from v to shortest distance from start to v.
    distance = {start: 0}
    queue = deque([start])
    while queue:
        u = queue.popleft()
        d = distance[u] + 1
        for neighbour in graph[u]:
            if neighbour not in distance:
                distance[neighbour] = d
                queue.append(neighbour)
                if neighbour not in graph.keys():
                    return distance


distance = bfs(graphFile, 'A')
print(distance)

# TASK 3
print([key for key, value in sorted(distance.items(), key=lambda t: t[1], reverse=True)])
