from collections import defaultdict


class Graph:

    def __init__(self, num):
        self.num = num
        self.graph = defaultdict(list)

    def add_edge(self, frm, to):
        self.graph[frm].append(to)
        self.graph[to].append(frm)

    def has_cycle(self):
        memo = set()
        for vertex in list(self.graph):
            if vertex not in memo:
                print()
                visited = set()
                if self.has_cycle_recursively(vertex, -1, visited, memo):
                    print()
                    return True

        print()
        return False

    def has_cycle_recursively(self, vertex, parent, visited, memo):
        print(vertex, end=' ')
        if vertex in visited:
            return True

        if vertex not in memo:
            memo.add(vertex)
            visited.add(vertex)
            for n in self.graph[vertex]:
                if n != parent:
                    if self.has_cycle_recursively(n, vertex, visited, memo):
                        return True

        visited.remove(vertex)

    def __repr__(self):
        return f"Graph({self.graph})"


# 1
g = Graph(4)
g.add_edge(0, 1)
g.add_edge(1, 2)
g.add_edge(2, 3)
g.add_edge(0, 2)
print(g.has_cycle())

# 2
g1 = Graph(3)
g1.add_edge(0, 1)
g1.add_edge(1, 2)
g1.add_edge(2, 3)
print(g1.has_cycle())

