# --- Parceiro de Programação: Análise de Tríades (Versão Otimizada) ---
import networkx as nx

# --------------------------------------------------------------------
# A parte de carregar os dados (que já tínhamos)
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


def analisar_rede_otimizado(lista_de_arestas):
    """
    Função otimizada que usa as funções 'built-in' do networkx
    para calcular tríades abertas e fechadas.
    """
    
    # --- PASSO 1: Construir o Grafo ---
    G = nx.Graph()
    G.add_edges_from(lista_de_arestas)
    
    print(f"Rede carregada com sucesso.")
    print(f"Total de Pessoas (Nós): {G.number_of_nodes()}")
    print(f"Total de Conexões (Arestas): {G.number_of_edges()}")
    print("-" * 30)

    # --- PASSO 2: Cálculo Otimizado ---

    # 1. Tríades Fechadas (Triângulos)
    # A função nx.triangles(G) retorna um dicionário: {nó: num_triangulos_que_ele_contém}
    # Como cada triângulo (A,B,C) é contado 3 vezes (uma para A, uma para B, uma para C),
    # nós somamos todos os valores e dividimos por 3.
    triangulos_por_no = nx.triangles(G).values()
    total_fechadas = sum(triangulos_por_no) // 3

    # 2. Tríades Abertas
    # Uma tríade (aberta ou fechada) é um "caminho de tamanho 2"
    # (Ex: A-B-C). O nó central é 'B'.
    # Para cada nó 'v', o número de tríades centradas nele é
    # igual ao número de combinações de 2 vizinhos.
    # Fórmula: (grau * (grau - 1)) / 2
    total_triades_potenciais = 0
    for v in G.nodes():
        grau = G.degree(v)
        if grau >= 2:
            total_triades_potenciais += (grau * (grau - 1)) // 2
            
    # As Tríades Abertas são todas as tríades potenciais
    # MENOS as que já contámos como fechadas.
    total_abertas = total_triades_potenciais - total_fechadas

    # --- PASSO 3: Resultados ---
    print(f"Resultados da Análise (Otimizada):")
    print(f"\n✅ Total de TRÍADES FECHADAS (Triângulos): {total_fechadas}")
    print(f"\n🔶 Total de TRÍADES ABERTAS: {total_abertas}")
    print("-" * 30)


# --- Execução do Programa Otimizado ---
# (Certifique-se de ter o 'networkx' instalado: pip install networkx)
analisar_rede_otimizado(lista_de_arestas)