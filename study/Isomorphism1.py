from itertools import permutations

def_isomorfo(g1,g2):

    if len(g1) != len(g2): #verificar se os grafos tem o mesmo numero de vertices
        return False

    nodes1 = list(g1,keys()) #listar todos os vertices de g1
    nodes2 = list(g2.keys()) #listar todos os vertices de g2

    for perm in permutations(nodes2): #gerar todas as permutacoes possiveis dos vertices de g2
        mapping = dist(zip(nodes1, perm)) #cria um dicionario que mapeia os vertices de g1 para os de g2

        isomorphic = True #assume que os grafos sao isomorfos ate provar o contrario
        for v1 in nodes1: #verifica se os vizinhos de cada vertice em g1 correspondem aos vizinhos mapeados em g2
            neighbors1 = set(g1[v1]) #obtem os vizinhos do vertice v1 em g1
            mapped_neighbors = {mapping[n] for n in neighbors1} #mapeia os vizinhos de v1 para os vertices correspondentes em g2

            v2 = mapping[v1] #obtem o vertice correspondente em g2
            neighbors2 = set(g2[v2]) #obtem os vizinhos do vertice v2 em g2
            if mapped_neighbors != neighbors2: #compara os conjuntos de vizinhos
                isomorphic = False 
                break
        if isomorphic:
            return True
    return False