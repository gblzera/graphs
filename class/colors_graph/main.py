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
        if v in self.adj[u]:
            self.adj[u].remove(v)
        if u in self.adj[v]:
            self.adj[v].remove(u)

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

    # --- Propriedades ---
    def is_null(self):
        return all(len(self.adj[v]) == 0 for v in self.nodes)

    def is_simple(self):
        for v in self.nodes:
            if v in self.adj[v]:   # laço
                return False
            if len(set(self.adj[v])) != len(self.adj[v]):  # paralelas
                return False
        return True

    def is_complete(self):
        n = len(self.nodes)
        for v in self.nodes:
            if len(self.adj[v]) != n - 1:
                return False
        return True

    # --- Subgrafos ---
    def is_subgrafo(self, outro):
        for v in outro.get_vertices():
            if v not in self.nodes:
                return False
        for u, v in outro.get_arestas():
            if v not in self.adj[u]:
                return False
        return True

    def is_subgrafo_gerador(self, outro):
        return set(self.nodes) == set(outro.get_vertices()) and self.is_subgrafo(outro)

    def is_subgrafo_induzido(self, outro):
        if set(self.nodes) != set(outro.get_vertices()):
            return False
        for u in self.nodes:
            for v in self.nodes:
                if u != v:
                    if (v in self.adj[u]) != (v in outro.adj[u]):
                        return False
        return True

    # --- Isomorfismo ---
    def is_isomorfo(self, outro):
        if len(self.nodes) != len(outro.get_vertices()):
            return False
        if len(self.get_arestas()) != len(outro.get_arestas()):
            return False

        for perm in itertools.permutations(outro.get_vertices()):
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
    
    # -- Coloração via backtracking ---
    def is_safe(self, v, color, assignment):
        """faz a verificação se a cor pode ser atribuida ao node sem conflito"""
        for neighbor in self.adj[v]:
            if neighbor in assignment and assignment[neighbor] == color:
                return False
        return True
    
    def graph_coloring_util(self, m, assignment, index):
        """backtracking recursivo"""
        if index == len(self.nodes):
            return True # todas as cores foram atribuidas
        
        v = self.nodes[index]
        for c in range(1, m + 1): # tenta as cores de 1 até m
            if self.is_safe(v, c, assignment):
                assignment[v] = c
                if self.graph_coloring_util(m, assignment, index + 1):
                    return True
                assignment[v] = 0 # backtrack
        return False
    
    def graph_coloring(self):
        """tenta colorir o grafo com o menor numero de cores"""
        for m in range(1, len(self.nodes) + 1): # no maximo n cores
            assignment = {v: 0 for v in self.nodes}
            if self.graph_coloring_util(m, assignment, 0):
                return m, assignment
        return len(self.nodes), {v: i+1 for i, v in enumerate(self.nodes)} 

if __name__ == "__main__":
    aulas = ['M', 'A', 'C', 'F', 'Q', 'P']
    g = ListGraph(aulas)

    # CONFLITOS
    g.add_edge('C', 'F') #calculo e fisica
    g.add_edge('C', 'A') #calculo e algebra
    g.add_edge('M', 'A') #matematica e algebra
    g.add_edge('M', 'P') #matematica e programação
    g.add_edge('P', 'A') #programação e algebra
    g.add_edge('Q', 'F') #quimica e fisica
    g.add_edge('F', 'A') #fisica e algebra

    print("\n--- Grafos de Conflitos ---")
    g.print()

    print("\n--- Coloração do Grafo ---")
    min_colors, assignment = g.graph_coloring()
    print(f"Númeor mínimo de horários necessários: (número cromático χ(G)): {min_colors}")
    print("Atribuição de horários (cores) às aulas:", assignment)
