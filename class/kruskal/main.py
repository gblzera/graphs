import random

class UnionFind:
    def __init__(self, num_elementos):
        # No começo, cada elemento é seu próprio pai (conjunto de um elemento só)
        self.parent = list(range(num_elementos))
        # O rank ajuda a manter as árvores balanceadas
        self.rank = [0] * num_elementos
    
    def find(self, elemento):
        if self.parent[elemento] != elemento:
            # Aqui acontece a mágica: compressão de caminho recursiva
            self.parent[elemento] = self.find(self.parent[elemento])
        return self.parent[elemento]
    
    def union(self, elem_a, elem_b):
        raiz_a = self.find(elem_a)
        raiz_b = self.find(elem_b)
        
        # Se já estão no mesmo conjunto, não tem o que fazer
        if raiz_a == raiz_b:
            return False
        
        # União por rank: a árvore menor vira filha da maior
        if self.rank[raiz_a] < self.rank[raiz_b]:
            self.parent[raiz_a] = raiz_b
        elif self.rank[raiz_a] > self.rank[raiz_b]:
            self.parent[raiz_b] = raiz_a
        else:
            # Ranks iguais: escolhemos um como pai e incrementamos seu rank
            self.parent[raiz_b] = raiz_a
            self.rank[raiz_a] += 1
        
        return True


def kruskal(num_nodes, edges):
    # Primeiro passo: ordenar as edges pelo peso
    edges.sort(key=lambda edge: edge[2])
    
    # Inicializa a estrutura Union-Find
    uf = UnionFind(num_nodes)
    arvore_minima = []
    
    # Processa cada edge em ordem crescente de peso
    for u, v, peso in edges:
        # Tenta unir os nodes (ajustando índices de 1-based para 0-based)
        if uf.union(u - 1, v - 1):
            # Se conseguiu unir, essa edge faz parte da MST
            arvore_minima.append((u, v, peso))
    
    return arvore_minima


def gerar_grafo_aleatorio(num_nodes, num_edges, peso_maximo=20):
    edges = set()
    
    # Continua gerando edges até atingir a quantidade desejada
    while len(edges) < num_edges:
        u = random.randint(1, num_nodes)
        v = random.randint(1, num_nodes)
        
        # Verifica se a edge é válida (sem loops e sem duplicatas)
        if u != v and (u, v) not in edges and (v, u) not in edges:
            peso = random.randint(1, peso_maximo)
            edges.add((u, v, peso))
    
    return list(edges)


if __name__ == "__main__":
    # Coleta as informações do usuário
    num_nodes = int(input("Digite o número de vértices: "))
    num_edges = int(input("Digite o número de arestas: "))
    
    # Gera o grafo aleatório
    edges = gerar_grafo_aleatorio(num_nodes, num_edges)
    
    # Mostra as edges geradas
    print("\nEdges geradas aleatoriamente (origem - destino | peso):")
    for origem, destino, peso in edges:
        print(f"{origem} - {destino}   (peso: {peso})")
    
    # Executa o algoritmo de Kruskal
    mst = kruskal(num_nodes, edges)
    peso_total = sum(peso for _, _, peso in mst)
    
    # Exibe os resultados
    print("\n" + "=" * 50)
    print("Árvore Geradora Mínima (MST) encontrada:")
    print("=" * 50)
    for origem, destino, peso in mst:
        print(f"{origem} - {destino}   (peso: {peso})")
    
    print(f"\nPeso total da MST: {peso_total}")
    print(f"Número de vértices na MST: {num_nodes}")
    print(f"Número de arestas na MST: {len(mst)}")