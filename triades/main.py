# --- Parceiro de Programação: Análise de Tríades (Versão Correta) ---
import networkx as nx
import itertools # Vamos usar o 'itertools' novamente

# --------------------------------------------------------------------
# A parte de carregar os dados
# COLE AQUI A SUA LISTA 'arestas_raw'
# (Eu vou usar a minha, mas se a sua for diferente, use a sua)
# --------------------------------------------------------------------
arestas_raw = [
    # Preta
    ("Domingo", "carlos"), ("domingo", "alejandro"), ("domingo", "eduardo"),
    ("carlos", "alejandro"), ("carlos", "eduardo"), ("carlos", "domingo"),
    ("eduardo", "domingo"), ("eduardo", "carlos"), ("eduardo", "alejandro"),
    ("Alejandro", "carlos"), ("alejandro", "domingo"), ("alejandro", "eduardo"),
    # Cinza
    ("bob", "mike"), ("bob", "lanny"), ("bob", "hal"), ("bob", "ike"), ("bob", "john"),
    ("mike", "bob"), ("mike", "ike"), ("ike", "bob"), ("ike", "mike"), ("ike", "gill"),
    ("hal", "bob"), ("hal", "john"), ("hal", "gill"), ("frank", "gill"), ("gill", "ike"),
    ("gill", "hal"), ("gill", "john"), ("john", "bob"), ("john", "hal"), ("john", "gill"),
    ("john", "lanny"), ("john", "karl"), ("lanny", "bob"), ("lanny", "john"), ("lanny", "karl"),
    ("karl", "lanny"), ("karl", "john"),
    # Branca
    ("ozzie", "norm"), ("norm", "ozzie"), ("norm", "paul"), ("norm", "utrecht"),
    ("norm", "sam"), ("norm", "vern"), ("paul", "norm"), ("paul", "quint"),
    ("quint", "paul"), ("quint", "utrecht"), ("quint", "russ"), ("utrecht", "quint"),
    ("utrecht", "norm"), ("utrecht", "sam"), ("utrecht", "russ"), ("russ", "utrecht"),
    ("russ", "quint"), ("russ", "ted"), ("ted", "russ"), ("ted", "vern"),
    ("sam", "utrecht"), ("sam", "norm"), ("sam", "xavier"), ("sam", "wendle"),
    ("xavier", "sam"), ("xavier", "wendle"), ("wendle", "xavier"), ("wendle", "sam"),
    # Entre Cores
    ("alejandro", "bob"), ("bob", "norm"), ("karl", "ozzie"),
    ("bob", "alejandro"), ("ozzie", "karl"), ("norm", "bob")
]

# Normalização (a mesma de antes)
arestas_processadas = set()
for u, v in arestas_raw:
    u_norm = u.lower()
    v_norm = v.lower()
    if u_norm < v_norm:
        arestas_processadas.add((u_norm, v_norm))
    else:
        arestas_processadas.add((v_norm, u_norm))

lista_de_arestas = list(arestas_processadas)
# --------------------------------------------------------------------
# Fim da parte de carregar os dados
# --------------------------------------------------------------------


def encontrar_triades_corretamente(lista_de_arestas):
    """
    Função (o nosso script manual original) que itera por todas as
    combinações para encontrar tríades únicas. Este método é o mais seguro.
    """
    
    # --- PASSO 1: Construir o Grafo ---
    G = nx.Graph()
    G.add_edges_from(lista_de_arestas)

    print(f"Rede carregada com sucesso.")
    print(f"Total de Pessoas (Nós): {G.number_of_nodes()}")
    print(f"Total de Conexões (Arestas): {G.number_of_edges()}")
    print("-" * 30)

    # Listas para guardar os nossos resultados
    triades_fechadas_set = set() # Usamos 'set' para evitar duplicados
    triades_abertas_set = set()  # (ex: A-B-C é o mesmo que B-C-A)

    # --- PASSO 2: O "Coração" do Algoritmo ---
    # Iteramos por CADA nó (pessoa) na rede.
    for v in G.nodes():
        
        vizinhos = list(G.neighbors(v))
        if len(vizinhos) < 2:
            continue
            
        # Vemos todas as combinações de 2 vizinhos
        for u, w in itertools.combinations(vizinhos, 2):
            
            # 'v' é o centro. 'u' e 'w' são os vizinhos.
            # Criamos uma chave única (frozenset) para a tríade {u, v, w}
            chave_triade = frozenset([u, v, w])

            if G.has_edge(u, w):
                # TRÍADE FECHADA (TRIÂNGULO)
                triades_fechadas_set.add(chave_triade)
            else:
                # TRÍADE ABERTA
                triades_abertas_set.add(chave_triade)

    # --- PASSO 3: Apresentar os Resultados ---
    print(f"Resultados da Análise (Método Correto - 'itertools'):")
    
    print(f"\n✅ Total de TRÍADES FECHADAS (Triângulos): {len(triades_fechadas_set)}")
    print(f"\n🔶 Total de TRÍADES ABERTAS: {len(triades_abertas_set)}")
    print("-" * 30)


# --- Execução do Programa ---
# (Certifique-se de ter o 'networkx' instalado: pip install networkx)
encontrar_triades_corretamente(lista_de_arestas)