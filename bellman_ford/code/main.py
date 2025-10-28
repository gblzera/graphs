# -----------------------------------------------
# Algoritmo de Bellman-Ford (versão terminal)
# -----------------------------------------------

class Grafo:
    def __init__(self, vertices):
        self.V = vertices
        self.arestas = []  # Lista de arestas (u, v, peso)

    def adicionar_aresta(self, u, v, peso):
        self.arestas.append((u, v, peso))

    def bellman_ford(self, origem):
        # Passo 1: Inicializar as distâncias
        dist = {v: float('inf') for v in range(self.V)}
        dist[origem] = 0

        print(f"Distâncias iniciais: {dist}")

        # Passo 2: Relaxar todas as arestas |V| - 1 vezes
        for i in range(self.V - 1):
            print(f"\nIteração {i + 1}:")
            alterado = False
            for u, v, peso in self.arestas:
                if dist[u] != float('inf') and dist[u] + peso < dist[v]:
                    dist[v] = dist[u] + peso
                    alterado = True
                    print(f"Atualizado: dist[{v}] = {dist[v]} (via {u})")
            if not alterado:
                print("Nenhuma atualização nesta iteração, encerrando cedo.")
                break

        # Passo 3: Verificar ciclos negativos
        for u, v, peso in self.arestas:
            if dist[u] != float('inf') and dist[u] + peso < dist[v]:
                print("\n⚠️ Ciclo de peso negativo detectado!")
                return None

        print("\nDistâncias finais mínimas a partir do vértice de origem:")
        for v in dist:
            print(f"{origem} → {v} = {dist[v]}")
        return dist


# ----------------------------
# Exemplo de uso
# ----------------------------
if __name__ == "__main__":
    g = Grafo(5)
    g.adicionar_aresta(0, 1, -1)
    g.adicionar_aresta(0, 2, 4)
    g.adicionar_aresta(1, 2, 3)
    g.adicionar_aresta(1, 3, 2)
    g.adicionar_aresta(1, 4, 2)
    g.adicionar_aresta(3, 2, 5)
    g.adicionar_aresta(3, 1, 1)
    g.adicionar_aresta(4, 3, -3)

    g.bellman_ford(0)
