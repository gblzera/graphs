class ListGraph:
    def __init__ (self, nodes):
        self.nodes = nodes
        self.adj = {v: [] for v in nodes}

    def add_edge(self, u, v):
        if v not in self.adj[u]:
            self.adj[u].append(v)
            self.adj[v].append(u)  # undirected graph

    def remove_edge(self, u, v):
        if v in self.adj[u]:
            self.adj[u].remove(v)
        if v in self.adj[v]:    
            self.adj[v].remove(u)

    def print(self):
        print("Adjacency List:")
        for v in self.nodes:
            print(v, "->", self.adj[v])
    
    def dfs(self, start, visited=None):
        if visited is None:
            visited = set()
        visited.add(start)
        print(start, end=' ')
        for neighbor in self.adj[start]:
            if neighbor not in visited:
                self.dfs(neighbor, visited)

# test
V = ["A","B","C","D","E"]
E = [("A","B"), ("A","C"), ("C","D"), ("C","E"), ("B","D")]

g = ListGraph(V)
for (u,v) in E:
    g.add_edge(u,v)

g.print()
print("\nDFS starting from node A:")
g.dfs("A")

print("\n\nRemovinf edge (A,C)...")
g.remove_edge("A", "C")
g.print()
print("\nDFS starting from node A:")
g.dfs("A")
