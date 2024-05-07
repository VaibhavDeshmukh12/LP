class BfsDfs:

    def __init__(self):
        self.vis = []

    def generate_graph(self):
        g = {}
        vertices = int(input("Enter the number of vertices: "))
        for i in range(vertices):
            edges = list(map(int, input(f"Enter the vertices connected to vertex {i}: ").split()))
            g[i] = edges
        self.vis = [False] * vertices 
        return g

    def dfs(self, g, s):
        self.vis[s] = True
        print(s, end=" ")
        for c in g[s]:
            if not self.vis[c]:
                self.dfs(g, c)

    def bfs(self, g, s):
        q = [s]
        visit = [s]
        print("\nBFS: ")
        while q:
            curr = q.pop(0)
            print(curr, end=" ")
            for c in g[curr]:
                if c not in visit:
                    q.append(c)
                    visit.append(c)

obj = BfsDfs()
g = obj.generate_graph()
s = int(input("\nEnter Starting Vertex: "))
print("\nDFS:")
obj.dfs(g, s)
obj.bfs(g, s)
