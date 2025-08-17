# tive que mandar pra IA corrigir que deu erro :(
import networkx as nx
import matplotlib.pyplot as plt

def dfs_visualizer(G, start):
    pos = nx.spring_layout(G, seed=42)  # posições fixas
    visited = set()

    def dfs(u):
        visited.add(u)
        # desenhar estado atual
        plt.clf()
        colors = ["lightblue" if v not in visited else "lightgreen" for v in G.nodes()]
        nx.draw(G, pos, with_labels=True, node_color=colors, node_size=800, font_size=12)
        plt.title(f"Visiting: {u}")
        plt.pause(1)  # pausa para animar

        for neighbor in G[u]:
            if neighbor not in visited:
                dfs(neighbor)

    dfs(start)          # chama o DFS
    plt.show(block=True)  # mostra o gráfico e mantém a janela aberta


# ==== Teste ====
V = ["A","B","C","D","E"]
E = [("A","B"), ("A","C"), ("B","D"), ("C","E"), ("D","E")]

G = nx.Graph()
G.add_nodes_from(V)
G.add_edges_from(E)

print("Original DFS (complete):")
plt.ion()  # ativa modo interativo
dfs_visualizer(G, "A")

# removendo aresta
print("\nRemoving edge (C,E) and testing DFS:")
G.remove_edge("C", "E")
dfs_visualizer(G, "A")
