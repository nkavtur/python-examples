from collections import defaultdict


class Graph:

    def __init__(self, num):
        self.num = num
        self.graph = defaultdict(list)

    def add_edge(self, frm, to):
        self.graph[frm].append(to)

    def has_cycle(self):
        memo = set()

        for v in list(self.graph):
            if v not in memo:
                visited = set()
                if self.has_cycle_recursively(v, memo, visited):
                    return True
        return False

    def has_cycle_recursively(self, vertex, memo, visited):
        print(vertex, end=' ')
        if vertex in visited:
            return True

        if vertex not in memo:
            memo.add(vertex)
            visited.add(vertex)

            for n in self.graph[vertex]:
                return self.has_cycle_recursively(n, memo, visited)

    def __repr__(self):
        return f"Graph({self.graph})"


# 1
# g = Graph(4)
# g.add_edge(0, 1)
# g.add_edge(0, 2)
# g.add_edge(1, 2)
# g.add_edge(2, 0)
# g.add_edge(2, 3)
# g.add_edge(3, 3)
# print(g.has_cycle())

# 2
# g1 = Graph(8)
# g1.add_edge(0, 1)
# g1.add_edge(0, 2)
# g1.add_edge(1, 2)
# g1.add_edge(2, 3)
#
# g1.add_edge(4, 5)
# g1.add_edge(5, 1)
#
# g1.add_edge(6, 7)
#
# print(g1.has_cycle())


# 3
g2 = Graph(4)
g2.add_edge(0, 1)
g2.add_edge(1, 2)
g2.add_edge(2, 3)
g2.add_edge(0, 2)
print(g2.has_cycle())
