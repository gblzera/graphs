Infinity = float('inf')

def bellman_ford(graph, N, E, start):
    """
    função principal do algoritmo de Bellman-Ford

    argumentos:
    graph(list): a lista de todas as edges. cada edge é uma tupla(u,v,peso)
    N (int): numero total de nodes (vertices)
    E (int): numero total de edges (arestas)
    start (int): o indice do node inicial (no caso do exercicio, 'S' que é 0)
    """

    distance = [Infinity] * N 
    # primeiro ciramos uma lista para armazenar as distancias mais curtas da origem
    # para todos os outros nodes
    # começamos assunmindo que todas as distancias são infinitas

    # porem a distancia da origem (S) é sempre 0, pois a distancia de S para S é 0
    distance[start] = 0

    # passo 2, relaxamento das egdes
    # o algoritimo repete o processo de relaxamento N-1 vezes
    # se temos 5 nodes (N=5), ele repete 4 vezes
    # isso garante que encontramos o caminho mais curto, mesmo com pesos negativos
    for i in range(N - 1):
        for u,v, weight in graph:
            # u é o no de orgime da aresta
            # v é o no de destino da aresta
            # weight é o peso da aresta
            if distance[u] != Infinity and distance[u] + weight < distance[v]:
                # se a ditancia de u n]ao é infinita e se o caminho é menor que a distancia atual 
                distance[v] = distance[u] + weight
                # atualizamos a distancia de v
    
    # passo 3, verificar ciclo negativo
    # apos N-1 interações, fazemos uma passagem adicional por todas as arestas
    for u,v, weight in graph:
        # se, mesmo depois de tudo, ainda conseguimos relaxar uma aresta
        if distance[u] != Infinity and distance[u] + weight < distance[v]:
            # então existe um ciclo negativo
            # EX: um loop A -> B -> A onde o custo total é -1
            # o algoritmo não pode dar uma respota final, pois o caminho fica encurtando sempre
            print("Graph contains negative weight cycle | no solution")
            return None #encerra a função
        
    # se não houver ciclo negativo, retornamos a lista de distancias
    return distance

# configuração do grafo da atividade

N = 5
E = 9

# mapear os nodes para os numeros
# S = 0
# A = 1
# B = 2
# C = 3
# D = 4

# 0 no origem
start = 0 # 'S'

# lista de todas as arestas no formato (origem, destino, peso)
graph = [
    (0, 1, 3),   # S -> A 
    (0, 2, 5),   # S -> B 
    (1, 3, -5),   # A -> C 
    (1, 4, 8),   # A -> D 
    (2, 1, 6),  # B -> A
    (2, 3, 8),  # B -> C
    (2, 4, -9),   # B -> D
    (4, 0, 2),  # D -> S
    (3, 4, -3)    #  C -> D
]

# chamar a funcao
result = bellman_ford(graph, N, E, start)

# se os resultados nao forem nulos (ou seja nao tem ciclo negativo)
if result:
    print("Result of Bellman-Ford Algorithm: (Start: 'S')")
    print("-----------------------------------------------")

    # lista de nomes para facilitar leitura

    nodes_names = ["S", "A", "B", "C", "D"]

    for i in range(N):
        print(f"Shortest distance from 'S' to '{nodes_names[i]}': {result[i]}")