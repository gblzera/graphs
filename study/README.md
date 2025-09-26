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



# Explicações do Chat-GEPETO:

# 📘 Guia Rápido de Grafos – Propriedades Essenciais

Este documento resume conceitos fundamentais de **teoria dos grafos**, com foco em propriedades estruturais e fórmulas úteis para estudo e consulta.

---

## 🔹 1. Ciclos Hamiltonianos e Problemas NP-Completos

- **NP-completo**: Classe de problemas para os quais:
  - Não se conhece algoritmo eficiente (tempo polinomial) para resolver.
  - Mas é **fácil verificar** se uma solução proposta está correta.

- **Exemplo clássico**: **Problema do Ciclo Hamiltoniano**
  - "Existe um ciclo que passa por **todos os vértices exatamente uma vez**?"
  - Aplicações: logística, roteamento, bioinformática, caixeiro-viajante.

- **Teorema de Dirac**:  
  Se um grafo tem `n ≥ 3` vértices e todo vértice possui **grau ≥ n/2**, então o grafo é Hamiltoniano.

---

## 🔹 2. Grafo de Ciclo (`Cₙ`)

- Definição: grafo com `n` vértices conectados em forma de anel.
- Propriedades:
  - Vértices: `n`
  - Arestas: `n`
  - Cada vértice tem **grau 2** → `Cₙ` é **2-regular**.
  - É **bipartido se e somente se `n` for par**.
  - Planar para qualquer `n`.

---

## 🔹 3. Handshaking Lemma (Lema do Aperto de Mão)

- **Enunciado**:  
  A soma dos graus de todos os vértices = `2 × número de arestas`.

  \[
  \sum_{v \in V} grau(v) = 2m
  \]

- **Consequência**:  
  O número de vértices de **grau ímpar é sempre par**.

- **Exemplo**:
  - Grafo com graus `[2, 2, 1, 1]` → soma = 6.
  - Número de arestas = 3 → `2·3 = 6`.

---

## 🔹 4. Grafos Regulares (k-Regulares)

- Definição: grafo onde **todo vértice tem grau `k`**.
- Fórmula para número de arestas:

  \[
  m = \frac{n \cdot k}{2}
  \]

- Exemplos:
  - `Cₙ` é **2-regular**.
  - Cubo (`Q₃`) é **3-regular**.
  - `Kₙ` (grafo completo) é **(n-1)-regular**.

---

## 🔹 5. Exemplos Clássicos de Grafos

### 🔸 Grafo Completo (`Kₙ`)
- Cada par de vértices distintos está conectado por uma aresta.
- Propriedades:
  - Vértices: `n`
  - Arestas: `n(n-1)/2`
  - Grau de cada vértice: `n-1` → **(n-1)-regular**
  - Bipartido? ❌ (exceto `K₂`)
  - Planar? Somente para `n ≤ 4`.

---

### 🔸 Grafo Bipartido Completo (`K_{m,n}`)
- Vértices divididos em dois conjuntos disjuntos `U` e `V`.
- Cada vértice em `U` conecta com todos os vértices em `V`.
- Propriedades:
  - Vértices: `m + n`
  - Arestas: `m · n`
  - Graus:
    - Vértices em `U`: grau `n`
    - Vértices em `V`: grau `m`
  - Bipartido? ✅ Sempre
  - Planar? Somente se `m ≤ 2` ou `n ≤ 2` (senão, contém `K_{3,3}` como subgrafo).

---

## 🔹 6. Tabela Comparativa

| Grafo         | Vértices | Arestas           | Regularidade       | Bipartido?         | Planar?         |
|---------------|----------|-------------------|--------------------|--------------------|-----------------|
| `Cₙ`          | `n`      | `n`               | 2-regular          | ✅ se `n` par      | ✅ sempre        |
| `Kₙ`          | `n`      | `n(n-1)/2`        | (n-1)-regular      | ❌ (exceto `K₂`)   | ✅ se `n ≤ 4`   |
| `K_{m,n}`     | `m+n`    | `m·n`             | regular se `m=n`   | ✅ sempre          | ✅ se `m≤2` ou `n≤2` |

---

## 🔹 7. Fórmulas Importantes

- **Handshaking Lemma**:  
  \[
  \sum grau(v) = 2m
  \]

- **k-regular**:  
  \[
  m = \frac{n \cdot k}{2}
  \]

- **Máximo de arestas**:
  - Grafo simples não direcionado:  
    \[
    \frac{n(n-1)}{2}
    \]
  - Grafo direcionado:  
    \[
    n(n-1)
    \]

---