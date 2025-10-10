
#codigo documentado por IA
#feito por:
# Gabriel Henrique Kuhn Paz - 2212082043
# Davi Serra Bezerra - 2312130031

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
    edges = []
    
    # Primeiro, garante que o grafo seja conexo criando uma árvore geradora
    nodes_disponiveis = list(range(1, num_nodes + 1))
    random.shuffle(nodes_disponiveis)
    
    # Conecta os nodes um por um para formar uma árvore
    for i in range(num_nodes - 1):
        u = nodes_disponiveis[i]
        v = nodes_disponiveis[i + 1]
        peso = random.randint(1, peso_maximo)
        edges.append((u, v, peso))
    
    # Agora adiciona as edges restantes aleatoriamente
    edges_set = {(min(u, v), max(u, v)) for u, v, _ in edges}
    
    while len(edges) < num_edges:
        u = random.randint(1, num_nodes)
        v = random.randint(1, num_nodes)
        edge_normalizada = (min(u, v), max(u, v))
        
        # Verifica se a edge é válida (sem loops e sem duplicatas)
        if u != v and edge_normalizada not in edges_set:
            peso = random.randint(1, peso_maximo)
            edges.append((u, v, peso))
            edges_set.add(edge_normalizada)
    
    return edges


if __name__ == "__main__":
    # Coleta as informações do usuário
    num_nodes = int(input("Digite o número de nodes: "))
    num_edges = int(input("Digite o número de edges: "))
    
    # Valida se há edges suficientes para conectar o grafo
    if num_edges < num_nodes - 1:
        print(f"\n⚠️ AVISO: Com {num_edges} edges não é possível conectar {num_nodes} nodes!")
        print(f"Mínimo necessário: {num_nodes - 1} edges")
        print(f"Ajustando automaticamente para {num_nodes - 1} edges...\n")
        num_edges = num_nodes - 1
    
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
    
    print(f"\n🎯 Peso total da MST: {peso_total}")
    print(f"📊 Número de nodes na MST: {num_nodes}")
    print(f"📊 Número de edges na MST: {len(mst)}")