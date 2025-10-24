import math

def dijkstra_step_by_step(graph, start_node):
    """
    Implementação didática do Algoritmo de Dijkstra, mostrando cada passo.
    Esta versão NÃO usa fila de prioridade (heapq) para ser mais fácil de seguir.
    """
    
    # Pega todos os nós do grafo
    all_nodes = set(graph.keys())
    
    # 1. Inicialização
    # Dicionário para armazenar as distâncias (estimativas)
    distances = {node: math.inf for node in all_nodes}
    # Dicionário para armazenar os predecessores
    predecessors = {node: None for node in all_nodes}
    
    # A distância do nó inicial para ele mesmo é 0
    distances[start_node] = 0
    
    # Conjunto de nós que ainda não foram visitados (processados)
    unvisited_nodes = set(all_nodes)
    
    step = 1
    
    print("--- Execução Passo a Passo do Dijkstra ---")
    print(f"Estado Inicial (Nó de partida: {start_node}):")
    print(f"  Distâncias: {distances}")
    print(f"  Predecessores: {predecessors}")
    print("-" * 60)

    while unvisited_nodes:
        
        # 2. Encontrar o nó NÃO VISITADO com a menor distância
        current_node = None
        min_distance = math.inf

        for node in unvisited_nodes:
            if distances[node] < min_distance:
                min_distance = distances[node]
                current_node = node
        
        # Se o nó com menor distância for infinito, os nós restantes são inalcançáveis
        if min_distance == math.inf:
            print("Nós restantes inalcançáveis. Encerrando.")
            break
            
        print(f"Passo {step}: Visitando o nó '{current_node}' (Distância: {min_distance})")
        
        # 3. Iterar sobre os vizinhos do nó atual (Relaxamento)
        for neighbor, weight in graph[current_node].items():
            
            # Só atualiza se o vizinho AINDA NÃO FOI VISITADO
            if neighbor in unvisited_nodes:
                new_distance = distances[current_node] + weight
                
                # 4. Se encontramos um caminho mais curto...
                if new_distance < distances[neighbor]:
                    old_dist = distances[neighbor]
                    # ...atualizamos a distância e o predecessor
                    distances[neighbor] = new_distance
                    predecessors[neighbor] = current_node
                    print(f"  -> Atualizando '{neighbor}': Dist. de {old_dist} para {new_distance} (via '{current_node}')")
        
        # 5. Marcar o nó atual como visitado
        unvisited_nodes.remove(current_node)
        
        print(f"\n  Estado após o Passo {step}:")
        print(f"    Distâncias: {distances}")
        print(f"    Predecessores: {predecessors}")
        print(f"    Nós não visitados: {unvisited_nodes if unvisited_nodes else '{}'}")
        print("-" * 60)
        step += 1

    print("--- Fim do Algoritmo ---")
    return distances, predecessors

# --- Execução ---

# 1. Definir o grafo da imagem
graph = {
    'S': {'A': 6, 'B': 7},
    'A': {'C': 5, 'D': 4},
    'B': {'A': 2, 'C': 8, 'D': 9},
    'C': {'D': 3},
    'D': {}
}

# 2. Definir o nó inicial
start_node = 'S'

# 3. Rodar o algoritmo
distances, predecessors = dijkstra_step_by_step(graph, start_node)

# 4. Exibir os resultados de forma formatada (igual ao anterior)
print("\n--- Tabela Final Resumida ---")
print(f"{'Vértice':<12} | {'Estimativa':<10} | {'Precedente':<10}")
print("-" * 40)

all_nodes_sorted = sorted(graph.keys())
for node in all_nodes_sorted:
    pred = predecessors[node] if predecessors[node] is not None else '-'
    print(f"{node:<12} | {distances[node]:<10} | {pred:<10}")