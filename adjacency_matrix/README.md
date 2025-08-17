## 📋 Descrição

- **Matriz de Adjacência**: Implementação usando programação orientada a objetos com herança
- **Visualização Interativa**: Renderização gráfica usando p5.js e NetworkX

## 🚀 Funcionalidades

### Visualizações
- **p5.js**: Visualização interativa em navegador
- **NetworkX + Matplotlib**: Visualização científica em Python

## 🔧 Como Usar

### Matriz de Adjacência (Programação Orientada a Objetos)

**JavaScript:**
```bash
node main.js  # Segunda versão
```

**Python:**
```bash
python main.py  # Segunda versão
```

### Visualizações

**p5.js (HTML):**
```bash
Abra main.html em um navegador web
```

**NetworkX (Python):**
```bash
pip install networkx matplotlib
python main.py  # Versão de visualização
```

## 📝 Exemplos de Uso

### Matriz de Adjacência com Herança

**JavaScript:**
```javascript
class Graph {
    numNodes() { throw new Error("Not implemented"); }
    addEdge(u, v) { throw new Error("Not implemented"); }
    // ... outros métodos abstratos
}

class DenseGraph extends Graph {
    constructor(nodes) {
        super();
        this.rotules = nodes;
        this.matrix = Array.from({ length: nodes.length }, 
                                () => Array(nodes.length).fill(0));
    }
    
    addEdge(u, v) {
        let i = this.rotules.indexOf(u);
        let j = this.rotules.indexOf(v);
        this.matrix[i][j] = this.matrix[j][i] = 1;
    }
}
```

**Python:**
```python
class Graph:
    def add_edge(self, u, v):
        raise NotImplementedError

class DenseGraph(Graph):
    def __init__(self, nodes):
        self.rotules = nodes
        self.matrix = [[0] * len(nodes) for _ in range(len(nodes))]
    
    def add_edge(self, u, v):
        i, j = self.rotules.index(u), self.rotules.index(v)
        self.matrix[i][j] = self.matrix[j][i] = 1
```

### Visualização com p5.js

```javascript
let vertices = ["A","B","C","D","E"];
let edges = [["A","B"], ["C","D"], ["C","E"], ["B","D"]];

function setup() {
    createCanvas(500, 500);
    // Posicionar vértices em círculo
    let angleStep = TWO_PI / vertices.length;
    for (let i = 0; i < vertices.length; i++) {
        positions[vertices[i]] = createVector(
            width/2 + 150 * cos(i * angleStep),
            height/2 + 150 * sin(i * angleStep)
        );
    }
}
```

### Visualização com NetworkX

```python
import networkx as nx
import matplotlib.pyplot as plt

G = nx.Graph()
G.add_nodes_from(["A","B","C","D","E"])
G.add_edges_from([("A","B"), ("C","D"), ("C","E"), ("B","D")])

pos = nx.spring_layout(G)
nx.draw(G, pos, with_labels=True, node_size=1000, 
        node_color="lightblue", font_size=14)
plt.show()
```

## 📊 Exemplo de Saída

### Lista de Adjacência
```
Adjacency List:
A -> [ 'B', 'C' ]
B -> [ 'A', 'D' ]
C -> [ 'A', 'D', 'E' ]
D -> [ 'C', 'B' ]
E -> [ 'C' ]

DFS starting from A: A B D C E
```

### Matriz de Adjacência
```
Adjacency Matrix:
  A B C D E
A 0 1 1 0 0
B 1 0 0 1 0
C 1 0 0 1 1
D 0 1 1 0 0
E 0 0 1 0 0

Number of nodes: 5
Number of edges: 5
Degree sequence: [2, 2, 3, 2, 1]
```

## 🏗️ Arquitetura do Projeto

### Hierarquia de Classes (OOP)

```
Graph (Classe Abstrata)
├── numNodes() / number_of_nodes()
├── numEdges() / number_of_edges()
├── degreeSequence() / degree_sequence()
├── addEdge() / add_edge()
├── removeEdge() / remove_edge()
└── print()

DenseGraph (Implementação Concreta)
├── Herda de Graph
├── Usa matriz de adjacência
└── Implementa todos os métodos abstratos
```

## 📈 Comparação de Implementações

| Aspecto | Lista de Adjacência | Matriz de Adjacência |
|---------|-------------------|---------------------|
| **Espaço** | O(V + E) | O(V²) |
| **Verificar aresta** | O(grau) | O(1) |
| **Adicionar aresta** | O(1) | O(1) |
| **Listar vizinhos** | O(grau) | O(V) |
| **Melhor para** | Grafos esparsos | Grafos densos |

## 🔍 Correções Identificadas

### JavaScript (Matriz de Adjacência)
```javascript
// Erros de digitação corrigidos:
addEgde → addEdge
removeEgde → removeEdge
```

### Python (Matriz de Adjacência)
```python
// Erro de digitação corrigido:
number_of_egdes → number_of_edges
```

## 🎨 Recursos Visuais

### p5.js Features
- Layout circular automático dos vértices
- Renderização em tempo real
- Cores personalizáveis
- Interface web interativa

### NetworkX Features
- Algoritmos de layout avançados (spring, circular, etc.)
- Visualização profissional
- Suporte a labels e pesos
- Múltiplas opções de estilização

## 💡 Casos de Uso por Implementação

### Lista de Adjacência
- Redes sociais (poucos amigos por pessoa)
- Grafos de dependências
- Árvores e florestas

### Matriz de Adjacência
- Grafos completos ou quase completos
- Algoritmos que requerem acesso rápido às arestas
- Análise de conectividade

### Visualizações
- Apresentações acadêmicas
- Debugging de algoritmos
- Análise exploratória de dados

## 🚦 Pré-requisitos

### Básico
- **JavaScript**: Node.js 12+
- **Python**: Python 3.6+

### Visualizações
- **p5.js**: Navegador web moderno
- **NetworkX**: `pip install networkx matplotlib`

## 📄 Licença

Este projeto é de domínio público e pode ser usado livremente para fins educacionais e comerciais.