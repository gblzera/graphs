# --- Importação das bibliotecas necessárias ---
import networkx as nx                # Criação e manipulação de grafos
import matplotlib.pyplot as plt      # Plotagem e visualização
import math                          # Cálculos matemáticos (para heurística)

# ------------------------------------------------------------
# Função heurística (distância euclidiana)
# ------------------------------------------------------------
def heuristic(pos, node1, node2):
    """
    Calcula a distância euclidiana entre dois nós (heurística).
    """
    x1, y1 = pos[node1]
    x2, y2 = pos[node2]
    return math.sqrt((x1 - x2)**2 + (y1 - y2)**2)

# ------------------------------------------------------------
# Função principal: a_star_visualizer
# ------------------------------------------------------------
def a_star_visualizer(G, start, goal, pos, title_suffix=""):
    """
    Executa e visualiza o algoritmo A* passo a passo.

    Parâmetros:
        G (nx.Graph): grafo ponderado
        start (str): nó inicial
        goal (str): nó objetivo
        pos (dict): posições fixas dos nós
        title_suffix (str): texto adicional no título da animação
    """

    # --- Inicialização ---
    open_set = {start}
    came_from = {}
    g_score = {node: float("inf") for node in G.nodes()}
    g_score[start] = 0
    f_score = {node: float("inf") for node in G.nodes()}
    f_score[start] = heuristic(pos, start, goal)

    step = 0
    plt.ion()  # modo interativo

    # --- Loop principal do A* ---
    while open_set:
        # Seleciona o nó com menor f_score
        current = min(open_set, key=lambda n: f_score[n])

        # --- Visualização ---
        plt.clf()
        node_colors = []
        for n in G.nodes():
            if n == current:
                node_colors.append("gold")        # nó atual
            elif n in open_set:
                node_colors.append("orange")      # nós a serem explorados
            elif g_score[n] < float("inf"):
                node_colors.append("lightgreen")  # já visitados
            else:
                node_colors.append("lightblue")   # não visitados

        nx.draw(
            G, pos,
            with_labels=True,
            node_color=node_colors,
            node_size=1200,
            font_size=14,
            font_weight="bold",
            edgecolors="black"
        )

        edge_labels = nx.get_edge_attributes(G, "weight")
        nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_color="yellow")

        plt.title(
            f"{title_suffix} Etapa {step}: analisando {current}",
            fontsize=16, color="white", pad=20
        )
        plt.pause(2)
        step += 1

        # --- Verifica se chegou ao objetivo ---
        if current == goal:
            print(f"✅ Caminho encontrado até {goal}!")
            break

        open_set.remove(current)

        # --- Explora vizinhos ---
        for neighbor in G[current]:
            tentative_g = g_score[current] + G[current][neighbor]["weight"]
            if tentative_g < g_score[neighbor]:
                came_from[neighbor] = current
                g_score[neighbor] = tentative_g
                f_score[neighbor] = tentative_g + heuristic(pos, neighbor, goal)
                open_set.add(neighbor)

    # --- Reconstrução do caminho ---
    path = []
    node = goal
    while node in came_from:
        path.append(node)
        node = came_from[node]
    path.append(start)
    path = path[::-1]

    # --- Exibe caminho final ---
    plt.clf()
    node_colors = ["lightgreen" if n in path else "lightblue" for n in G.nodes()]
    nx.draw(
        G, pos,
        with_labels=True,
        node_color=node_colors,
        node_size=1200,
        font_size=14,
        font_weight="bold",
        edgecolors="black"
    )
    nx.draw_networkx_edges(G, pos, edgelist=list(zip(path[:-1], path[1:])), width=4, edge_color="green")

    edge_labels = nx.get_edge_attributes(G, "weight")
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_color="yellow")

    plt.title(f"{title_suffix} Caminho final: {' → '.join(path)}", fontsize=16, color="white", pad=20)
    plt.pause(3)
    plt.ioff()
    plt.show()

    print("🟢 Caminho final encontrado:", " → ".join(path))


# ------------------------------------------------------------
# Construção do grafo
# ------------------------------------------------------------
G = nx.Graph()

edges = [
    ("A", "B", 4),
    ("A", "C", 2),
    ("B", "C", 1),
    ("B", "D", 5),
    ("C", "D", 8),
    ("C", "E", 10),
    ("D", "E", 2),
    ("D", "F", 6),
    ("E", "F", 3)
]

# Adiciona as arestas com pesos
for u, v, w in edges:
    G.add_edge(u, v, weight=w)

# --- Posições fixas dos nós ---
pos = {
    "A": (0, 1.5),
    "B": (-1, 0.5),
    "C": (1, 0.5),
    "D": (-1.2, -0.8),
    "E": (0, -0.8),
    "F": (1.2, -0.8)
}

# ------------------------------------------------------------
# Execução: A* de A até F
# ------------------------------------------------------------
print("🔹 Executando A* de A até F:")
a_star_visualizer(G, "A", "F", pos, title_suffix="Algoritmo A* -")
