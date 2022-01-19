from collections import defaultdict


class Graph:

    def __init__(self):
        self.graph = defaultdict(list)

    def add_edge(self, frm, to):
        self.graph[frm].append(to)

    def dfs(self, vertex):
        visited = [False] * len(self.graph)
        self._dfs_recursively(vertex, visited)

    def _dfs_recursively(self, vertex, visited):
        print(vertex, end=' ')
        visited[vertex] = True

        for n in self.graph[vertex]:
            if not visited[n]:
                visited[n] = True
                self._dfs_recursively(n, visited)

    def __repr__(self):
        return f"Graph({self.graph})"


g = Graph()
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 2)
g.add_edge(2, 0)
g.add_edge(2, 3)
g.add_edge(3, 3)

print(g)

g.dfs(2)
