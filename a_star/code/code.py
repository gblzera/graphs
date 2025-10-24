# --- Importação das bibliotecas necessárias ---
import networkx as nx
import math
import time

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
# Função principal: a_star_terminal
# ------------------------------------------------------------
def a_star_terminal(G, start, goal, pos):
    """
    Executa o algoritmo A* e exibe o progresso passo a passo no terminal.
    """
    open_set = {start}
    came_from = {}
    g_score = {node: float("inf") for node in G.nodes()}
    g_score[start] = 0
    f_score = {node: float("inf") for node in G.nodes()}
    f_score[start] = heuristic(pos, start, goal)

    step = 0

    print(f"\n🔹 Iniciando A* de {start} até {goal}\n")

    while open_set:
        current = min(open_set, key=lambda n: f_score[n])
        step += 1
        print(f"📍 Etapa {step}: analisando nó {current}")
        print(f"   -> g_score[{current}] = {g_score[current]:.2f}")
        print(f"   -> f_score[{current}] = {f_score[current]:.2f}")

        # --- Verifica se chegou ao objetivo ---
        if current == goal:
            print(f"\n✅ Caminho encontrado até {goal}!\n")
            break

        open_set.remove(current)

        # --- Explora vizinhos ---
        for neighbor in G[current]:
            tentative_g = g_score[current] + G[current][neighbor]["weight"]

            print(f"   → Vizinho {neighbor}: custo atual {g_score[neighbor]:.2f}, "
                  f"tentativa {tentative_g:.2f}")

            if tentative_g < g_score[neighbor]:
                came_from[neighbor] = current
                g_score[neighbor] = tentative_g
                f_score[neighbor] = tentative_g + heuristic(pos, neighbor, goal)
                open_set.add(neighbor)
                print(f"     ✅ Atualizado! Novo melhor caminho para {neighbor}")
        print(f"   Conjunto aberto: {list(open_set)}\n")
        time.sleep(1)  # pausa para acompanhar passo a passo

    # --- Reconstrução do caminho ---
    path = []
    node = goal
    while node in came_from:
        path.append(node)
        node = came_from[node]
    path.append(start)
    path = path[::-1]

    # --- Resultado final ---
    print("🟢 Caminho final encontrado:", " → ".join(path))
    total_cost = sum(G[path[i]][path[i+1]]["weight"] for i in range(len(path)-1))
    print(f"💰 Custo total do caminho: {total_cost:.2f}\n")

    print("Detalhes dos custos finais:")
    for n in G.nodes():
        g = g_score[n]
        f = f_score[n]
        print(f" - {n}: g = {g if g < float('inf') else '∞'}, f = {f if f < float('inf') else '∞'}")

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

# --- Posições fixas dos nós (usadas apenas para heurística) ---
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
if __name__ == "__main__":
    a_star_terminal(G, "A", "F", pos)
