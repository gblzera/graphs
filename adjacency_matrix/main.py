class Graph:
    def number_of_edges(self):
        raise NotImplementedError
    
    def number_of_vertices(self):
        raise NotImplementedError
    
    def degree_sequence(self):
        raise NotImplementedError
    
    def add_edge(self, u, v):
        raise NotImplementedError
    
    def remove_edge(self, u, v):
        raise NotImplementedError
    
    def print(self):
        raise NotImplementedError

class DenseGraph(Graph):
    def __init__(self, nodes):
        self.rotules = nodes
        self.n = len(nodes)
        self.matrix = [[0] * self.n for _ in range(self.n)]

    def number_of_nodes(self):
        return self.n
    
    def number_of_egdes(self):
        return sum(sum(row) for row in self.matrix) // 2
    
    def degree_sequence(self):
        return [sum(row) for row in self.matrix]
    
    def add_edge(self, u, v):
        i, j = self.rotules.index(u), self.rotules.index(v)
        if self.matrix[i][j] == 0:
            self.matrix[i][j] = self.matrix[j][i] = 1
    
    def remove_edge (self, u, v):
        i, j = self.rotules.index(u), self.rotules.index(v)
        if self.matrix[i][j] == 1:
            self.matrix[i][j] = self.matrix[j][i] = 0

    def print(self):
        print("Adjacency Matrix:")
        print("  ", " ".join(self.rotules))
        for i, row in enumerate(self.matrix):
            print(self.rotules[i], row)


# test
V = ["A", "B", "C", "D", "E"]
E = [("A","B"), ("A","C"), ("C","D"), ("C","E"), ("B","D")]

g = DenseGraph(V)
for u, v in E:
    g.add_edge(u, v)

g.print()
print("Number of nodes:", g.number_of_nodes())
print("Number of edges:", g.number_of_egdes())
print("Degree sequence:", g.degree_sequence())

print("\nRemoving edge (A,C)...")
g.remove_edge("A", "C")
g.print()