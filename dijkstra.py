import sys

class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[0 for column in range(vertices)] for row in range(vertices)]

    def print_solution(self, dist,parent):
        print("Vertex \tDistance from Source")
        for node in range(1,self.V):
            print(parent[node],"--",node, "\t", dist[node])

    def min_distance(self, dist, spt_set):
        min_val = sys.maxsize
        min_index = - 1

        for v in range(self.V):
            if dist[v] < min_val and spt_set[v] is False:
                min_val = dist[v]
                min_index = v
        return min_index

    def dijkstra(self, src):
        dist = [sys.maxsize] * self.V
        dist[src] = 0
        parent = [-1] * self.V
        spt_set = [False] * self.V

        for _ in range(self.V):
            u = self.min_distance(dist, spt_set)
            spt_set[u] = True
            for v in range(self.V):
                if self.graph[u][v] > 0 and not spt_set[v] and dist[v] > dist[u] + self.graph[u][v]:
                    dist[v] = dist[u] + self.graph[u][v]
                    parent[v] = u

        self.print_solution(dist,parent)

def main():
    num_vertices = int(input("Enter the number of vertices: "))
    g = Graph(num_vertices)

    print("Enter the adjacency matrix of the graph:")
    for i in range(num_vertices):
        g.graph[i] = list(map(int, input().split()))

    source = int(input("Enter the source vertex: "))
    g.dijkstra(source)

if __name__ == "__main__":
    main()
