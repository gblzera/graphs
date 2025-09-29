from manim import *

class DFSComplete(Scene):
    def construct(self):
        # --- TÍTULO PRINCIPAL COM ANIMAÇÃO ---
        title = Text("Busca em Profundidade", font_size=70, color=YELLOW, weight=BOLD)
        subtitle = Text("Depth-First Search (DFS)", font_size=35, color=GRAY).next_to(title, DOWN)
        title_group = VGroup(title, subtitle)
        
        self.play(Write(title, run_time=1.5), FadeIn(subtitle, shift=UP))
        self.wait(1)
        self.play(title_group.animate.scale(0.7).to_edge(UP))
        self.wait(0.5)

        # --- INTRODUÇÃO COM ÍCONES ---
        intro_title = Text("Características Principais", font_size=45, color=BLUE).to_edge(UP)
        self.play(Transform(title_group, intro_title))
        
        intro_items = [
            ("🎯", "Explora profundamente antes de retornar"),
            ("🔄", "Usa backtracking ao encontrar becos sem saída"),
            ("📚", "Implementação: Recursiva ou com Pilha"),
            ("⚡", "Complexidade: O(V + E)"),
            ("🎲", "Aplicações: Labirintos, ciclos, componentes")
        ]
        
        intro_group = VGroup()
        for icon, text in intro_items:
            item = VGroup(
                Text(icon, font_size=35),
                Text(text, font_size=28).set_color(WHITE)
            ).arrange(RIGHT, buff=0.3)
            intro_group.add(item)
        
        intro_group.arrange(DOWN, aligned_edge=LEFT, buff=0.4).shift(DOWN*0.5)
        
        for item in intro_group:
            self.play(FadeIn(item, shift=RIGHT), run_time=0.6)
            self.wait(0.3)
        
        self.wait(2)
        self.play(FadeOut(intro_group))

        # --- COMPARAÇÃO BFS vs DFS COM VISUALIZAÇÃO ---
        comp_title = Text("DFS vs BFS", font_size=50, color=PURPLE).to_edge(UP)
        self.play(Transform(title_group, comp_title))
        
        # Duas árvores lado a lado
        left_label = Text("BFS (Largura)", font_size=32, color=BLUE).shift(LEFT*3 + UP*2)
        right_label = Text("DFS (Profundidade)", font_size=32, color=RED).shift(RIGHT*3 + UP*2)
        
        bfs_desc = Text("Nível por nível →", font_size=24, color=GRAY).next_to(left_label, DOWN)
        dfs_desc = Text("Ramo completo ↓", font_size=24, color=GRAY).next_to(right_label, DOWN)
        
        self.play(
            Write(left_label), Write(right_label),
            FadeIn(bfs_desc), FadeIn(dfs_desc)
        )
        self.wait(2)
        self.play(FadeOut(left_label, right_label, bfs_desc, dfs_desc))

        # --- PSEUDOCÓDIGO RECURSIVO ---
        pseudo_title = Text("Pseudocódigo Recursivo", font_size=48, color=GREEN).to_edge(UP)
        self.play(Transform(title_group, pseudo_title))
        
        code_lines = [
            ("DFS(grafo G, vértice s):", WHITE),
            ("  marcar s como VISITADO", YELLOW),
            ("  para cada vizinho v de s:", WHITE),
            ("    se v NÃO foi visitado:", BLUE),
            ("      DFS(G, v)  // Recursão", RED),
        ]
        
        code_group = VGroup()
        for line, color in code_lines:
            code_group.add(Text(line, font="Consolas", font_size=30, color=color))
        code_group.arrange(DOWN, aligned_edge=LEFT, buff=0.3).shift(UP*0.5)
        
        for line in code_group:
            self.play(AddTextLetterByLetter(line, run_time=0.8))
            self.wait(0.3)
        
        self.wait(2)
        self.play(FadeOut(code_group))

        # --- PSEUDOCÓDIGO ITERATIVO ---
        pseudo_iter_title = Text("Pseudocódigo Iterativo (Pilha)", font_size=48, color=ORANGE).to_edge(UP)
        self.play(Transform(title_group, pseudo_iter_title))
        
        iter_code_lines = [
            ("DFS_Iterativo(grafo G, vértice s):", WHITE),
            ("  pilha = [s]", YELLOW),
            ("  enquanto pilha não vazia:", WHITE),
            ("    v = pilha.pop()", BLUE),
            ("    se v não visitado:", WHITE),
            ("      marcar v como VISITADO", YELLOW),
            ("      adicionar vizinhos à pilha", GREEN),
        ]
        
        iter_code_group = VGroup()
        for line, color in iter_code_lines:
            iter_code_group.add(Text(line, font="Consolas", font_size=28, color=color))
        iter_code_group.arrange(DOWN, aligned_edge=LEFT, buff=0.25).shift(UP*0.3)
        
        for line in iter_code_group:
            self.play(AddTextLetterByLetter(line, run_time=0.7))
            self.wait(0.2)
        
        self.wait(2)
        self.play(FadeOut(iter_code_group))

        # --- EXECUÇÃO VISUAL PRINCIPAL ---
        exec_title = Text("Simulação Visual", font_size=50, color=TEAL).to_edge(UP)
        self.play(Transform(title_group, exec_title))
        
        # Definição do grafo (mais complexo)
        vertices = ["A", "B", "C", "D", "E", "F"]
        edges = [
            ("A", "B"), ("A", "C"), ("B", "D"), 
            ("B", "E"), ("C", "F"), ("D", "E")
        ]
        
        layout = {
            "A": UP*2,
            "B": LEFT*2.5 + DOWN*0.5,
            "C": RIGHT*2.5 + DOWN*0.5,
            "D": LEFT*2.5 + DOWN*2.5,
            "E": DOWN*2.5,
            "F": RIGHT*2.5 + DOWN*2.5,
        }
        
        graph = Graph(
            vertices, edges, layout=layout,
            vertex_config={"radius": 0.35, "color": BLUE, "fill_opacity": 0.8},
            edge_config={"stroke_width": 4, "color": GRAY}
        ).scale(0.8).shift(LEFT*1.5)
        
        # Labels nos vértices
        vertex_labels = {}
        for v in vertices:
            label = Text(v, font_size=28, color=WHITE, weight=BOLD)
            label.move_to(graph.vertices[v])
            vertex_labels[v] = label
        
        self.play(Create(graph), *[Write(label) for label in vertex_labels.values()])
        self.wait(1)

        # --- PILHA VISUAL ---
        stack_title = Text("Pilha", font_size=38, color=ORANGE, weight=BOLD).to_edge(RIGHT).shift(UP*2.5)
        self.play(Write(stack_title))
        
        stack_container = Rectangle(
            width=2.2, height=5, 
            color=WHITE, stroke_width=3
        ).next_to(stack_title, DOWN, buff=0.3)
        self.play(Create(stack_container))
        
        # Legenda de visitados
        legend = VGroup(
            VGroup(Circle(radius=0.15, color=BLUE, fill_opacity=0.8), Text("Não visitado", font_size=20)).arrange(RIGHT, buff=0.2),
            VGroup(Circle(radius=0.15, color=YELLOW, fill_opacity=0.8), Text("Processando", font_size=20)).arrange(RIGHT, buff=0.2),
            VGroup(Circle(radius=0.15, color=RED, fill_opacity=0.8), Text("Visitado", font_size=20)).arrange(RIGHT, buff=0.2),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.2).scale(0.8).to_edge(DOWN).shift(RIGHT*2.5)
        
        self.play(FadeIn(legend, shift=UP))
        
        stack_elements = []
        
        def push_stack(node):
            txt = Text(node, font_size=32, color=BLACK, weight=BOLD)
            rect = Rectangle(
                width=1.8, height=0.65, 
                color=ORANGE, fill_color=ORANGE, fill_opacity=0.9,
                stroke_width=2
            )
            g = VGroup(rect, txt)
            
            if stack_elements:
                g.next_to(stack_elements[-1], UP, buff=0.05)
            else:
                g.next_to(stack_container.get_bottom(), UP, buff=0.1)
            
            stack_elements.append(g)
            self.play(FadeIn(g, shift=UP, scale=0.5), run_time=0.5)
            self.wait(0.2)
        
        def pop_stack():
            if stack_elements:
                g = stack_elements.pop()
                self.play(FadeOut(g, shift=DOWN, scale=1.5), run_time=0.5)
                # Reorganizar pilha
                for i, elem in enumerate(stack_elements):
                    if i == 0:
                        target_pos = stack_container.get_bottom() + UP*0.475
                    else:
                        target_pos = stack_elements[i-1].get_center() + UP*0.7
                    self.play(elem.animate.move_to(target_pos), run_time=0.3)
                self.wait(0.2)
        
        # Contador de ordem
        order_counter = VGroup()
        order_num = 1
        
        # --- SIMULAÇÃO DFS ITERATIVA ---
        visited = set()
        stack = []
        
        start = "A"
        push_stack(start)
        stack.append(start)
        
        while stack:
            current = stack.pop()
            pop_stack()
            
            if current not in visited:
                # Destacar processamento
                self.play(
                    graph.vertices[current].animate.set_color(YELLOW),
                    vertex_labels[current].animate.set_color(BLACK),
                    run_time=0.5
                )
                self.wait(0.3)
                
                visited.add(current)
                
                # Marcar como visitado
                self.play(
                    graph.vertices[current].animate.set_color(RED),
                    vertex_labels[current].animate.set_color(WHITE),
                    run_time=0.5
                )
                
                # Adicionar número de ordem
                order_label = Text(str(order_num), font_size=18, color=YELLOW, weight=BOLD)
                order_label.next_to(graph.vertices[current], UP+RIGHT, buff=0.05)
                order_counter.add(order_label)
                self.play(FadeIn(order_label, scale=2), run_time=0.3)
                order_num += 1
                
                # Destacar arestas exploradas
                neighbors = list(graph._graph.neighbors(current))
                for neighbor in sorted(neighbors, reverse=True):
                    # Tentar ambas as direções da aresta
                    try:
                        edge = graph.edges[(current, neighbor)]
                    except KeyError:
                        edge = graph.edges[(neighbor, current)]
                    
                    if neighbor not in visited:
                        self.play(edge.animate.set_color(YELLOW), run_time=0.3)
                        push_stack(neighbor)
                        stack.append(neighbor)
                    else:
                        self.play(edge.animate.set_color(GREEN).set_stroke(width=2), run_time=0.2)
                
                self.wait(0.4)

        self.wait(1)
        
        # --- FINALIZAÇÃO ---
        end_box = Rectangle(width=10, height=1.5, color=GREEN, fill_color=GREEN, fill_opacity=0.7)
        end_text = Text("DFS Completo!", font_size=48, color=GREEN, weight=BOLD)
        end_detail = Text(f"Ordem de visitação: {' → '.join(['A', 'B', 'D', 'E', 'C', 'F'])}", 
                         font_size=28, color=WHITE)
        end_group = VGroup(end_text, end_detail).arrange(DOWN, buff=0.3)
        end_final = VGroup(end_box, end_group)
        
        self.play(
            FadeIn(end_box, scale=0.8),
            Write(end_text),
            run_time=1
        )
        self.wait(0.5)
        self.play(Write(end_detail))
        self.wait(3)
        
        # Fade out final
        self.play(
            *[FadeOut(mob) for mob in self.mobjects],
            run_time=1.5
        )
        self.wait(1)