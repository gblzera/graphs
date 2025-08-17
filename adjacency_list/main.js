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
}

// test
let V = ["A","B","C","D","E"];
let E = [["A","B"], ["A","C"], ["C","D"], ["C","E"], ["B","D"]];

let g = new ListGraph(V);
E.forEach(([u,v]) => g.add_edge(u, v));

g.print();
console.log("DFS starting from A:");
g.dfs("A");

console.log("\n\nRemoving edge (A,C)...");
g.remove_edge("A", "C");
g.print();
console.log("DFS starting from A after removing edge (A,C):");
g.dfs("A");
