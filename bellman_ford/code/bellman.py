# --- Importação das bibliotecas ---
import networkx as nx
import matplotlib.pyplot as plt
import time

# ------------------------------------------------------------
# Função principal: Bellman-Ford com visualização
# ------------------------------------------------------------
def bellman_ford_visualizer(G, start, pos, title_suffix=""):
    # Inicialização
    dist = {node: float("inf") for node in G.nodes()}
    dist[start] = 0
    predecessor = {node: None for node in G.nodes()}

    plt.style.use("dark_background")
    plt.ion()  # modo interativo

    # Função auxiliar para desenhar o grafo
    def desenhar_grafo(highlight_edges=None, highlight_nodes=None, step_title=""):
        plt.clf()
        node_colors = []
        for n in G.nodes():
            if highlight_nodes and n in highlight_nodes:
                node_colors.append("#FFD700")  # nó destacado
            elif dist[n] < float("inf"):
                node_colors.append("#90EE90")  # nó já alcançado
            else:
                node_colors.append("#87CEEB")  # nó ainda infinito

        edge_colors = []
        for (u, v) in G.edges():
            if highlight_edges and (u, v) in highlight_edges:
                edge_colors.append("lime")  # caminho destacado
            else:
                # <-- MUDANÇA 1: Corrigindo as arestas invisíveis
                edge_colors.append("gray")  # MUDADO DE "white" PARA "gray"

        nx.draw(
            G, pos,
            with_labels=True,
            node_color=node_colors,
            node_size=1500,
            font_size=14,
            font_weight="bold",
            edgecolors="black",
            edge_color=edge_colors,
            arrowsize=20,
            width=2
        )

        # pesos das arestas
        edge_labels = nx.get_edge_attributes(G, "weight")
        nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_color="yellow", font_size=12)

        # distâncias nos nós
        label_dist = {n: f"{n}\n({dist[n] if dist[n]!=float('inf') else '∞'})" for n in G.nodes()}
        nx.draw_networkx_labels(G, pos, labels=label_dist, font_size=13, font_color="black")

        plt.title(step_title, fontsize=15, color="white", pad=20)
        plt.pause(1)

    # ------------------------------------------------------------
    # Relaxamento das arestas |V|-1 vezes
    # ------------------------------------------------------------
    for i in range(len(G.nodes()) - 1):
        alterado = False
        for (u, v, dados) in G.edges(data=True):
            peso = dados["weight"]
            if dist[u] != float("inf") and dist[u] + peso < dist[v]:
                dist[v] = dist[u] + peso
                predecessor[v] = u
                alterado = True
                desenhar_grafo(highlight_edges=[(u,v)], highlight_nodes=[u,v],
                               step_title=f"{title_suffix} Iteração {i+1} - Relaxando {u}→{v}")
        if not alterado:
            break

    # ------------------------------------------------------------
    # Verificação de ciclos negativos
    # ------------------------------------------------------------
    for (u, v, dados) in G.edges(data=True):
        peso = dados["weight"]
        if dist[u] != float("inf") and dist[u] + peso < dist[v]:
            desenhar_grafo(step_title=f"{title_suffix} Ciclo de peso negativo detectado!")
            print("⚠️ Ciclo de peso negativo detectado!")
            plt.show()
            return

    # ------------------------------------------------------------
    # <-- MUDANÇA 2: Mostrar a ÁRVORE de caminhos mínimos completa
    # ------------------------------------------------------------

    # Reconstruir TODAS as arestas da árvore de caminhos mínimos
    caminho_edges = []
    for node, pred in predecessor.items():
        if pred is not None:
            caminho_edges.append((pred, node))

    # ------------------------------------------------------------
    # Visualização final
    # ------------------------------------------------------------
    desenhar_grafo(
        highlight_edges=caminho_edges, 
        step_title=f"{title_suffix} Resultado Final - Árvore de Caminhos Mínimos"
    )
    plt.ioff()
    plt.show()

    print("\n🟢 Distâncias finais a partir do nó de origem:")
    for n in G.nodes():
        print(f"{start} → {n} = {dist[n]}")
    
    # Imprimir a árvore de predecessores
    print("\n🟢 Árvore de caminhos mínimos (Predecessores):")
    for node, pred in predecessor.items():
        if pred is not None:
            print(f"{pred} → {node}")

# ------------------------------------------------------------
# Construção do grafo de exemplo
# ------------------------------------------------------------
G = nx.DiGraph()
edges = [
    ("A", "B", -1),
    ("A", "C", 4),
    ("B", "C", 3),
    ("B", "D", 2),
    ("B", "E", 2),
    ("D", "C", 5),
    ("D", "B", 1),
    ("E", "D", -3)
]
for u, v, w in edges:
    G.add_edge(u, v, weight=w)

pos = {
    "A": (0, 1.5),
    "B": (-1, 0.5),
    "C": (1, 0.5),
    "D": (-1.2, -0.8),
    "E": (0.2, -0.8)
}

# ------------------------------------------------------------
# Execução
# ------------------------------------------------------------
print("🔹 Executando Bellman-Ford a partir de A:")
bellman_ford_visualizer(G, "A", pos, title_suffix="Bellman-Ford -")