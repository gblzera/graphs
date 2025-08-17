# Aulas e Estudos de Grafos – Representações e Busca

Este projeto reúne implementações de **estruturas de grafos** e **algoritmos de busca (DFS e BFS)** em **Python** e **JavaScript**, acompanhados de **visualizações gráficas** para fins didáticos.

## Estrutura 

- **adjacency_list/**  
  Implementações de grafos usando **Lista de Adjacência**, com suporte a **DFS (busca em profundidade)**.

- **adjacency_matrix/**  
  Implementações de grafos usando **Matriz de Adjacência**, incluindo operações básicas (adicionar/remover arestas, imprimir grafo, sequência de graus, etc.).

- **dfs/**  
  Visualizações do algoritmo **DFS** passo a passo, mostrando o processo de visitação dos nós.

- **bfs/**  
  Visualizações do algoritmo **BFS** passo a passo, mostrando a visita em largura.

## Linguagens

Cada pasta contém implementações em:
- **Python** (didático e com uso de bibliotecas como `networkx` + `matplotlib` para visualização).  
- **JavaScript** (usando `p5.js` para visualização interativa em navegador).

## Objetivo

Este repositório serve para:
- Aprender diferentes formas de representar grafos (matriz × lista).  
- Explorar algoritmos clássicos de busca (DFS e BFS).  
- Comparar representações e ver o impacto delas em código.  
- Demonstrar com **visualizações animadas** como cada algoritmo percorre o grafo.

## 🚀 Como Executar

### Python
1. Instale dependências:
   ```bash
   pip install networkx matplotlib
    Execute qualquer arquivo .py:
    python dfs/dfs_visualizer.py

### JavaScript
    ```bash
    Abra o arquivo .html correspondente no navegador.
    O grafo e as animações aparecerão automaticamente (usando p5.js).