import sys
class Dijkstra:
    def __init__(self,vertices):
        self.v = vertices
        self.graph = [[0 for _ in range(vertices)] for _ in range(vertices)]
    
    def display(self,distance):
        print('Vertex \tDistance from source')
        for node in range(self.v):
            print(node,"\t ",distance[node])
    
    def min_node(self,distance,visited):
        min_value = sys.maxsize
        min_index = -1
        
        for i in range(self.v):
            if distance[i] < min_value and not visited[i]:
                min_value = distance[i]
                min_index = i
        return min_index
    
    def dijkstra(self,source):
        visited = [False] * self.v
        distance = [sys.maxsize] * self.v
        distance[source] = 0
        
        for _ in range(self.v):
            u = self.min_node(distance,visited)
            visited[u] = True
            for v in range(self.v):
                if self.graph[u][v] > 0 and not visited[v] and distance[v] > self.graph[u][v]+distance[u]:
                    distance[v] = self.graph[u][v] + distance[u]
        self.display(distance)

v = int(int(input("\nEnter total number of vertices: ")))

g = Dijkstra(v)

print("Enter adjacency matrix: ")

for i in range(v):
    g.graph[i] = list(map(int,input().split()))

src = int(input("\nEnter source vertex: "))
g.dijkstra(src)












# class Graph:
#     def __init__(self,vertices):
#         self.V = vertices
#         self.graph = [[] for _ in range(vertices)]
    
#     def add_edge(self,u,v):
#         self.graph[u].append(v)
#         self.graph[v].append(u)
    
#     def is_safe(self,v,color,c):
#         for i in self.graph[v]:
#             if color[i] == c:
#                 return False
#         return True
    
#     def graph_coloring_util(self,color,v):
#         if self.V == v:
#             return True
#         for c in range(1,self.V+1):
#             if self.is_safe(v,color,c):
#                 color[v] = c
#                 return self.graph_coloring_util(color,v+1)
    
#     def graph_coloring(self):
#         color = [0] * self.V
#         self.graph_coloring_util(color,0)
#         print("\nVertex\tColor")
#         for i in range(self.V):
#             print(i,"\t",color[i])
        
#         print("Minimum color required: ",max(color))

# v = int(input("\nEnter total number of vertices: "))
# e = int(input("Enter number of edges: "))

# obj = Graph(v)

# print("\nEnter edges (u v): ")
# for i in range(e):
#     u,v = map(int,input().split())
#     obj.add_edge(u,v)

# obj.graph_coloring()





# import sys

# class Prims:
#     def __init__(self,v):
#         self.V = v
#         self.graph = [[0 for _ in range(v)] for _ in range(v)]

#     def find_min_index(self,dist,visited):
#         min_value = sys.maxsize
#         min_index = None
        
#         for v in range(self.V):
#             if dist[v] < min_value and not visited[v]:
#                 min_index = v
#                 min_value = dist[v]
#         return min_index

#     def prims_mst(self):
#         dist = [sys.maxsize] * self.V
#         parent = [None] * self.V
#         visited = [False] * self.V
        
#         dist[0] = 0
#         parent[0] = -1
        
#         for _ in range(self.V):
#             u = self.find_min_index(dist,visited)
#             visited[u] = True
#             for v in range(self.V):
#                 if self.graph[u][v] > 0 and dist[v] > self.graph[u][v] and not visited[v]:
#                     dist[v] = self.graph[u][v]
#                     parent[v] = u
#         print("\nEdges \t Weight")
#         for i in range(1,self.V):
#             print(f"{parent[i]} - {i} \t {self.graph[i][parent[i]]}")

# v = int(input("\nEnter total number of vertices: "))

# obj = Prims(v)
# print("Enter adjacency matrix: ")
# for i in range(v):
#     obj.graph[i] = list(map(int,input().split()))

# obj.prims_mst()


# def jobSheduling(arr,t):
    
#     arr.sort(key=lambda x:x[2],reverse=True)    
#     result = [False] * t
#     job = ['-1'] * t
#     total_profit = 0
    
#     for i in range(len(arr)):
#         for j in range(min(t-1,arr[i][1]-1),-1,-1):
#             if result[j] is False:
#                 result[j] = True
#                 job[j] = arr[i][0]
#                 total_profit += arr[i][2]
#                 break
#     print("\nJob Sequence: ",job)
#     print("Maximum profit: ",total_profit)

# n = int(input("Enter total number of jobs: "))
# arr = []

# print("\nEnter job details in format 'job_id deadline profit'")
# for i in range(n):
#     job_id,deadline,profit = input().split()
#     arr.append((job_id,int(deadline),int(profit)))

# jobSheduling(arr,max(job[1] for job in arr))

# class BFS_DFS:
    
#     def __init__(self,vertices):
#         self.V = vertices
#         self.visited = [False] * vertices

#     def generate_graph(self):
#         g = {}
#         for i in range(self.V):
#             edges = list(map(int,input(f"\nEnter vertices connected to {i}: ").split()))
#             g[i] = edges
#         return g

#     def dfs(self,g,s):
#         self.visited[s] = True
#         print(s,end=" ")
#         for c in g[s]:
#             if not self.visited[c]:
#                 self.dfs(g,c)
    
#     def bfs(self,g,s):
#         q = [s]
#         visit = [s]
        
#         while q:
#             curr = q.pop(0)
#             print(curr,end=" ")
#             for c in g[curr]:
#                 if c not in visit:
#                     q.append(c)
#                     visit.append(c)

# v = int(input("Enter total number of vertices: "))

# obj = BFS_DFS(v)
# graph = obj.generate_graph()

# s = int(input("\nEnter starting vertex: "))
# print("\nDfs: ")
# obj.dfs(graph,s)
# print("\nBFS: ")
# obj.bfs(graph,s)