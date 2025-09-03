import itertools

class ListGraph:
    def __init__(self, nodes):
        self.nodes = nodes
        self.adj = {v: [] for v in nodes}

    def add_edge(self, u, v):
        if v not in self.adj[u]:
            self.adj[u].append(v)
            self.adj[v].append(u)

    def remove_edge(self, u, v):
        self.adj[u] = [x for x in self.adj[u] if x != v]
        self.adj[v] = [x for x in self.adj[v] if x != u]

    def print(self):
        print("Adjacency List:")
        for v in self.nodes:
            print(v, "->", self.adj[v])

    def dfs(self, start, visited=None):
        if visited is None:
            visited = set()
        visited.add(start)
        print(start, end=" ")
        for neighbor in self.adj[start]:
            if neighbor not in visited:
                self.dfs(neighbor, visited)

    def get_vertices(self):
        return self.nodes

    def get_arestas(self):
        edges = []
        for v in self.nodes:
            for u in self.adj[v]:
                if self.nodes.index(u) > self.nodes.index(v):
                    edges.append([v, u])
        return edges

    def is_subgrafo(self, outro):
        for v in outro.get_vertices():
            if v not in self.nodes:
                return False
        for u, v in outro.get_arestas():
            if v not in self.adj[u]:
                return False
        return True

    def is_subgrafo_gerador(self, outro):
        if len(self.nodes) != len(outro.get_vertices()):
            return False
        for v in self.nodes:
            if v not in outro.get_vertices():
                return False
        for u, v in outro.get_arestas():
            if v not in self.adj[u]:
                return False
        return True

    def is_subgrafo_induzido(self, outro):
        if len(self.nodes) != len(outro.get_vertices()):
            return False
        for v in self.nodes:
            if v not in outro.get_vertices():
                return False
        for v in self.nodes:
            for u in self.nodes:
                if u != v:
                    tem_aqui = u in self.adj[v]
                    tem_outro = u in outro.adj[v]
                    if tem_aqui != tem_outro:
                        return False
        return True

    def is_null(self):
        for v in self.nodes:
            if len(self.adj[v]) > 0:
                return False
        return True

    def is_simple(self):
        for v in self.nodes:
            if v in self.adj[v]:
                return False
            if len(set(self.adj[v])) != len(self.adj[v]):
                return False
        return True

    def is_complete(self):
        n = len(self.nodes)
        for v in self.nodes:
            if len(self.adj[v]) != n - 1:
                return False
            for u in self.nodes:
                if u != v and u not in self.adj[v]:
                    return False
        return True

    def is_isomorfo(self, outro):
        if len(self.nodes) != len(outro.get_vertices()): #se nao tiver o mesmo numero de vertices
            return False
        if len(self.get_arestas()) != len(outro.get_arestas()): #edges =/ edges
            return False 
        
        for perm in itertools.permutations(outro.get_vertices()): #perm permutation
            mapping = dict(zip(self.nodes, perm))
            ok = True
            for u in self.nodes:
                for v in self.nodes:
                    if u != v:
                        have1 = v in self.adj[u]
                        have2 = mapping[v] in outro.adj[mapping[u]]
                        if have1 != have2:
                            ok = False
                            break
                if not ok:
                    break
            if ok:
                return True
            return False

if __name__ == "__main__":
    #print("=== TESTE 1: Grafo Original ===")
    #V = ["A", "B", "C", "D", "E"]
    #E = [["A", "B"], ["A", "C"], ["C", "D"], ["C", "E"], ["B", "D"]]

    #g = ListGraph(V)
    #for u, v in E:
    #    g.add_edge(u, v)

    #g.print()

    # Escolha quais métodos executar descomentando as linhas abaixo:

    # 1) DFS a partir do vértice "A"
    # print("\nDFS a partir de 'A':", end=" ")
    # g.dfs("A")
    # print()

    # 2) Verifica se o grafo é nulo
    # print("Grafo nulo?", g.is_null())

    # 3) Verifica se o grafo é simples
    # print("Grafo simples?", g.is_simple())

    # 4) Verifica se o grafo é completo
    # print("Grafo completo?", g.is_complete())

    # 5) Imprime vértices
    # print("Vértices:", g.get_vertices())

    # 6) Imprime arestas
    # print("Arestas:", g.get_arestas())

    # 7) isomorfo
    G1 = ListGraph(["A", "B", "C"])
    G1.add_edge("A", "B")
    G1.add_edge("B", "C")
    G1.add_edge("C", "A")

    G2 = ListGraph(["X", "Y", "Z"])
    G2.add_edge("X", "Y")
    G2.add_edge("Y", "Z")
    G2.add_edge("Z", "X")

    print("\n Grafo G1")
    G1.print()

    print("\n Grafo G2")
    G2.print()

    print("\nG1 é ismorfo a G2?", G1.is_isomorfo(G2))

    # --- Teste subgrafo ---

    #print("\n=== TESTE SUBGRAFO ===")
    #G1 = ListGraph(["A", "B", "C"])
    #G1.add_edge("A", "B")
    #G1.add_edge("B", "C")

    #G2 = ListGraph(["A", "B"])
    #G2.add_edge("A", "B")

    # Você também pode escolher qual método testar descomentando abaixo:

    # print("G2 é subgrafo de G1?", G1.is_subgrafo(G2))
    # print("G2 é subgrafo gerador de G1?", G1.is_subgrafo_gerador(G2))
    # print("G2 é subgrafo induzido de G1?", G1.is_subgrafo_induzido(G2))