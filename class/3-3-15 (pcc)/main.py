import itertools
import heapq

class ListGraph:
    def __init__(self, nodes):
        self.nodes = nodes
        self.adj = {v: [] for v in nodes}

    def add_edge(self, u, v, w=1):
        if v not in [x[0] for x in self.adj[u]]:
            self.adj[u].append((v, w))
            self.adj[v].append((u, w))

    def remove_edge(self, u, v):
        self.adj[u] = [(x, w) for (x, w) in self.adj[u] if x != v]
        self.adj[v] = [(x, w) for (x, w) in self.adj[v] if x != u]

    def print(self):
        print("Adjacency List:")
        for v in self.nodes:
            print(v, "->", self.adj[v])

    def dfs(self, start, visited=None):
        if visited is None:
            visited = set()
        visited.add(start)
        print(start, end=" ")
        for (neighbor, _) in self.adj[start]:
            if neighbor not in visited:
                self.dfs(neighbor, visited)

    def get_vertices(self):
        return self.nodes

    def get_arestas(self):
        edges = []
        for v in self.nodes:
            for (u, w) in self.adj[v]:
                if self.nodes.index(u) > self.nodes.index(v):
                    edges.append([v, u, w])
        return edges

    # --- Propriedades ---
    def is_null(self):
        return all(len(self.adj[v]) == 0 for v in self.nodes)

    def is_simple(self):
        for v in self.nodes:
            vizinhos = [x[0] for x in self.adj[v]]
            if v in vizinhos:   # laço
                return False
            if len(set(vizinhos)) != len(vizinhos):  # paralelas
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
        for u, v, _ in outro.get_arestas():
            if v not in [x[0] for x in self.adj[u]]:
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
                    have1 = v in [x[0] for x in self.adj[u]]
                    have2 = v in [x[0] for x in outro.adj[u]]
                    if have1 != have2:
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
                        have1 = v in [x[0] for x in self.adj[u]]
                        have2 = mapping[v] in [x[0] for x in outro.adj[mapping[u]]]
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
        for (neighbor, _) in self.adj[v]:
            if neighbor in assignment and assignment[neighbor] == color:
                return False
        return True
    
    def graph_coloring_util(self, m, assignment, index):
        if index == len(self.nodes):
            return True
        v = self.nodes[index]
        for c in range(1, m + 1):
            if self.is_safe(v, c, assignment):
                assignment[v] = c
                if self.graph_coloring_util(m, assignment, index + 1):
                    return True
                assignment[v] = 0
        return False
    
    def graph_coloring(self):
        for m in range(1, len(self.nodes) + 1):
            assignment = {v: 0 for v in self.nodes}
            if self.graph_coloring_util(m, assignment, 0):
                return m, assignment
        return len(self.nodes), {v: i+1 for i, v in enumerate(self.nodes)} 

    # --- Algoritmo do Carteiro Chinês ---
    def grau(self, v):
        return len(self.adj[v])

    def nodes_odds(self):
        return [v for v in self.nodes if self.grau(v) % 2 == 1]

    def dijkstra(self, start):
        dist = {v: float("inf") for v in self.nodes}
        dist[start] = 0
        pq = [(0, start)]
        while pq:
            d, u = heapq.heappop(pq)
            if d > dist[u]:
                continue
            for (v, w) in self.adj[u]:
                if dist[v] > dist[u] + w:
                    dist[v] = dist[u] + w
                    heapq.heappush(pq, (dist[v], v))
        return dist

    def chinese_postman(self, start):
        total = sum(w for _, _, w in self.get_arestas())
        odds = self.nodes_odds()

        if not odds:  # já é euleriano
            return total * 2, "Já existe um circuito euleriano"

        # calcular distâncias mínimas entre ímpares
        dist = {u: self.dijkstra(u) for u in self.nodes}

        melhor = float("inf")
        for emp in itertools.permutations(odds):
            if len(emp) % 2 != 0: 
                continue
            usado = set()
            custo = 0
            for i in range(0, len(emp), 2):
                if emp[i] not in usado and emp[i+1] not in usado:
                    custo += dist[emp[i]][emp[i+1]]
                    usado.add(emp[i])
                    usado.add(emp[i+1])
            if len(usado) == len(odds):
                melhor = min(melhor, custo)

        return total*2 + melhor, f"Circuito fechado no ponto {start}"

# -----------------------------
if __name__ == "__main__":
    #aulas = ['M', 'A', 'C', 'F', 'Q', 'P']
    #g = ListGraph(aulas)

    # CONFLITOS
    #g.add_edge('C', 'F')
    #g.add_edge('C', 'A')
    #g.add_edge('M', 'A')
    #g.add_edge('M', 'P')
    #g.add_edge('P', 'A')
    #g.add_edge('Q', 'F')
    #g.add_edge('F', 'A')

    #print("\n--- Grafos de Conflitos ---")
    #g.print()

    #print("\n--- Coloração do Grafo ---")
    #min_colors, assignment = g.graph_coloring()
    #print(f"Número mínimo de horários necessários (χ(G)): {min_colors}")
    #print("Atribuição de horários às aulas:", assignment)

    # -------- ATIVIDADE: LUZ NO CERRADO --------
    print("\n--- Problema do Carteiro Chinês (PCC)---")
    pontos = ['A','B','C','D','E','F']
    cpp = ListGraph(pontos)
    cpp.add_edge('A','B',100)
    cpp.add_edge('A','C',80)
    cpp.add_edge('B','C',120)
    cpp.add_edge('B','D',200)
    cpp.add_edge('C','D',100)
    cpp.add_edge('C','E',150)
    cpp.add_edge('D','F',90)
    cpp.add_edge('E','F',110)

    cpp.print()
    custo, msg = cpp.chinese_postman('A')
    print(f"Distância mínima total a ser percorrida: {custo} metros")
    print(msg)
