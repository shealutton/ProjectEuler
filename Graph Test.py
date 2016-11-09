
# Depth first search, unordered results
def dfs_paths(graph, start, goal):
    stack = [(start, [start])]
    while stack:
        (vertex, path) = stack.pop()
        for next in graph[vertex] - set(path):
            if next == goal:
                yield path + [next]
            else:
                stack.append((next, path + [next]))


# Breadth first search, always returns shortest path first
def bfs_paths(graph, start, goal):
    queue = [(start, [start])]
    while queue:
        (vertex, path) = queue.pop(0)
        for next in graph[vertex] - set(path):
            if next == goal:
                yield path + [next]
            else:
                queue.append((next, path + [next]))


def shortest_path(graph, start, goal):
    try:
        return next(bfs_paths(graph, start, goal))
    except StopIteration:
        return None


graph = {'A': set(['B', 'C']),
         'B': set(['A', 'D', 'E']),
         'C': set(['A', 'F']),
         'D': set(['B']),
         'E': set(['B', 'F']),
         'F': set(['C', 'E'])}


# Depth first
print(list(dfs_paths(graph, 'A', 'F')))  # [['A', 'C', 'F'], ['A', 'B', 'E', 'F']]
# Breadth first
print(list(bfs_paths(graph, 'A', 'F')))  # [['A', 'C', 'F'], ['A', 'B', 'E', 'F']])
print(shortest_path(graph, 'A', 'F'))  # ['A', 'C', 'F']




