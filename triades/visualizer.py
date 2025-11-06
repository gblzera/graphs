# --- Parceiro de Programação: Visualizando Conceitos de Tríades ---

import networkx as nx
import matplotlib.pyplot as plt

# --- 1. Criar Tríade FECHADA ---
# Um grafo simples de 3 nós (A, B, C)
G_fechada = nx.Graph()
# A está ligado a B, B a C, e C a A. Forma um triângulo.
G_fechada.add_edges_from([('A', 'B'), ('B', 'C'), ('C', 'A')])

# Definimos as posições (para ficar um triângulo bonito)
pos_fechada = {'A': [0, 1], 'B': [1, 0], 'C': [-1, 0]}

# --- 2. Criar Tríade ABERTA ---
# 3 nós: Maria, João, Ana
G_aberta = nx.Graph()
# Maria está ligada a João, e João a Ana.
# A ligação ('Maria', 'Ana') está EM FALTA.
G_aberta.add_edges_from([('Maria', 'João'), ('João', 'Ana')])

# Posições
pos_aberta = {'Maria': [0, 1], 'João': [0, 0], 'Ana': [1, 1]}

# --- 3. Desenhar os Grafos ---
print("A gerar visualização... Verifique a nova janela que vai abrir.")

# Criamos uma figura que terá 2 gráficos (1 linha, 2 colunas)
plt.figure(figsize=(10, 5))

# --- Gráfico 1: A Tríade Fechada ---
plt.subplot(1, 2, 1) # (linhas, colunas, índice)
plt.title("Exemplo: Tríade FECHADA (Triângulo)", fontsize=14)
nx.draw(G_fechada, 
        pos=pos_fechada, 
        with_labels=True, 
        node_size=2500, 
        node_color='#a0cbe2', # Azul claro
        font_size=16,
        font_weight='bold')

# --- Gráfico 2: A Tríade Aberta ---
plt.subplot(1, 2, 2)
plt.title("Exemplo: Tríade ABERTA ('João' é a ponte)", fontsize=14)
nx.draw(G_aberta, 
        pos=pos_aberta, 
        with_labels=True, 
        node_size=2500, 
        node_color='#a0e2a0', # Verde claro
        font_size=16,
        font_weight='bold')

# Mostrar a janela com os gráficos
plt.tight_layout() # Ajusta para não sobrepor
plt.show()

print("Visualização gerada.")