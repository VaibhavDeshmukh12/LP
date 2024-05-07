class Graph:
    def __init__(self, vertices):
        self.n = vertices
        self.graph = [[] for _ in range(vertices)]

    def add_edge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)

    def is_safe(self, v, color, c):
        for i in self.graph[v]:
            if color[i] == c:
                return False
        return True

    def graph_coloring_util(self, color, v):
        if v == self.n:
            return True
        for c in range(1, self.n + 1):
            if self.is_safe(v, color, c):
                color[v] = c
                return self.graph_coloring_util(color, v + 1)

    def graph_coloring(self):
        color = [0] * self.n
        self.graph_coloring_util(color,0)
        print("The coloring is:")
        max_color = max(color)
        for v in range(self.n):
            print("Vertex", v, ":", "Color", color[v])
        print("Minimum number of colors required:", max_color)

V = int(input("Enter the number of vertices: "))
E = int(input("Enter the number of edges: "))

g = Graph(V)

print("Enter edges in the format 'source destination':")
for _ in range(E):
    u, v = map(int, input().split())
    g.add_edge(u, v)
g.graph_coloring()
