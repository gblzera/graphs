## 📋 Descrição

Este projeto implementa uma estrutura de dados de grafo não-direcionado utilizando lista de adjacência. A implementação inclui operações básicas como adição e remoção de arestas, além do algoritmo de busca em profundidade (DFS).

## 🚀 Funcionalidades

- **Criação de grafo**: Inicialização com lista de nós
- **Adição de arestas**: Conecta dois nós no grafo
- **Remoção de arestas**: Remove conexão entre dois nós
- **Visualização**: Exibe a lista de adjacência
- **DFS (Depth-First Search)**: Busca em profundidade a partir de um nó inicial

## 🔧 Como Usar

### JavaScript (Node.js)

```bash
# Execute o arquivo JavaScript
node main.js
```

### Python

```bash
# Execute o arquivo Python
python main.py
```

## 📝 Exemplo de Uso

### Criando um Grafo

**JavaScript:**
```javascript
let vertices = ["A", "B", "C", "D", "E"];
let arestas = [["A","B"], ["A","C"], ["C","D"], ["C","E"], ["B","D"]];

let grafo = new ListGraph(vertices);
arestas.forEach(([u,v]) => grafo.add_edge(u, v));
```

**Python:**
```python
vertices = ["A", "B", "C", "D", "E"]
arestas = [("A","B"), ("A","C"), ("C","D"), ("C","E"), ("B","D")]

grafo = ListGraph(vertices)
for (u,v) in arestas:
    grafo.add_edge(u,v)
```

### Operações Disponíveis

#### Adicionar Aresta
```javascript
// JavaScript
grafo.add_edge("A", "B");
```
```python
# Python
grafo.add_edge("A", "B")
```

#### Remover Aresta
```javascript
// JavaScript
grafo.remove_edge("A", "C");
```
```python
# Python
grafo.remove_edge("A", "C")
```

#### Visualizar Lista de Adjacência
```javascript
// JavaScript
grafo.print();
```
```python
# Python
grafo.print()
```

#### Executar DFS
```javascript
// JavaScript
grafo.dfs("A");
```
```python
# Python
grafo.dfs("A")
```

## 📊 Exemplo de Saída

```
Adjacency List:
A -> [ 'B', 'C' ]
B -> [ 'A', 'D' ]
C -> [ 'A', 'D', 'E' ]
D -> [ 'C', 'B' ]
E -> [ 'C' ]

DFS starting from A:
A B D C E 

Removing edge (A,C)...
Adjacency List:
A -> [ 'B' ]
B -> [ 'A', 'D' ]
C -> [ 'D', 'E' ]
D -> [ 'C', 'B' ]
E -> [ 'C' ]

DFS starting from A after removing edge (A,C):
A B D C E 
```

## 🏗️ Estrutura da Classe

### Construtor
- **Parâmetros**: `nodes` - lista de nós do grafo
- **Inicializa**: Lista de adjacência vazia para cada nó

### Métodos

| Método | Descrição | Complexidade |
|--------|-----------|-------------|
| `add_edge(u, v)` | Adiciona aresta entre nós u e v | O(1) |
| `remove_edge(u, v)` | Remove aresta entre nós u e v | O(k) onde k é o grau do nó |
| `print()` | Exibe a lista de adjacência | O(V + E) |
| `dfs(start)` | Busca em profundidade | O(V + E) |

## 🔍 Correções Aplicadas

O código Python original continha um pequeno erro na função `remove_edge`:
```python
# Erro original:
if v in self.adj[v]:    # estava usando 'v' em vez de 'u'
    self.adj[v].remove(u)

# Correção:
if u in self.adj[v]:
    self.adj[v].remove(u)
```

## 💡 Características do Grafo

- **Tipo**: Não-direcionado
- **Representação**: Lista de adjacência
- **Arestas múltiplas**: Não permitidas (verificação de duplicatas)
- **Laços**: Não implementados (assumindo grafos simples)

## 🎯 Casos de Uso

- Redes sociais (conexões entre pessoas)
- Mapas rodoviários (cidades conectadas por estradas)
- Circuitos elétricos
- Estruturas moleculares
- Algoritmos de pathfinding

## 🚦 Pré-requisitos

- **JavaScript**: Node.js (versão 12+)
- **Python**: Python 3.6+

## 📄 Licença

Este projeto é de domínio público e pode ser usado livremente para fins educacionais e comerciais.