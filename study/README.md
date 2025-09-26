## 1. Matriz de Adjacência x Lista 

### matrix -> representação n * n (onde n é o numero de vertices) || cada posicao (i, j) indica se existe aresta entre i e j 
### lista -> representa cada vertice, onde tem uma lista com seus vizinhos 

### complexidade matrix:
    Matrix -> O(n^2) -> ideal para grafos densos, ruim para esparsos
    verifica se existe aresta: O(1) acessa direto na matrix
    percorrer vizinhos: O(n) precisa olhar a lista toda

### complexidade lista:
    Lista -> (n + m)m onde m = numero de arestas || ideal para grafos esparsos
    verifica vizinhos: O(grau de vertices)
    verifica se existe aresta especifica (i,j): O(grau(i))

## 2. Ciclos Hamiltonianos

### Um ciclo que passa por todos os vertices exatamente uma vez e volta ao inicio
### probelma de decisão: "Existe ciclo hamiltoniando?" -> NP-completo.
### aplicacoes: logistica, PCC, bioinformatica

## 3. Custo para acesso

### Matrix: acesso a qualquer (i,j) é O(1)
### Lista: acesso a vizinhos é O(grau(v)), verificar se uma aresta existe é mais caro que na matrix

## 4. Cálculo para quantidade de arestas

### Grafo simples não direcionado: maximo n(n-1)/2
### grafo direcionado: maximo n(n-1)
### com laços permitidos: soma-se n

## 5. Grafo C (ciclo)

### C(n): grafo em forma de anel com n vertices

## 6. Grafo bipartido

### verices divididos em dois conjuntos U e V, sem arestas dentro do mesmo conjunto
### exemplo: relação aluno-diciplina
### pode ser testados com BFS/DFS e 2-coloração
### Arestas maximas: |U| * |V|

## 7. Handshaking Lemma

### Soma dos graus de todos os verices = 2.m (onde m = numero de arestas)
### CONSEQUENCIA: numero de vertices de grau impar é sempre par

## 8. Grafo k

### Pode significar:
    k-colorível: pode ser colorido com no máx. k cores.

    k-regular: todos os vértices têm grau k.

    k-partido: generalização de bipartido (divisão em k conjuntos). 

## 9. Grafo planar

### pode ser desenhado no plano sem arestas cruzadas
### teorema de euler: para grafos planares conexos, n - m + f = 2 (vertices - arestas + faces)
### aplicação: mapas, circuitos eletricos

## 10. Subgrafo gerador e induzido

### Subgrafo gerador: contem todos os vertices do grafo orifinal, mas so algumas arestas.
    exemplo: arvore geradora minima

### induzido: contem um subconjunto de vertices e todos as arestas entre eles no grafo original