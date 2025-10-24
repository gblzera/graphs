from manim import *

class DijkstraVisualization(Scene):
    def construct(self):
        # --- TÍTULO E INTRODUÇÃO ---
        title = Text("Algoritmo de Dijkstra", font_size=70, color=YELLOW, weight=BOLD)
        subtitle = Text("Busca do Caminho Mais Curto (Sem Heurística)", font_size=35, color=GRAY)
        subtitle.next_to(title, DOWN, buff=0.3)
        title_group = VGroup(title, subtitle)
        
        self.play(Write(title, run_time=1.5), FadeIn(subtitle, shift=UP))
        self.wait(2.5)
        self.play(title_group.animate.scale(0.6).to_edge(UP), run_time=1)
        self.wait(1)

        # --- O QUE É DIJKSTRA ---
        what_title = Text("O que é o Algoritmo de Dijkstra?", font_size=50, color=TEAL, weight=BOLD)
        what_title.to_edge(UP)
        self.play(Transform(title_group, what_title))
        self.wait(0.5)
        
        what_desc = VGroup(
            Text("• Algoritmo de busca de caminho mais curto", font_size=32),
            Text("• Garante a menor distância de um nó origem a todos os outros", font_size=32),
            Text("• Usa uma fila de prioridade (Min-Heap)", font_size=32),
            Text("• Não usa heurísticas — é puramente baseado em custos reais", font_size=32),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.4)
        what_desc.shift(DOWN * 0.5)
        
        for item in what_desc:
            self.play(FadeIn(item, shift=RIGHT), run_time=0.8)
            self.wait(2)
        
        self.wait(2)
        self.play(FadeOut(what_desc), run_time=0.8)
        self.wait(1)

        # --- CONCEITO FUNDAMENTAL ---
        formula_title = Text("Ideia Central", font_size=50, color=ORANGE, weight=BOLD)
        formula_title.to_edge(UP)
        self.play(Transform(title_group, formula_title), run_time=0.8)
        self.wait(1)

        concept = VGroup(
            Text("• Mantém uma lista de distâncias mínimas (g(n))", font_size=32),
            Text("• Expande sempre o nó com a menor distância conhecida", font_size=32),
            Text("• Atualiza distâncias dos vizinhos se achar caminho melhor", font_size=32),
            Text("• Continua até visitar todos os nós ou alcançar o objetivo", font_size=32)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.4).shift(DOWN * 0.5)

        for line in concept:
            self.play(FadeIn(line, shift=RIGHT), run_time=0.8)
            self.wait(2)
        
        self.wait(2)
        self.play(FadeOut(concept), run_time=0.8)
        self.wait(1)

        # --- GRAFO DE EXEMPLO ---
        graph_title = Text("Simulação Visual de Dijkstra", font_size=50, color=TEAL, weight=BOLD)
        graph_title.to_edge(UP)
        self.play(Transform(title_group, graph_title), run_time=0.8)
        self.wait(1)

        # Definição do grafo
        vertices = ["S", "A", "B", "C", "D", "E", "G"]
        edges = [
            ("S", "A"), ("S", "B"),
            ("A", "C"), ("A", "D"),
            ("B", "D"), ("C", "E"),
            ("D", "E"), ("E", "G")
        ]
        layout = {
            "S": LEFT * 4.5 + UP * 0.5,
            "A": LEFT * 1.5 + UP * 2.5,
            "B": LEFT * 1.5 + DOWN * 1.5,
            "C": RIGHT * 1.5 + UP * 2.5,
            "D": RIGHT * 1.5 + DOWN * 1.5,
            "E": RIGHT * 4.5 + UP * 0.5,
            "G": RIGHT * 6.5
        }
        weights = {
            ("S", "A"): 2, ("S", "B"): 4,
            ("A", "C"): 3, ("A", "D"): 2,
            ("B", "D"): 3, ("C", "E"): 4,
            ("D", "E"): 1, ("E", "G"): 2
        }

        graph = Graph(
            vertices, edges, layout=layout,
            vertex_config={"radius": 0.4, "color": BLUE, "fill_opacity": 0.9},
            edge_config={"stroke_width": 4, "color": GRAY}
        ).scale(0.85)
        
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
        info_box = Rectangle(width=13, height=1.3, color=BLUE, fill_opacity=0.2)
        info_box.to_edge(UP).shift(DOWN * 0.05)
        self.play(Create(info_box), run_time=0.6)

        def show_info(text, color=WHITE):
            info = Text(text, font_size=30, color=color, weight=BOLD)
            info.move_to(info_box)
            self.play(FadeIn(info), run_time=0.6)
            self.wait(2)
            self.play(FadeOut(info), run_time=0.3)

        # Distâncias (g)
        g_labels = {}

        def add_g_label(v, g):
            label = Text(f"g={g}", font_size=20, color=WHITE, weight=BOLD)
            label.next_to(graph.vertices[v], UP, buff=0.15)
            label.add_background_rectangle(color=BLACK, opacity=0.8, buff=0.08)
            g_labels[v] = label
            self.play(FadeIn(label, scale=0.8), run_time=0.5)
        
        # Passo 1: Inicializar S
        show_info("Passo 1: Inicializar com nó S (g=0)", GREEN)
        self.play(graph.vertices["S"].animate.set_color(GREEN))
        add_g_label("S", 0)
        self.wait(1)

        # Passo 2: Expandir S
        show_info("Passo 2: Expandir S → A e B", YELLOW)
        self.play(graph.vertices["S"].animate.set_color(RED))
        self.play(graph.vertices["A"].animate.set_color(GREEN), graph.vertices["B"].animate.set_color(GREEN))
        add_g_label("A", 2)
        add_g_label("B", 4)
        self.wait(2)

        # Passo 3: Escolher menor g (A)
        show_info("A tem menor g (2) → Expandir A", BLUE)
        self.play(graph.vertices["A"].animate.set_color(RED))
        self.play(graph.vertices["C"].animate.set_color(GREEN), graph.vertices["D"].animate.set_color(GREEN))
        add_g_label("C", 5)
        add_g_label("D", 4)
        self.wait(2)

        # Passo 4: Escolher D (g=4)
        show_info("D tem menor g → Expandir D", BLUE)
        self.play(graph.vertices["D"].animate.set_color(RED))
        self.play(graph.vertices["E"].animate.set_color(GREEN))
        add_g_label("E", 5)
        self.wait(2)

        # Passo 5: Expandir E
        show_info("Expandir E → Alcançar G", GREEN)
        self.play(graph.vertices["E"].animate.set_color(RED))
        self.play(graph.vertices["G"].animate.set_color(YELLOW))
        add_g_label("G", 7)
        self.wait(2)

        # Destacar caminho ótimo
        show_info("Caminho ótimo: S → A → D → E → G", GREEN)
        optimal_path = [("S", "A"), ("A", "D"), ("D", "E"), ("E", "G")]
        for edge in optimal_path:
            self.play(graph.edges[edge].animate.set_color(GREEN).set_stroke(width=8), run_time=0.6)
            self.wait(0.8)
        self.wait(2)

        # --- RESULTADO FINAL ---
        result_box = Rectangle(width=10, height=2.5, color=GREEN, fill_color=GREEN, fill_opacity=0.25)
        result_text = Text("✓ Caminho Ótimo Encontrado!", font_size=42, color=GREEN, weight=BOLD)
        result_path = Text("S → A → D → E → G", font_size=48, color=YELLOW, weight=BOLD)
        result_cost = Text("Custo Total: 7", font_size=36, color=WHITE)

        result_group = VGroup(result_text, result_path, result_cost).arrange(DOWN, buff=0.35)
        final = VGroup(result_box, result_group)
        self.play(FadeIn(result_box, scale=0.9), run_time=0.8)
        self.play(Write(result_text), run_time=1)
        self.play(Write(result_path), run_time=1)
        self.play(Write(result_cost), run_time=1)
        self.wait(3)

        self.play(*[FadeOut(m) for m in self.mobjects], run_time=2)
        self.wait(1)

        # --- CONCLUSÃO ---
        conclusion_title = Text("Conclusão", font_size=50, color=GOLD, weight=BOLD)
        self.play(FadeIn(conclusion_title), run_time=0.8)
        conclusion_points = VGroup(
            Text("✓ Garante o menor caminho em grafos com pesos positivos", font_size=34, color=GREEN),
            Text("✓ Usa apenas custo real (g(n)) — sem heurísticas", font_size=34, color=BLUE),
            Text("✓ Base para o A* (quando somamos a heurística h(n))", font_size=34, color=YELLOW),
            Text("✓ Ideal para mapas, rotas e redes", font_size=34, color=ORANGE)
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.6)
        conclusion_points.shift(DOWN * 0.5)
        for p in conclusion_points:
            self.play(FadeIn(p, shift=RIGHT), run_time=0.8)
            self.wait(2)
        self.wait(3)
