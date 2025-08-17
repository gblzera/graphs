import networkx as nx
import matplotlib.pyplot as plt

# create graph
V = ["A","B","C","D","E"]
E = [("A","B"), ("A","C"), ("C","D"), ("C","E"), ("B","D")]

G = nx.Graph()
G.add_nodes_from(V)
G.add_edges_from(E)

# draw
pos = nx.spring_layout(G) # layout for visualization
nx.draw(G, pos, with_labels=True, node_size=1000, node_color="lightblue", font_size=14, font_weight="bold")
nx.draw_networkx_edge_labels(G, pos)

plt.title("Graph Visualization - NetworkX")
plt.show()

# remove egdes (A,C) and draw again
G.remove_edge("A","C")
plt.figure()
nx.draw(G, pos, with_labels=True, node_size=1000, node_color="lightgreen", font_size=14, font_weight="bold")
plt.title("Graph after removing edge (A,C)")
plt.show()