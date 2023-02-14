from collections import deque

def bfs(graph, start, dest):
    visited = set()
    queue = deque([(start, [start])])
    while queue:
        (node, path) = queue.popleft()
        if node == dest:
            return path
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, path + [neighbor]))
    return None

# Driver code
graph = {
    'A' : ['B','C'],
    'B' : ['D', 'E'],
    'C' : ['F'],
    'D' : [],
    'E' : ['F'],
    'F' : []
}

start = 'A'
dest = 'F'
path = bfs(graph, start, dest)
if path:
    print("The path from", start, "to", dest, "is:")
    print(*path)
else:
    print("There is no path from", start, "to", dest)
