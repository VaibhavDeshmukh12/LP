import sys

class Graph: 
    def __init__(self,vertices):
        self.V = vertices
        self.graph = [[0 for _ in range(vertices)] for _ in range(vertices)]
    
    def min_key(self,key,mst_key):
        min_value = sys.maxsize
        min_index = None
        for v in range(self.V):
            if key[v] < min_value and not mst_key[v]:
                min_value = key[v]
                min_index = v
        return min_index
    
    def prims_mst(self):
        key = [sys.maxsize] * self.V
        parent = [None] * self.V
        key[0] = 0
        parent[0] = - 1
        mst_key = [False] * self.V

        for _ in range(self.V):
            u = self.min_key(key,mst_key)
            mst_key[u] = True
            for v in range(self.V):
                if self.graph[u][v] > 0 and not mst_key[v] and key[v] > self.graph[u][v]:
                    key[v] = self.graph[u][v]
                    parent[v] = u
        print("Edge \t Weight")
        for i in range(1,self.V):
            print(f"{parent[i]} - {i} \t {self.graph[i][parent[i]]}")

v = int(input("Enter number of vertices: "))
g = Graph(v)

print("Enter adjacency matrix: ")
for i in range(v):
    g.graph[i] = list(map(int,input().split()))

g.prims_mst()