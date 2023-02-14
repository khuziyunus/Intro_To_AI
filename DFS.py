def dfs(visited, graph, node, dest, path):
    if node == dest:
        path.append(node)
        return True

    else:
        visited.add(node)
        path.append(node)
        for neighbor in graph[node]:
            if dfs(visited, graph, neighbor, dest, path):
                return True
        path.pop()
    return False

def find_path(graph, start, dest):
    visited = set()
    path = []
    if dfs(visited, graph, start, dest, path):
        return path
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
path = find_path(graph, start, dest)
if path:
    print("The path from", start, "to", dest, "is:")
    print(*path)
else:
    print("There is no path from", start, "to", dest)
