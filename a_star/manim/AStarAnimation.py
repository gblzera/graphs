from manim import *

class AStarVisualization(Scene):
    def construct(self):
        # --- TÍTULO E INTRODUÇÃO ---
        title = Text("Algoritmo A*", font_size=70, color=YELLOW, weight=BOLD)
        subtitle = Text("Busca Informada por Custo + Heurística", font_size=35, color=GRAY)
        subtitle.next_to(title, DOWN, buff=0.3)
        title_group = VGroup(title, subtitle)
        
        self.play(Write(title, run_time=1.5), FadeIn(subtitle, shift=UP))
        self.wait(2.5)
        self.play(title_group.animate.scale(0.6).to_edge(UP), run_time=1)
        self.wait(1)

        # --- O QUE É A* ---
        what_title = Text("O que é o A*?", font_size=50, color=TEAL, weight=BOLD)
        what_title.to_edge(UP)
        self.play(Transform(title_group, what_title))
        self.wait(0.5)
        
        what_desc = VGroup(
            Text("• Algoritmo de busca de caminho mais curto", font_size=32),
            Text("• Combina estratégias de Dijkstra e Busca Gulosa", font_size=32),
            Text("• Usa conhecimento do problema (heurística)", font_size=32),
            Text("• Muito usado em IA, jogos e navegação", font_size=32),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.4)
        what_desc.shift(DOWN * 0.5)
        
        for item in what_desc:
            self.play(FadeIn(item, shift=RIGHT), run_time=0.8)
            self.wait(2)
        
        self.wait(2)
        self.play(FadeOut(what_desc), run_time=0.8)
        self.wait(1)

        # --- FÓRMULA FUNDAMENTAL (SEM LATEX) ---
        formula_title = Text("Fórmula Fundamental do A*", font_size=50, color=ORANGE, weight=BOLD)
        formula_title.to_edge(UP)
        self.play(Transform(title_group, formula_title), run_time=0.8)
        self.wait(1)
        
        # Fórmula principal usando Text
        formula = Text("f(n) = g(n) + h(n)", font_size=80, color=YELLOW, weight=BOLD)
        self.play(Write(formula, run_time=1.5))
        self.wait(2.5)
        
        # Explicações dos componentes
        g_exp = VGroup(
            Text("g(n)", font_size=60, color=BLUE, weight=BOLD),
            Text("= Custo real do início até n", font_size=28)
        ).arrange(RIGHT, buff=0.5)
        g_exp.move_to(UP * 1.2)
        
        h_exp = VGroup(
            Text("h(n)", font_size=60, color=RED, weight=BOLD),
            Text("= Estimativa (heurística) de n até o objetivo", font_size=28)
        ).arrange(RIGHT, buff=0.5)
        h_exp.next_to(g_exp, DOWN, buff=0.6)
        
        f_exp = VGroup(
            Text("f(n)", font_size=60, color=YELLOW, weight=BOLD),
            Text("= Custo total estimado do caminho", font_size=28)
        ).arrange(RIGHT, buff=0.5)
        f_exp.next_to(h_exp, DOWN, buff=0.6)
        
        self.play(FadeOut(formula), run_time=0.6)
        self.wait(0.5)
        
        for exp in [g_exp, h_exp, f_exp]:
            self.play(FadeIn(exp, shift=UP), run_time=1)
            self.wait(2.5)
        
        self.wait(2)
        self.play(FadeOut(g_exp), FadeOut(h_exp), FadeOut(f_exp), run_time=0.8)
        self.wait(1)

        # --- CARACTERÍSTICAS PRINCIPAIS ---
        char_title = Text("Características Principais", font_size=50, color=TEAL, weight=BOLD)
        char_title.to_edge(UP)
        self.play(Transform(title_group, char_title), run_time=0.8)
        self.wait(1)
        
        characteristics = [
            ("🧠", "Usa heurística para guiar a busca de forma inteligente", BLUE),
            ("⚖️", "Equilibra exploração (g) e estimativa (h)", GREEN),
            ("🎯", "Garante caminho ótimo se h é admissível", YELLOW),
            ("📦", "Usa fila de prioridade (Min-Heap)", ORANGE),
            ("🚀", "Mais eficiente que Dijkstra em muitos casos", RED),
            ("✅", "Completo e ótimo quando bem configurado", PURPLE),
        ]

        char_group = VGroup()
        for icon, text, color in characteristics:
            item = VGroup(
                Text(icon, font_size=40),
                Text(text, font_size=28, color=color)
            ).arrange(RIGHT, buff=0.4)
            char_group.add(item)
        char_group.arrange(DOWN, aligned_edge=LEFT, buff=0.45)
        char_group.shift(DOWN * 0.3)

        for item in char_group:
            self.play(FadeIn(item, shift=RIGHT), run_time=0.7)
            self.wait(2.5)
        
        self.wait(2)
        self.play(FadeOut(char_group), run_time=0.8)
        self.wait(1)

        # --- HEURÍSTICA ADMISSÍVEL ---
        heur_title = Text("Heurística Admissível", font_size=50, color=PURPLE, weight=BOLD)
        heur_title.to_edge(UP)
        self.play(Transform(title_group, heur_title), run_time=0.8)
        self.wait(1)
        
        heur_def = VGroup(
            Text("Uma heurística é ADMISSÍVEL quando:", font_size=36, color=WHITE),
            Text("h(n) ≤ h*(n)", font_size=70, color=YELLOW, weight=BOLD),
            Text("Nunca superestima o custo real até o objetivo", font_size=30, color=GRAY),
        ).arrange(DOWN, buff=0.6)
        
        for item in heur_def:
            self.play(Write(item), run_time=1.2)
            self.wait(2.5)
        
        self.wait(2)
        self.play(FadeOut(heur_def), run_time=0.8)
        self.wait(1)
        
        # Exemplos de heurísticas
        examples_text = Text("Exemplos de Heurísticas:", font_size=40, color=ORANGE)
        examples_text.to_edge(UP).shift(DOWN * 0.5)
        self.play(Write(examples_text), run_time=0.8)
        self.wait(1)
        
        examples = VGroup(
            Text("• Distância Manhattan (grade)", font_size=32, color=BLUE),
            Text("• Distância Euclidiana (espaço 2D)", font_size=32, color=GREEN),
            Text("• Distância de Chebyshev (diagonal)", font_size=32, color=YELLOW),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.5)
        examples.shift(DOWN * 0.8)
        
        for ex in examples:
            self.play(FadeIn(ex, shift=RIGHT), run_time=0.8)
            self.wait(2.5)
        
        self.wait(2)
        self.play(FadeOut(examples_text), FadeOut(examples), run_time=0.8)
        self.wait(1)

        # --- GRAFO DE EXEMPLO ---
        graph_title = Text("Simulação Visual do A*", font_size=50, color=TEAL, weight=BOLD)
        graph_title.to_edge(UP)
        self.play(Transform(title_group, graph_title), run_time=0.8)
        self.wait(1)

        # Definição do grafo
        vertices = ["S", "A", "B", "C", "D", "G"]
        edges = [
            ("S", "A"), ("S", "B"), 
            ("A", "C"), ("B", "C"),
            ("B", "D"), ("C", "G"), ("D", "G")
        ]
        layout = {
            "S": LEFT * 4.5 + UP * 1,
            "A": LEFT * 1.5 + UP * 2.5,
            "B": LEFT * 1.5 + DOWN * 1.5,
            "C": RIGHT * 2 + UP * 0.5,
            "D": RIGHT * 2 + DOWN * 2,
            "G": RIGHT * 5.5
        }
        weights = {
            ("S", "A"): 2, ("S", "B"): 1,
            ("A", "C"): 2, ("B", "C"): 5,
            ("B", "D"): 2, ("C", "G"): 3, ("D", "G"): 2
        }
        heuristics = {"S": 7, "A": 6, "B": 4, "C": 2, "D": 1, "G": 0}

        # Criar grafo
        graph = Graph(
            vertices, edges, layout=layout,
            vertex_config={"radius": 0.4, "color": BLUE, "fill_opacity": 0.9},
            edge_config={"stroke_width": 4, "color": GRAY}
        ).scale(0.85).shift(DOWN * 0.3)
        
        self.play(Create(graph, run_time=2))
        self.wait(2)

        # Labels dos vértices
        vertex_labels = {
            v: Text(v, font_size=32, color=WHITE, weight=BOLD).move_to(graph.vertices[v])
            for v in vertices
        }
        for lbl in vertex_labels.values():
            self.play(Write(lbl), run_time=0.3)
        self.wait(2)

        # Pesos das arestas
        edge_labels = {}
        for edge, weight in weights.items():
            edge_center = (graph.vertices[edge[0]].get_center() + graph.vertices[edge[1]].get_center()) / 2
            label = Text(str(weight), font_size=26, color=WHITE, weight=BOLD)
            label.move_to(edge_center)
            label.add_background_rectangle(color=BLACK, opacity=0.7, buff=0.1)
            edge_labels[edge] = label
            self.play(FadeIn(label, scale=0.8), run_time=0.3)
        self.wait(2)

        # Heurísticas
        h_labels = {}
        for v in vertices:
            h = heuristics[v]
            label = Text(f"h={h}", font_size=22, color=YELLOW, weight=BOLD)
            label.next_to(graph.vertices[v], DOWN, buff=0.2)
            h_labels[v] = label
            self.play(FadeIn(label, scale=0.8), run_time=0.3)
        self.wait(2.5)

        # --- LEGENDA ---
        legend = VGroup(
            VGroup(Circle(radius=0.15, color=GREEN, fill_opacity=0.8), Text("Fronteira", font_size=20)).arrange(RIGHT, buff=0.2),
            VGroup(Circle(radius=0.15, color=RED, fill_opacity=0.8), Text("Visitado", font_size=20)).arrange(RIGHT, buff=0.2),
            VGroup(Circle(radius=0.15, color=YELLOW, fill_opacity=0.8), Text("Objetivo", font_size=20)).arrange(RIGHT, buff=0.2),
        ).arrange(RIGHT, buff=0.6)
        legend.to_corner(DR).shift(UP * 0.5 + LEFT * 0.3)
        legend.add_background_rectangle(color=BLACK, opacity=0.8, buff=0.2)
        self.play(FadeIn(legend, shift=UP), run_time=0.8)
        self.wait(2)

        # --- SIMULAÇÃO PASSO A PASSO ---
        # Remover o título antigo
        self.play(FadeOut(title_group), run_time=0.6)
        self.wait(0.5)

        # Área para informações no topo
        info_box = Rectangle(width=13, height=1.3, color=BLUE, fill_opacity=0.2)
        info_box.to_edge(UP).shift(DOWN * 0.05)
        self.play(Create(info_box), run_time=0.6)
        
        def update_info(text, color=WHITE):
            info = Text(text, font_size=30, color=color, weight=BOLD)
            info.move_to(info_box)
            return info
        
        current_info = None

        def show_info(text, color=WHITE):
            nonlocal current_info
            new_info = update_info(text, color)
            if current_info:
                self.play(Transform(current_info, new_info), run_time=0.6)
            else:
                current_info = new_info
                self.play(FadeIn(current_info), run_time=0.6)
            self.wait(2)

        # Labels de g e f
        gf_labels = {}

        def add_gf_label(v, g, f):
            label = Text(f"g={g}, f={f}", font_size=20, color=WHITE, weight=BOLD)
            label.next_to(graph.vertices[v], UP, buff=0.15)
            label.add_background_rectangle(color=BLACK, opacity=0.8, buff=0.08)
            gf_labels[v] = label
            return label

        # PASSO 1: Inicializar com S
        show_info("Passo 1: Inicializar com nó inicial S", GREEN)
        self.play(graph.vertices["S"].animate.set_color(GREEN), run_time=0.8)
        self.wait(2)
        
        s_label = add_gf_label("S", 0, 7)
        self.play(FadeIn(s_label, scale=0.8), run_time=0.6)
        show_info("S: g(S)=0, h(S)=7 → f(S)=0+7=7", BLUE)
        self.wait(2.5)

        # PASSO 2: Expandir S
        show_info("Passo 2: Expandir S - menor f na fronteira", YELLOW)
        self.play(graph.vertices["S"].animate.set_color(RED), run_time=0.6)
        self.wait(2)
        
        self.play(
            graph.edges[("S", "A")].animate.set_color(YELLOW),
            graph.edges[("S", "B")].animate.set_color(YELLOW),
            run_time=0.8
        )
        self.wait(2)

        # Adicionar A e B à fronteira
        show_info("Adicionar vizinhos A e B à fronteira", GREEN)
        self.play(
            graph.vertices["A"].animate.set_color(GREEN),
            graph.vertices["B"].animate.set_color(GREEN),
            run_time=0.8
        )
        self.wait(2)
        
        a_label = add_gf_label("A", 2, 8)
        b_label = add_gf_label("B", 1, 5)
        self.play(FadeIn(a_label, scale=0.8), FadeIn(b_label, scale=0.8), run_time=0.6)
        show_info("A: g=2, f=8 | B: g=1, f=5 → Escolher B (menor f)", BLUE)
        self.wait(3)

        # PASSO 3: Expandir B
        show_info("Passo 3: Expandir B - menor f=5", YELLOW)
        self.play(graph.vertices["B"].animate.set_color(RED), run_time=0.6)
        self.wait(2)
        
        self.play(
            graph.edges[("B", "C")].animate.set_color(YELLOW),
            graph.edges[("B", "D")].animate.set_color(YELLOW),
            run_time=0.8
        )
        self.wait(2)

        # Adicionar C e D
        show_info("Adicionar vizinhos C e D à fronteira", GREEN)
        self.play(
            graph.vertices["C"].animate.set_color(GREEN),
            graph.vertices["D"].animate.set_color(GREEN),
            run_time=0.8
        )
        self.wait(2)
        
        c_label = add_gf_label("C", 6, 8)
        d_label = add_gf_label("D", 3, 4)
        self.play(FadeIn(c_label, scale=0.8), FadeIn(d_label, scale=0.8), run_time=0.6)
        show_info("C: g=6, f=8 | D: g=3, f=4 → Escolher D (menor f)", BLUE)
        self.wait(3)

        # PASSO 4: Expandir D
        show_info("Passo 4: Expandir D - menor f=4", YELLOW)
        self.play(graph.vertices["D"].animate.set_color(RED), run_time=0.6)
        self.wait(2)
        
        self.play(graph.edges[("D", "G")].animate.set_color(YELLOW), run_time=0.8)
        self.wait(2)

        # Encontrar objetivo
        show_info("Vizinho G encontrado - É o objetivo!", GREEN)
        self.play(graph.vertices["G"].animate.set_color(YELLOW), run_time=0.8)
        self.wait(2)
        
        g_label = add_gf_label("G", 5, 5)
        self.play(FadeIn(g_label, scale=0.8), run_time=0.6)
        show_info("G: g=5, f=5 | OBJETIVO ALCANÇADO!", GREEN)
        self.wait(3)

        # Destacar caminho ótimo
        self.play(FadeOut(current_info), run_time=0.6)
        self.wait(1)
        
        optimal_path = [("S", "B"), ("B", "D"), ("D", "G")]
        for edge in optimal_path:
            self.play(graph.edges[edge].animate.set_color(GREEN).set_stroke(width=8), run_time=0.6)
            self.wait(0.8)
        
        self.wait(2)

        # --- RESULTADO FINAL ---
        result_box = Rectangle(width=10, height=2.5, color=GREEN, fill_color=GREEN, fill_opacity=0.25)
        result_box.add(Rectangle(width=10, height=2.5, color=GREEN, stroke_width=6))
        
        result_text = Text("✓ Caminho Ótimo Encontrado!", font_size=42, color=GREEN, weight=BOLD)
        result_path = Text("S → B → D → G", font_size=48, color=YELLOW, weight=BOLD)
        result_cost = Text("Custo Total: 5", font_size=36, color=WHITE)
        
        result_group = VGroup(result_text, result_path, result_cost).arrange(DOWN, buff=0.35)
        final = VGroup(result_box, result_group)
        
        self.play(FadeIn(result_box, scale=0.9), run_time=0.8)
        self.wait(1)
        self.play(Write(result_text), run_time=1)
        self.wait(2)
        self.play(Write(result_path), run_time=1)
        self.wait(2)
        self.play(Write(result_cost), run_time=1)
        self.wait(3)

        # Limpar tela completamente antes da próxima seção
        all_graph_objects = [graph, result_box, result_group, legend, info_box]
        all_graph_objects.extend(vertex_labels.values())
        all_graph_objects.extend(edge_labels.values())
        all_graph_objects.extend(h_labels.values())
        all_graph_objects.extend(gf_labels.values())
        
        self.play(*[FadeOut(obj) for obj in all_graph_objects], run_time=1)
        self.wait(1)

        # --- COMPARAÇÃO COM OUTROS ALGORITMOS ---
        # Criar novo título para esta seção
        comp_title = Text("A* vs Outros Algoritmos", font_size=50, color=PURPLE, weight=BOLD)
        comp_title.to_edge(UP)
        self.play(FadeIn(comp_title), run_time=0.8)
        self.wait(1.5)
        
        comparison = VGroup(
            VGroup(
                Text("Dijkstra:", font_size=36, color=BLUE, weight=BOLD),
                Text("Explora todos os caminhos (mais lento)", font_size=28)
            ).arrange(RIGHT, buff=0.5),
            VGroup(
                Text("Busca Gulosa:", font_size=36, color=RED, weight=BOLD),
                Text("Só usa h(n), pode não ser ótimo", font_size=28)
            ).arrange(RIGHT, buff=0.5),
            VGroup(
                Text("A*:", font_size=36, color=GREEN, weight=BOLD),
                Text("Equilibra g(n) e h(n) - rápido e ótimo!", font_size=28)
            ).arrange(RIGHT, buff=0.5),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.7)
        comparison.shift(DOWN * 0.3)
        
        for comp in comparison:
            self.play(FadeIn(comp, shift=UP), run_time=0.9)
            self.wait(2.5)
        
        self.wait(3)
        self.play(FadeOut(comparison), FadeOut(comp_title), run_time=0.8)
        self.wait(1)

        # --- CONCLUSÃO ---
        conclusion_title = Text("Conclusão", font_size=50, color=GOLD, weight=BOLD)
        conclusion_title.to_edge(UP)
        self.play(FadeIn(conclusion_title), run_time=0.8)
        self.wait(1)
        
        conclusion_points = VGroup(
            Text("✓ A* é eficiente para busca de caminhos", font_size=34, color=GREEN),
            Text("✓ Heurística admissível garante otimalidade", font_size=34, color=BLUE),
            Text("✓ Amplamente usado em IA e jogos", font_size=34, color=YELLOW),
            Text("✓ Equilíbrio perfeito entre velocidade e precisão", font_size=34, color=ORANGE),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.6)
        conclusion_points.shift(DOWN * 0.5)
        
        for point in conclusion_points:
            self.play(FadeIn(point, shift=RIGHT), run_time=0.8)
            self.wait(2.5)
        
        self.wait(3)

        # Fade out final
        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=2)
        self.wait(2)