class ListGraph{
    constructor(nodes) {
        this.nodes = nodes;
        this.adj = {};
        nodes.forEach(v => this.adj[v] = []);
    }

    add_edge(u, v){
        if(!this.adj[u].includes(v)){
            this.adj[u].push(v);
            this.adj[v].push(u); // undirected graph
        }
    }

    remove_edge(u,v){
        this.adj[u] = this.adj[u].filter(x => x !== v);
        this.adj[v] = this.adj[v].filter(x => x !== u);
    }

    print(){
        console.log("Adjacency List:");
        for (let v of this.nodes) {
            console.log(v, "->", this.adj[v]);
        }
    }

    dfs(start, visited = new Set()){
        visited.add(start);
        process.stdout.write(start + " ");
        for (let neighbor of this.adj[start]){
            if (!visited.has(neighbor)){
                this.dfs(neighbor, visited);
            }
        }
    }

    // retorna os vértices
    get_vertices(){
        return this.nodes;
    }

    // retorna as arestas como pares [u,v]
    get_arestas(){
        let edges = [];
        for (let v of this.nodes) {
            for (let u of this.adj[v]) {
                if (this.nodes.indexOf(u) > this.nodes.indexOf(v)) {
                    edges.push([v, u]);
                }
            }
        }
        return edges;
    }

    // verifica se "outro" é subgrafo
    is_subgrafo(outro){
        for (let v of outro.get_vertices()){
            if (!this.nodes.includes(v)) return false;
        }
        for (let [u,v] of outro.get_arestas()){
            if (!this.adj[u].includes(v)) return false;
        }
        return true;
    }

    // verifica se é subgrafo gerador
    is_subgrafo_gerador(outro){
        if (this.nodes.length !== outro.get_vertices().length) return false;
        for (let v of this.nodes){
            if (!outro.get_vertices().includes(v)) return false;
        }
        for (let [u,v] of outro.get_arestas()){
            if (!this.adj[u].includes(v)) return false;
        }
        return true;
    }

    // verifica se é subgrafo induzido
    is_subgrafo_induzido(outro){
        if (this.nodes.length !== outro.get_vertices().length) return false;
        for (let v of this.nodes){
            if (!outro.get_vertices().includes(v)) return false;
        }
        for (let v of this.nodes){
            for (let u of this.nodes){
                if (u !== v){
                    let temAqui = this.adj[v].includes(u);
                    let temOutro = outro.adj[v].includes(u);
                    if (temAqui !== temOutro) return false;
                }
            }
        }
        return true;
    }

    // Verifica se o grafo é nulo (sem arestas)
    is_null(){
        for (let v of this.nodes) {
            if (this.adj[v].length > 0) {
                return false;
            }
        }
        return true;
    }

    // Verifica se o grafo é simples (sem laços e sem arestas múltiplas)
    is_simple(){
        for (let v of this.nodes) {
            if (this.adj[v].includes(v)) {
                return false;
            }
            let unique_neighbors = new Set(this.adj[v]);
            if (unique_neighbors.size !== this.adj[v].length) {
                return false;
            }
        }
        return true;
    }

    // Verifica se o grafo é completo (todos os vértices conectados entre si)
    is_complete(){
        let n = this.nodes.length;
        for (let v of this.nodes) {
            if (this.adj[v].length !== n - 1) {
                return false;
            }
            for (let u of this.nodes) {
                if (u !== v && !this.adj[v].includes(u)) {
                    return false;
                }
            }
        }
        return true;
    }

    analyze(){
        console.log("\n=== ANÁLISE DO GRAFO ===");
        console.log("Grafo nulo:", this.is_null());
        console.log("Grafo simples:", this.is_simple());
        console.log("Grafo completo:", this.is_complete());
        
        if (this.is_null()) {
            console.log("→ Este é um grafo NULO (sem arestas)");
        } else if (this.is_complete()) {
            console.log("→ Este é um grafo COMPLETO (todos os vértices conectados)");
        } else if (this.is_simple()) {
            console.log("→ Este é um grafo SIMPLES (sem laços nem arestas múltiplas)");
        } else {
            console.log("→ Este grafo não é simples (possui laços ou arestas múltiplas)");
        }
    }
}


// testes

console.log("=== TESTE 1: Grafo Original ===");
let V = ["A","B","C","D","E"];
let E = [["A","B"], ["A","C"], ["C","D"], ["C","E"], ["B","D"]];

let g = new ListGraph(V);
E.forEach(([u,v]) => g.add_edge(u, v));

g.print();
g.analyze();

console.log("\nVertices:", g.get_vertices());
console.log("Arestas:", g.get_arestas());

console.log("\n\n=== TESTE SUBGRAFO ===");
let G1 = new ListGraph(["A","B","C"]);
G1.add_edge("A","B");
G1.add_edge("B","C");

let G2 = new ListGraph(["A","B"]);
G2.add_edge("A","B");

console.log("G2 é subgrafo de G1?", G1.is_subgrafo(G2));
console.log("G2 é subgrafo gerador de G1?", G1.is_subgrafo_gerador(G2));
console.log("G2 é subgrafo induzido de G1?", G1.is_subgrafo_induzido(G2));
