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
        "A": (0, 1.5), #pos1 v1
        "B": (-1, 0.5), #pos2 v2
        "C": (1, 0.5), #pos3 v3
        "D": (-1.2, -0.8), #pos4 v4 
        "E": (0, -0.8), #pos5 v5 
        "F": (1.2, -0.8) #pos6 v6
    }

    # --- Estruturas principais do BFS ---
    visited = set()           # Conjunto de nós já visitados
    queue = deque([start])    # Fila (FIFO) contendo o nó inicial
    step = 0                  # Contador de etapas da animação

    # --- Ativa o modo interativo do matplotlib (permite atualização em tempo real) ---
    plt.ion()

    # --- Loop principal do BFS ---
    while queue:
        # Remove o primeiro nó da fila
        u = queue.popleft()

        # Se o nó ainda não foi visitado
        if u not in visited:
            visited.add(u)  # Marca o nó como visitado
            step += 1       # Incrementa o contador de etapas

            # --- Visualização do grafo a cada passo ---
            plt.clf()  # Limpa o gráfico anterior para desenhar o novo estado

            # Define a cor dos nós: verde = visitado, azul = não visitado
            node_colors = [
                "lightgreen" if n in visited else "lightblue"
                for n in G.nodes()
            ]

            # Desenha o grafo com rótulos e formatação
            nx.draw(
                G, pos,
                with_labels=True,
                node_color=node_colors,
                node_size=1200,
                font_size=14,
                font_weight="bold",
                edgecolors="black"
            )

            # Mostra os pesos das arestas (se existirem)
            edge_labels = nx.get_edge_attributes(G, "weight")
            nx.draw_networkx_edge_labels(
                G, pos, edge_labels=edge_labels, font_color="yellow"
            )

            # Define o título indicando o passo atual e o nó visitado
            plt.title(
                f"{title_suffix} Etapa {step}: visitando {u}",
                fontsize=16, color="white", pad=20
            )

            # Pausa de 1 segundo entre cada etapa (para visualização gradual)
            plt.pause(3)

            # --- Adiciona à fila os vizinhos ainda não visitados ---
            for neighbor in G[u]:
                if neighbor not in visited and neighbor not in queue:
                    queue.append(neighbor)

    # --- Encerra o modo interativo e mostra o resultado final ---
    plt.ioff()
    plt.show()

# ------------------------------------------------------------
# Construção do grafo
# ------------------------------------------------------------

# Cria um grafo não-direcionado
G = nx.Graph()

# Lista de arestas com pesos: (nó_origem, nó_destino, peso)
edges = [
    ("A", "B", 1),
    ("A", "C", 3),
    ("B", "D", 4),
    ("B", "E", 5),
    ("C", "F", 6),
    ("D", "E", 2)
]

# Adiciona as arestas ao grafo
G.add_weighted_edges_from(edges)

# ------------------------------------------------------------
# Execução 1: BFS no grafo completo
# ------------------------------------------------------------
print("🔹 BFS completo com todas as arestas:")
bfs_visualizer(G, "A", title_suffix="Grafo original -")

# ------------------------------------------------------------
# Execução 2: Removendo uma aresta e executando novamente
# ------------------------------------------------------------
print("\n🔸 Removendo aresta (B, E) e executando BFS novamente:")

# Verifica se a aresta existe antes de remover
if G.has_edge("B", "E"):
    G.remove_edge("B", "E")
else:
    print("Aresta (B, E) não existe, continuando com a simulação sem ela.")

# Executa novamente o BFS após a alteração do grafo
bfs_visualizer(G, "A", title_suffix="Após remover (B,E) -")
