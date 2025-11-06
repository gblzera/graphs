/*
 * --- Parceiro de Programação: Algoritmo de Bellman-Ford em C++ ---
 *
 * Incluímos as bibliotecas necessárias:
 * <iostream> - Para imprimir no console (ex: std::cout)
 * <vector>   - Para usar a estrutura de dados 'vector' (lista/array dinâmico)
 * <climits>  - Para usar o valor 'INT_MAX' (o nosso "Infinito")
 * <string>   - Para usar 'std::string' (para os nomes dos nós)
 */
#include <iostream>
#include <vector>
#include <climits>
#include <string>

// Para representar o "Infinito", usamos o maior valor inteiro possível.
// É uma prática comum em C++ para algoritmos de grafos.
#define INF INT_MAX

/**
 * @brief Estrutura de Dados para Aresta
 *
 * Em C++, é uma boa prática criar uma 'struct' (estrutura) para
 * organizar dados relacionados. Esta struct representa uma única
 * aresta (seta) no nosso grafo.
 */
struct Aresta {
    int origem;  // Nó de origem (ex: 'S' = 0)
    int destino; // Nó de destino (ex: 'A' = 1)
    int peso;    // O custo da aresta (ex: 3)
};

/**
 * @brief Função principal do Bellman-Ford
 *
 * Argumentos:
 * grafo (vector<Aresta>): A lista de todas as arestas.
 * V (int): O número total de Vértices (nós).
 * E (int): O número total de Arestas (conexões).
 * origem (int): O índice do nó inicial (0).
 *
 * Retorna:
 * Um 'vector<int>' com as distâncias.
 * Se um ciclo negativo for detetado, retorna um vetor vazio.
 */
std::vector<int> bellmanFord(const std::vector<Aresta>& grafo, int V, int E, int origem) {

    // --- PASSO 1: INICIALIZAÇÃO ---
    // Criamos um vetor para armazenar as distâncias.
    // std::vector<int> distancias(V, INF);
    // (V = tamanho do vetor, INF = valor inicial de todos os elementos)
    std::vector<int> distancias(V, INF);

    // A distância da origem para ela mesma é 0.
    distancias[origem] = 0;

    // --- PASSO 2: RELAXAMENTO (O "Coração" do Algoritmo) ---
    // Repetimos o processo V-1 vezes.
    for (int i = 0; i < V - 1; ++i) {
        
        // Em cada iteração, passamos por TODAS as arestas (E arestas).
        // Usamos 'const auto& aresta' para iterar pela lista de forma eficiente.
        for (const auto& aresta : grafo) {
            int u = aresta.origem;
            int v = aresta.destino;
            int peso = aresta.peso;

            // Verificamos se encontramos um caminho MAIS CURTO:
            // 1. A distância até 'u' NÃO é infinita (distancias[u] != INF)
            //    (Esta verificação também previne 'overflow' (INF + peso))
            // 2. E se o caminho (distancia[u] + peso) é MENOR que a distância para 'v'
            if (distancias[u] != INF && distancias[u] + peso < distancias[v]) {
                // Se for, atualizamos a distância para 'v'.
                distancias[v] = distancias[u] + peso;
            }
        }
    }

    // --- PASSO 3: VERIFICAÇÃO DE CICLO NEGATIVO ---
    // Fazemos uma passagem ADICIONAL por todas as arestas.
    for (const auto& aresta : grafo) {
        int u = aresta.origem;
        int v = aresta.destino;
        int peso = aresta.peso;

        // Se, mesmo depois de V-1 iterações, ainda conseguirmos encurtar um caminho...
        if (distancias[u] != INF && distancias[u] + peso < distancias[v]) {
            // ...significa que há um ciclo negativo.
            // Usamos 'std::cout' para imprimir e 'std::endl' para nova linha.
            std::cout << "❌ Erro: O grafo contém um ciclo de peso negativo!" << std::endl;
            // Retornamos um vetor vazio '{}' para sinalizar o erro.
            return {};
        }
    }

    // Se tudo correu bem, retorna o vetor com as distâncias finais.
    return distancias;
}


/**
 * @brief Função principal 'main'
 *
 * Em C++, a execução do programa começa sempre pela função 'main'.
 */
int main() {
    
    // --- Configuração do Nosso Grafo (O seu grafo com ciclo) ---

    // Total de Vértices (Nós): S, A, B, C, D
    int V = 5;
    // Total de Arestas (Setas)
    int E = 9;

    // Mapeamento: S=0, A=1, B=2, C=3, D=4
    int origem = 0; // 'S'

    // Criamos um 'std::vector' do tipo 'Aresta' para guardar o grafo.
    // Usamos {} para inicializar os valores da nossa struct (origem, destino, peso).
    std::vector<Aresta> grafo = {
        {0, 1, 3},    // S -> A
        {0, 2, 5},    // S -> B
        {1, 3, -5},   // A -> C
        {1, 4, 8},    // A -> D
        {2, 1, 6},    // B -> A
        {2, 3, 8},    // B -> C
        {2, 4, -9},   // B -> D
        {4, 0, 2},    // D -> S (O ciclo!)
        {3, 4, -3}    // C -> D
    };

    // --- Execução do Programa ---

    // Chamamos a função e guardamos o resultado
    std::vector<int> resultados = bellmanFord(grafo, V, E, origem);

    // --- Apresentação dos Resultados ---

    // Verificamos se o vetor de resultados NÃO está vazio
    // (Se estiver vazio, significa que 'bellmanFord' detetou um ciclo)
    if (!resultados.empty()) {
        std::cout << "Resultados do Algoritmo Bellman-Ford (Origem: 'S')" << std::endl;
        std::cout << "-----------------------------------------------------" << std::endl;

        // Criamos um vetor de strings para os nomes, facilitando a leitura
        std::vector<std::string> nomes_nos = {"S", "A", "B", "C", "D"};

        // Usamos um loop 'for' clássico para imprimir os resultados
        for (int i = 0; i < V; ++i) {
            std::cout << "Distância mais curta de 'S' para '" << nomes_nos[i] 
                      << "': " << resultados[i] << std::endl;
        }
    }

    // 'return 0' indica que o programa terminou com sucesso.
    return 0;
}