from collections import defaultdict, deque


class Graph:

    def __init__(self):
        self.graph = defaultdict(list)

    def add_edge(self, frm, to):
        self.graph[frm].append(to)

    def bfs(self, vertex):
        visited = [False] * len(self.graph)
        visited[vertex] = True

        queue = deque([vertex])
        while queue:
            level_size = len(queue)

            for i in range(level_size):
                current = queue.popleft()
                print(current, end=' ')

                for n in self.graph[current]:
                    if not visited[n]:
                        visited[n] = True
                        queue.append(n)

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


g.bfs(2)
