from collections import defaultdict


class Graph:

    def __init__(self, num):
        self.num = num
        self.graph = defaultdict(list)
        self.tc = [[0] * num for i in range(num)]

    def add_edge(self, frm, to):
        self.graph[frm].append(to)

    def transitive_closure(self):
        for vertex in range(self.num):
            self.dfs(vertex, vertex)

    def dfs(self, u, v):
        if u == v:
            self.tc[u][v] = 1
        else:
            self.tc[u][v] = 1

        for n in self.graph[v]:
            if not self.tc[u][n]:
                self.dfs(u, n)

    def __repr__(self):
        return f"Graph({self.graph})"


# 1
g = Graph(4)
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 2)
g.add_edge(2, 0)
g.add_edge(2, 3)
g.add_edge(3, 3)

g.transitive_closure()

print(g.tc)
