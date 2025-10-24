# --- Importação das bibliotecas necessárias ---
import networkx as nx                # Criação e manipulação de grafos
import matplotlib.pyplot as plt      # Plotagem e visualização
from collections import deque        # Estrutura de fila eficiente (usada no BFS)

# ------------------------------------------------------------
# Função principal: bfs_visualizer
# ------------------------------------------------------------
def bfs_visualizer(G, start, title_suffix=""):
    """
    Executa e visualiza o algoritmo de busca em largura (BFS) passo a passo.

    Parâmetros:
        G (nx.Graph): grafo a ser percorrido
        start (str): nó inicial da busca
        title_suffix (str): texto adicional exibido no título da animação
    """

    # --- Posições fixas para os nós (mantém layout constante durante a animação) ---
    pos = {
        "A": (0, 1.5), #v1
        "B": (-1, 0.5),
        "C": (1, 0.5),
        "D": (-1.2, -0.8),
        "E": (0, -0.8),
        "F": (1.2, -0.8) #v6
    }

    # --- Estruturas principais do BFS ---
    visited = set()           # Conjunto de nós já visitados
    queue = deque([start])    # Fila (FIFO) contendo o nó inicial
    step = 0                  # Contador de etapas da animação

    # --- Ativa o modo interativo do matplotlib ---
    plt.ion()

    # --- Loop principal do BFS ---
    while queue:
        u = queue.popleft()

        if u not in visited:
            visited.add(u)
            step += 1

            plt.clf()

            node_colors = [
                "lightgreen" if n in visited else "lightblue"
                for n in G.nodes()
            ]

            nx.draw(
                G, pos,
                with_labels=True,
                node_color=node_colors,
                node_size=1200,
                font_size=14,
                font_weight="bold",
                edgecolors="black"
            )

            # Não mostra pesos, pois o grafo não tem
            edge_labels = nx.get_edge_attributes(G, "weight")
            if edge_labels:
                nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_color="yellow")

            plt.title(
                f"{title_suffix} Etapa {step}: visitando {u}",
                fontsize=16, color="white", pad=20
            )

            plt.pause(3)

            for neighbor in G[u]:
                if neighbor not in visited and neighbor not in queue:
                    queue.append(neighbor)

    plt.ioff()
    plt.show()

# ------------------------------------------------------------
# Construção do grafo
# ------------------------------------------------------------

# Cria um grafo não-direcionado
G = nx.Graph()

# Lista de arestas sem pesos
edges = [
    ("A", "B"),
    ("A", "C"),
    ("B", "D"),
    ("B", "E"),
    ("C", "F"),
    ("D", "E")
]

# Adiciona as arestas ao grafo
G.add_edges_from(edges)

# ------------------------------------------------------------
# Execução 1: BFS no grafo completo
# ------------------------------------------------------------
print("🔹 BFS completo com todas as arestas:")
bfs_visualizer(G, "A", title_suffix="Grafo original -")

# ------------------------------------------------------------
# Execução 2: Removendo uma aresta e executando novamente
# ------------------------------------------------------------
print("\n🔸 Removendo aresta (B, E) e executando BFS novamente:")

if G.has_edge("B", "E"):
    G.remove_edge("B", "E")
else:
    print("Aresta (B, E) não existe, continuando com a simulação sem ela.")

bfs_visualizer(G, "A", title_suffix="Após remover (B,E) -")
