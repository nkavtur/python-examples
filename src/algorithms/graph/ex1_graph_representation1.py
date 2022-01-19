class Graph:

    def __init__(self, n):
        self.n = n
        self.vertices_list = [0] * n
        self.vertices = {}
        self.adj_matrix = [[0] * n for i in range(n)]

    def set_vertex(self, vtx, id):
        self.vertices[id] = vtx
        self.vertices_list[vtx] = id

    def set_edge(self, frm, to):
        fmt_vtx = self.vertices[frm]
        to_vtx = self.vertices[to]
        print(fmt_vtx, to_vtx)
        self.adj_matrix[fmt_vtx][to_vtx] = 1
        self.adj_matrix[to_vtx][fmt_vtx] = 1

    def get_vertex(self):
        return self.vertices_list

    def get_edges(self):
        edges = []
        for i in range(self.n):
            for j in range(self.n):
                if self.adj_matrix[i][j]:
                    edges.append([self.vertices_list[i], self.vertices_list[j]])

        return edges


G = Graph(6)

G.set_vertex(0, 'a')
G.set_vertex(1, 'b')
G.set_vertex(2, 'c')
G.set_vertex(3, 'd')
G.set_vertex(4, 'e')
G.set_vertex(5, 'f')

G.set_edge('a', 'e')
G.set_edge('a', 'c')
G.set_edge('c', 'b')
G.set_edge('b', 'e')
G.set_edge('e', 'd')
G.set_edge('f', 'e')

print(G.get_edges())

