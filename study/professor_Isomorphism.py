def is_isomorfo(sefl,grafo):
    if (self.numero_vertices() != grafo.numero_vertices()):
        return False
    
    if (self.numero_arestas() != grafo.numero_arestas()):
        return False
    
    if (self.sequencia_de_grau() != grafo.sequencia_de_grau()):
        return False    
    
    vertices1 = list(self.get_vertices())
    vertices2 = list(grafo.get_vertices())

    for p in itertools.permutations(vertices2):
        mapping = dict(zip(vertices1, p))

        if self._cehga_mapeamento_preserva_adjacencia(self, grafo, mapping):
            return True
    return False
    
def _cehga_mapeamento_preserva_adjacencia(self, grafo1, grafo2, mapping):
    arestas_1 = grafo1.get_arestas()
    arestas_2 = grafo2.get_arestas()

    for aresta in arestas_1:
        u1, v1 = aresta
        u2 = mapping[u1]
        v2 = mapping[v1]

        if ((u2,v2) not in arestas_2) and ((v2,u2) not in arestas_2):
            return False
    return True