from collections import defaultdict


class Graph:

    def __init__(self, num):
        self.num = num
        self.graph = defaultdict(list)

    def add_edge(self, frm, to):
        self.graph[frm].append(to)

    def count_paths(self, s, d):
        visited = set()
        all_paths = []
        path = []
        self.count_paths_recursively(s, d, visited, all_paths, path)
        print()
        return all_paths

    def count_paths_recursively(self, s, d, visited, all_paths, path):
        # print(s, end=' ')
        visited.add(s)
        path.append(s)

        if s == d:
            all_paths.append(path.copy())

        else:
            for n in self.graph[s]:
                if n not in visited:
                    self.count_paths_recursively(n, d, visited, all_paths, path)

        visited.remove(s)
        path.pop()

    def __repr__(self):
        return f"Graph({self.graph})"


# 1
g = Graph(4)
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(0, 3)
g.add_edge(2, 0)
g.add_edge(2, 1)
g.add_edge(1, 3)

print(g.count_paths(s=2, d=3))
