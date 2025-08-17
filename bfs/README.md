# BFS Visualizer

Um visualizador interativo do algoritmo Breadth-First Search (BFS) utilizando NetworkX e Matplotlib.

## Descrição

Este projeto implementa uma visualização animada do algoritmo de busca em largura (BFS) em grafos. O programa permite observar como o algoritmo explora os nós do grafo passo a passo, destacando visualmente os nós visitados e não visitados.

## Funcionalidades

- Visualização animada do algoritmo BFS
- Destaque visual dos nós visitados (verde claro) e não visitados (azul claro)
- Layout automático dos nós usando spring layout
- Demonstração com modificação de grafo (remoção de arestas)
- Interface interativa com pausas entre cada passo

## Pré-requisitos

Certifique-se de ter o Python instalado (versão 3.6+) junto com as seguintes bibliotecas:

```bash
pip install networkx matplotlib
```

## Como usar

1. Clone ou baixe o arquivo `main.py`
2. Execute o script:

```bash
python main.py
```

3. O programa executará duas visualizações:
   - Primeiro: BFS no grafo completo
   - Segundo: BFS após remover a aresta (C,E)

## Estrutura do Código

### Função Principal: `bfs_visualizer(G, start)`

- **G**: Grafo NetworkX
- **start**: Nó inicial para começar a busca

### Algoritmo

1. Inicializa uma fila com o nó inicial
2. Para cada nó na fila:
   - Marca como visitado
   - Atualiza a visualização
   - Adiciona vizinhos não visitados à fila
   - Pausa por 1 segundo para visualização

### Grafo de Exemplo

O programa usa um grafo com:
- **Nós**: A, B, C, D, E
- **Arestas**: (A,B), (A,C), (B,D), (C,E), (D,E)

## Cores da Visualização

- **Azul claro**: Nós não visitados
- **Verde claro**: Nós já visitados
- **Destaque**: Nó sendo visitado atualmente

## Personalização

Para usar com seu próprio grafo, modifique as variáveis:

```python
# Seus nós
V = ["X", "Y", "Z"]  

# Suas arestas
E = [("X", "Y"), ("Y", "Z")]

# Nó inicial
bfs_visualizer(G, "X")
```

## Exemplo de Saída

O programa mostra:
1. Título indicando o nó sendo visitado
2. Grafo colorido com nós visitados/não visitados
3. Animação passo a passo do algoritmo BFS

## Controles

- **Fechar janela**: Para interromper a visualização
- **Aguardar**: O programa pausa automaticamente entre cada passo

## Aplicações Educacionais

Este visualizador é útil para:
- Ensinar algoritmos de grafos
- Demonstrar como BFS funciona
- Comparar comportamento em diferentes estruturas de grafo
- Visualizar o impacto de modificações no grafo

## Requisitos do Sistema

- Python 3.6+
- NetworkX
- Matplotlib
- Sistema com interface gráfica para exibição

## 📄 Licença

Este projeto é de domínio público e pode ser usado livremente para fins educacionais e comerciais.