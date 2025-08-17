# DFS Visualization Project

Este projeto implementa visualizações animadas do algoritmo **Depth-First Search (DFS)** em grafos, disponível em duas versões: uma versão web interativa usando p5.js e uma versão desktop usando Python com NetworkX e Matplotlib.

## 🌐 Versão Web (main.html)

### Características
- Visualização em tempo real do algoritmo DFS
- Interface web responsiva usando p5.js
- Animação automática com 1 passo por segundo
- Nós visitados destacados em verde
- Layout circular dos vértices

### Como Executar
1. Abra o arquivo `main.html` em qualquer navegador moderno
2. A animação iniciará automaticamente
3. Observe como o algoritmo DFS percorre o grafo a partir do vértice "B"

### Grafo Utilizado
- **Vértices**: A, B, C, D, E
- **Arestas**: A-C, B-D, C-E, D-E

### Tecnologias
- HTML5
- JavaScript
- p5.js (biblioteca de visualização)

## 🐍 Versão Python (main.py)

### Características
- Implementação completa com NetworkX
- Animação interativa usando Matplotlib
- Demonstração com modificação do grafo (remoção de aresta)
- Layout spring para posicionamento automático dos nós

### Dependências
```bash
pip install networkx matplotlib
```

### Como Executar
```bash
python main.py
```

### Funcionalidades
1. **DFS Completo**: Executa DFS no grafo original a partir do vértice "A"
2. **Modificação do Grafo**: Remove a aresta (C,E) e executa DFS novamente
3. **Visualização Animada**: Mostra cada passo do algoritmo com pausa de 1 segundo

### Grafo Utilizado
- **Vértices**: A, B, C, D, E
- **Arestas Iniciais**: A-B, A-C, B-D, C-E, D-E
- **Após Modificação**: Remove aresta C-E

## 🎯 Algoritmo DFS

O **Depth-First Search** é um algoritmo de busca em grafos que:

1. Visita um vértice e o marca como visitado
2. Recursivamente visita todos os vizinhos não visitados
3. Retrocede quando não há mais vizinhos não visitados
4. Continua até que todos os vértices acessíveis sejam visitados

### Complexidade
- **Tempo**: O(V + E), onde V = vértices e E = arestas
- **Espaço**: O(V) para a pilha de recursão

## 🎨 Visualização

### Cores dos Nós
- **Azul Claro**: Nós não visitados
- **Verde Claro**: Nós já visitados pelo algoritmo

### Layout
- **Versão Web**: Disposição circular dos vértices
- **Versão Python**: Layout spring (posicionamento automático)

## 🛠️ Personalização

### Modificar o Grafo (versão web)
Edite as variáveis no início do arquivo `main.html`:
```javascript
let vertices = ["A","B","C","D","E"];
let edges = [["A","C"],["B","D"],["C","E"],["D","E"]];
```

### Modificar o Grafo (versão Python)
Edite as listas no final do arquivo `main.py`:
```python
V = ["A","B","C","D","E"]
E = [("A","B"), ("A","C"), ("B","D"), ("C","E"), ("D","E")]
```

## 📚 Recursos Educacionais

Este projeto é ideal para:
- Aprendizado de algoritmos de grafos
- Visualização de estruturas de dados
- Compreensão do comportamento do DFS
- Comparação entre diferentes implementações

## 📄 Licença

Este projeto está disponível para uso educacional e pode ser modificado livremente.