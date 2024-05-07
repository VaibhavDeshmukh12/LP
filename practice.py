# Job sheduling
"""
def jobSheduling(arr,t):

    result = [False] * t
    job = ['-1'] * t
    total_profit = 0
    
    for i in range(len(arr)):
        for j in range(min(t-1,arr[i][1]-1),-1,-1):
            if result[j] is False:
                result[j] = True
                job[j] = arr[i][0]
                total_profit += arr[i][2]
                break
    print("\nJob sequence: ",job)
    print("Max profit: ",total_profit)

n = int(input("Enter total number of jobs: "))
arr = []
print("\nEnter job details in format 'job_id deadline profit'")
for _ in range(n):
    job_id, deadline, profit = input().split()
    arr.append((job_id,int(deadline),int(profit)))

jobSheduling(arr,max(job[1] for job in arr))

"""

# prims
"""
import sys
class Prims:
    def __init__(self,vertices):
        self.V = vertices
        self.graph = [[0 for _ in range(vertices)] for _ in range(vertices)]
        # print(self.graph)
    
    def min_key(self,dist,visited):
        min_value = sys.maxsize
        min_index = - 1

        for i in range(self.V):
            if dist[i] < min_value and not visited[i]:
                min_value = dist[i]
                min_index = i
        return min_index

    def prims_mst(self):
        dist = [sys.maxsize] * self.V
        parent = [-1] * self.V
        visited = [False] * self.V
        dist[0] = 0
        
        for _ in range(self.V):
            u = self.min_key(dist,visited)
            visited[u] = True
            for v in range(self.V):
                if (self.graph[u][v] > 0 and not visited[v] and dist[v] > self.graph[u][v]):
                    dist[v] = self.graph[u][v]
                    parent[v] = u
        print("\nEdges\tDistance")
        for i in range(1,self.V):
            print(f"{parent[i]} -- {i}\t{self.graph[i][parent[i]]}")

v = int(input("\nEnter number of vertices: "))

prm = Prims(v)

print("Enter adjacency matrix: ")
for i in range(v):
    prm.graph[i] = list(map(int,input().split()))

prm.prims_mst()
"""

# Dijkstras
"""
import sys
class Dijkstra:
    def __init__(self,v):
        self.V = v
        self.graph = [[0 for _ in range(v)] for _ in range(v)]
    
    def display(self,dist):
        print("\nVertex\t Distance from source")
        for node in range(self.V):
            print(f"{node} \t {dist[node]}")

    def min_key(self,dist,visited):
        min_value = sys.maxsize
        min_index = -1
        for i in range(self.V):
            if dist[i] < min_value and not visited[i]:
                min_value = dist[i]
                min_index = i
        return min_index
    
    def dijkstras(self,source):
        visited = [False] * self.V
        distance = [sys.maxsize] * self.V
        distance[source] = 0
        
        for _ in range(self.V):
            u = self.min_key(distance,visited)
            visited[u] = True
            for v in range(self.V):
                if (self.graph[u][v] > 0 and not visited[v] and distance[v] > self.graph[u][v] + distance[u]): 
                    distance[v] = self.graph[u][v] + distance[u]
        self.display(distance)

v = int(input("\nEnter total number of vertices: "))

dij = Dijkstra(v)

print("\nEnter adjacency matrix: ")
for i in range(v):
    dij.graph[i] = list(map(int,input().split()))

src = int(input("Enter source vertex: "))
dij.dijkstras(src)
"""

# Graph coloring
"""
class Graph:
    def __init__(self,vertices):
        self.V = vertices
        self.graph = [[] for _ in range(vertices)]
    
    def add_edge(self,u,v):
        self.graph[u].append(v)
        self.graph[v].append(u)
    
    def is_safe(self,v,color,c):
        for i in self.graph[v]:
            if color[i] == c:
                return False
        return True
    
    def graph_coloring_util(self,color,v):
        if self.V == v:
            return True
        
        for c in range(1,self.V+1):
            if self.is_safe(v,color,c):
                color[v] = c
                return self.graph_coloring_util(color,v+1)

    def graph_coloring(self):
        color = [0] * self.V
        self.graph_coloring_util(color,0)
        print("\nVertex\t Color")
        for c in range(self.V):
            print(f"{c}  \t  {color[c]}")
        print("Minimum color required: ",max(color))

v = int(input("\nEnter number of vertices: "))
e = int(input("Enter total number of edges: "))
obj = Graph(v)

print("Enter edges (u v): ")
for _ in range(e):
    u,v = map(int,input().split())
    obj.add_edge(u,v)

obj.graph_coloring()
"""

class DfsBfs:
    def __init__(self):
        self.vis = []
    
    def generate_graph(self):
        v = int(input("\nEnter number of vertices: "))
        self.vis = [False] * v
        g = {}
        for i in range(v):
            edges = list(map(int,input(f"Enter vertices adjacent to {i}: ").split()))
            g[i] = edges
        return g
    
    def dfs(self,g,s):
        self.vis[s] = True
        print(s,end=" ")
        for c in g[s]:
            if not self.vis[c]:
                self.dfs(g,c)
    
    def bfs(self,g,s):
        q = [s]
        visited = [s]
        
        while q:
            curr = q.pop(0)
            print(curr,end=" ")
            for c in g[curr]:
                if c not in visited:
                    q.append(c)
                    visited.append(c)

obj = DfsBfs()
g = obj.generate_graph()
obj.dfs(g,0)
print("\nBFS:")
obj.bfs(g,0)