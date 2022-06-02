graph = {'5' : ['7','2'], '3' : ['2', '4'], '7' : ['8'], '2' : [], '4' : ['8'], '8' : []}

visited = []
queue = []

def bfs(visited, graph, node):
  visited.append(node)
  queue.append(node)

  while queue:
    m = queue.pop(0)
    print (m, end = ", ")

    for neighbour in graph[m]:
      if neighbour not in visited:
        visited.append(neighbour)
        queue.append(neighbour)
print("Graph:", graph)
print("BFS traversal of graph with source 5:")
bfs(visited, graph, '5')