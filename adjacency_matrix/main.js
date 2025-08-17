class Graph{
    numNodes() {throw new Error("Not implemented");}
    numEdges() {throw new Error("Not implemented");}
    degreeSequence() {throw new Error("Not implemented");}
    addEdge(u, v) {throw new Error("Not implemented");}
    removeEdge(u, v) {throw new Error("Not implemented");}
    print() {throw new Error("Not implemented");}
}

class DenseGraph extends Graph{
    constructor(nodes) {
        super();
        this.rotules = nodes;
        this.n = nodes.length;
        this.matrix = Array.from({ length: this.n}, () => Array(this.n).fill(0));
    }

    numNodes(){
        return this.n;
    }

    numEdges(){
        let count = 0;
        for( let i=0; i < this.n; i++){
            for (let j=0; j < this.n; j++){
                count += this.matrix[i][j];
            }
        }
        return count / 2;
    }

    degreeSequence(){
        return this.matrix.map(row => row.reduce((a,b) => a + b, 0));
    }

    addEgde(u,v){
        let i = this.rotules.indexOf(u);
        let j = this.rotules.indexOf(v);
        if (this.matrix[i][j] === 0){
            this.matrix[i][j] = this.matrix[j][i] = 1;
        }
    }

    removeEgde(u,v){
        let i = this.rotules.indexOf(u);
        let j = this.rotules.indexOf(v);
        if (this.matrix[i][j] === 1){
            this.matrix[i][j] = this.matrix[j][i] = 0;
        }
    }

    print(){
        console.log("Adjacency Matrix:");
        console.log("  " + this.rotules.join(" "));
        for(let i = 0; i < this.n; i++){
            console.log(this.rotules[i] + " " + this.matrix[i].join(" ") );
        }
    }
}

// test
let V = ['A', 'B', 'C', 'D', 'E'];
let E = [["A","B"],["A","C"],["C","D"],["C","E"],["B","D"]];

let g = new DenseGraph(V);
E.forEach(([u,v]) => g.addEgde(u,v));
g.print();

console.log("Number of nodes:", g.numNodes());
console.log("Number of edges:", g.numEdges());
console.log("Degree sequence:", g.degreeSequence());

console.log("Removing edge (A, C)...");
g.removeEgde("A","C");
g.print();