import networkx as nx
import matplotlib.pyplot as plt
from collections import deque

def bfs_visualizer(G, start):
    pos = nx.spring_layout(G, seed=42)
    visited = set()
    queue = deque([start])

    while queue:
        u = queue.popleft()
        if u not in visited:
            visited.add(u)

            # draw the current state
            plt.clf()
            colors = ["lightblue" if v not in visited else "lightgreen" for v in G.nodes()]
            nx.draw(G, pos, with_labels=True, node_color=colors, node_size=800, font_size=16)
            plt.title(f"Visiting Node: {u}")
            plt.pause(1)

            # add neighbors not yet visited
            for neighbor in G[u]:
                if neighbor not in visited and neighbor not in queue:
                    queue.append(neighbor)
    
    plt.show(block=True)

# test
V = ["A","B","C","D","E","F"]
E = [("A","B"), ("A","C"), ("B","D"), ("B","E"), ("D","E"),("C","F")]

G = nx.Graph()
G.add_nodes_from(V)
G.add_edges_from(E)

print("Original BFS (complete):")
plt.ion()  # turn on interactive mode
bfs_visualizer(G, "A")

# removing egdes
print("\nRemoving edge (C,E) and testing BFS:")
G.remove_edge("C", "E")
bfs_visualizer(G, "A")