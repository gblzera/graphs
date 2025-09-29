from manim import *

class BFSComplete(Scene):
    def construct(self):
        # --- TÍTULO PRINCIPAL COM ANIMAÇÃO ---
        title = Text("Busca em Largura", font_size=70, color=BLUE, weight=BOLD)
        subtitle = Text("Breadth-First Search (BFS)", font_size=35, color=GRAY).next_to(title, DOWN)
        title_group = VGroup(title, subtitle)
        
        self.play(Write(title, run_time=1.5), FadeIn(subtitle, shift=UP))
        self.wait(1)
        self.play(title_group.animate.scale(0.7).to_edge(UP))
        self.wait(0.5)

        # --- INTRODUÇÃO COM ÍCONES ---
        intro_title = Text("Características Principais", font_size=45, color=TEAL).to_edge(UP)
        self.play(Transform(title_group, intro_title))
        
        intro_items = [
            ("🎯", "Explora nível por nível sistematicamente"),
            ("↔️", "Visita todos os vizinhos antes de aprofundar"),
            ("📋", "Implementação: Sempre usa Fila (Queue)"),
            ("⚡", "Complexidade: O(V + E)"),
            ("🎲", "Aplicações: Menor caminho, níveis, conexões")
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

        # --- COMPARAÇÃO DFS vs BFS ---
        comp_title = Text("BFS vs DFS - Diferenças", font_size=48, color=PURPLE).to_edge(UP)
        self.play(Transform(title_group, comp_title))
        
        comparison = VGroup(
            VGroup(
                Text("BFS", font_size=36, color=BLUE, weight=BOLD),
                Text("• Usa Fila (FIFO)", font_size=24),
                Text("• Explora por níveis", font_size=24),
                Text("• Encontra menor caminho", font_size=24),
                Text("• Mais memória", font_size=24),
            ).arrange(DOWN, aligned_edge=LEFT, buff=0.3),
            VGroup(
                Text("DFS", font_size=36, color=RED, weight=BOLD),
                Text("• Usa Pilha (LIFO)", font_size=24),
                Text("• Explora profundamente", font_size=24),
                Text("• Não garante menor caminho", font_size=24),
                Text("• Menos memória", font_size=24),
            ).arrange(DOWN, aligned_edge=LEFT, buff=0.3)
        ).arrange(RIGHT, buff=2, aligned_edge=UP)
        
        self.play(FadeIn(comparison, shift=UP))
        self.wait(3)
        self.play(FadeOut(comparison))

        # --- PSEUDOCÓDIGO ---
        pseudo_title = Text("Pseudocódigo do BFS", font_size=48, color=GREEN).to_edge(UP)
        self.play(Transform(title_group, pseudo_title))
        
        code_lines = [
            ("BFS(grafo G, vértice s):", WHITE),
            ("  fila = [s]", YELLOW),
            ("  marcar s como VISITADO", YELLOW),
            ("  enquanto fila não vazia:", WHITE),
            ("    v = fila.dequeue()  // Remove do início", BLUE),
            ("    para cada vizinho w de v:", WHITE),
            ("      se w não visitado:", WHITE),
            ("        marcar w como VISITADO", YELLOW),
            ("        fila.enqueue(w)  // Adiciona no fim", GREEN),
        ]
        
        code_group = VGroup()
        for line, color in code_lines:
            code_group.add(Text(line, font="Consolas", font_size=26, color=color))
        code_group.arrange(DOWN, aligned_edge=LEFT, buff=0.2).shift(UP*0.2)
        
        for line in code_group:
            self.play(AddTextLetterByLetter(line, run_time=0.7))
            self.wait(0.2)
        
        self.wait(2)
        self.play(FadeOut(code_group))

        # --- DEMONSTRAÇÃO VISUAL DE FILA ---
        queue_demo_title = Text("Como Funciona a Fila (FIFO)", font_size=46, color=ORANGE).to_edge(UP)
        self.play(Transform(title_group, queue_demo_title))
        
        queue_label = Text("First In, First Out", font_size=32, color=GRAY).shift(UP*2)
        self.play(Write(queue_label))
        
        # Desenhar fila visual
        queue_box = Rectangle(width=10, height=1.5, color=WHITE)
        entrada = Text("← Entrada", font_size=24, color=GREEN).next_to(queue_box, RIGHT)
        saida = Text("Saída →", font_size=24, color=RED).next_to(queue_box, LEFT)
        
        self.play(Create(queue_box), Write(entrada), Write(saida))
        
        # Simular enqueue/dequeue
        demo_items = []
        for i, letter in enumerate(['A', 'B', 'C']):
            item = Text(letter, font_size=32, color=BLACK)
            rect = Rectangle(width=0.8, height=1.2, color=BLUE, fill_color=BLUE, fill_opacity=0.8)
            g = VGroup(rect, item)
            g.move_to(queue_box.get_right() + LEFT*(0.5 + i*1))
            demo_items.append(g)
            self.play(FadeIn(g, shift=LEFT), run_time=0.5)
            self.wait(0.3)
        
        self.wait(1)
        self.play(FadeOut(demo_items[0], shift=LEFT), run_time=0.5)
        self.wait(1)
        
        self.play(
            FadeOut(queue_box, entrada, saida, queue_label, *demo_items[1:])
        )

        # --- EXECUÇÃO VISUAL PRINCIPAL ---
        exec_title = Text("Simulação Visual do BFS", font_size=48, color=TEAL).to_edge(UP)
        self.play(Transform(title_group, exec_title))
        
        # Definição do grafo
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

        # --- FILA VISUAL ---
        queue_title = Text("Fila", font_size=38, color=ORANGE, weight=BOLD).to_edge(RIGHT).shift(UP*2.5)
        self.play(Write(queue_title))
        
        queue_container = Rectangle(
            width=2.2, height=5, 
            color=WHITE, stroke_width=3
        ).next_to(queue_title, DOWN, buff=0.3)
        self.play(Create(queue_container))
        
        # Setas indicando entrada e saída
        entrada_arrow = Arrow(
            start=queue_container.get_bottom() + DOWN*0.3,
            end=queue_container.get_bottom(),
            color=GREEN, buff=0
        )
        entrada_label = Text("IN", font_size=20, color=GREEN).next_to(entrada_arrow, DOWN, buff=0.1)
        
        saida_arrow = Arrow(
            start=queue_container.get_top(),
            end=queue_container.get_top() + UP*0.3,
            color=RED, buff=0
        )
        saida_label = Text("OUT", font_size=20, color=RED).next_to(saida_arrow, UP, buff=0.1)
        
        self.play(
            Create(entrada_arrow), Write(entrada_label),
            Create(saida_arrow), Write(saida_label)
        )
        
        # Legenda de visitados
        legend = VGroup(
            VGroup(Circle(radius=0.15, color=BLUE, fill_opacity=0.8), Text("Não visitado", font_size=20)).arrange(RIGHT, buff=0.2),
            VGroup(Circle(radius=0.15, color=YELLOW, fill_opacity=0.8), Text("Na fila", font_size=20)).arrange(RIGHT, buff=0.2),
            VGroup(Circle(radius=0.15, color=GREEN, fill_opacity=0.8), Text("Processando", font_size=20)).arrange(RIGHT, buff=0.2),
            VGroup(Circle(radius=0.15, color=RED, fill_opacity=0.8), Text("Visitado", font_size=20)).arrange(RIGHT, buff=0.2),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.2).scale(0.75).to_edge(DOWN).shift(RIGHT*2.5)
        
        self.play(FadeIn(legend, shift=UP))
        
        queue_elements = []
        
        def enqueue(node):
            txt = Text(node, font_size=32, color=BLACK, weight=BOLD)
            rect = Rectangle(
                width=1.8, height=0.65, 
                color=ORANGE, fill_color=ORANGE, fill_opacity=0.9,
                stroke_width=2
            )
            g = VGroup(rect, txt)
            
            if queue_elements:
                g.next_to(queue_elements[-1], DOWN, buff=0.05)
            else:
                g.next_to(queue_container.get_top(), DOWN, buff=0.1)
            
            queue_elements.append(g)
            self.play(FadeIn(g, shift=DOWN, scale=0.5), run_time=0.5)
            self.wait(0.2)
        
        def dequeue():
            if queue_elements:
                g = queue_elements.pop(0)
                self.play(FadeOut(g, shift=UP, scale=1.5), run_time=0.5)
                # Reorganizar fila (todos sobem)
                for i, elem in enumerate(queue_elements):
                    if i == 0:
                        target_pos = queue_container.get_top() + DOWN*0.475
                    else:
                        target_pos = queue_elements[i-1].get_center() + DOWN*0.7
                    self.play(elem.animate.move_to(target_pos), run_time=0.3)
                self.wait(0.2)
                return g
        
        # Contador de ordem e nível
        order_counter = VGroup()
        level_counter = VGroup()
        order_num = 1
        
        # --- SIMULAÇÃO BFS ---
        from collections import deque
        
        visited = set()
        queue = deque()
        levels = {}
        
        start = "A"
        queue.append(start)
        visited.add(start)
        levels[start] = 0
        
        # Marcar início como na fila
        self.play(
            graph.vertices[start].animate.set_color(YELLOW),
            vertex_labels[start].animate.set_color(BLACK),
            run_time=0.5
        )
        enqueue(start)
        
        while queue:
            current = queue.popleft()
            dequeue()
            
            # Destacar processamento
            self.play(
                graph.vertices[current].animate.set_color(GREEN),
                vertex_labels[current].animate.set_color(BLACK),
                run_time=0.5
            )
            self.wait(0.3)
            
            # Marcar como completamente visitado
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
            
            # Adicionar nível
            level_label = Text(f"N{levels[current]}", font_size=16, color=TEAL, weight=BOLD)
            level_label.next_to(graph.vertices[current], DOWN+LEFT, buff=0.05)
            level_counter.add(level_label)
            self.play(FadeIn(level_label, scale=1.5), run_time=0.3)
            
            order_num += 1
            
            # Explorar vizinhos
            neighbors = sorted(list(graph._graph.neighbors(current)))
            for neighbor in neighbors:
                # Tentar ambas as direções da aresta
                try:
                    edge = graph.edges[(current, neighbor)]
                except KeyError:
                    edge = graph.edges[(neighbor, current)]
                
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)
                    levels[neighbor] = levels[current] + 1
                    
                    # Destacar aresta e adicionar à fila
                    self.play(edge.animate.set_color(YELLOW), run_time=0.3)
                    self.play(
                        graph.vertices[neighbor].animate.set_color(YELLOW),
                        vertex_labels[neighbor].animate.set_color(BLACK),
                        run_time=0.4
                    )
                    enqueue(neighbor)
                else:
                    # Aresta já explorada
                    self.play(edge.animate.set_color(GREEN).set_stroke(width=2), run_time=0.2)
            
            self.wait(0.4)

        self.wait(1)
        
        # --- ANÁLISE DE NÍVEIS ---
        level_title = Text("Níveis de Distância", font_size=40, color=TEAL).to_edge(UP)
        self.play(Transform(title_group, level_title))
        
        level_info = VGroup(
            Text("Nível 0: A", font_size=28, color=TEAL),
            Text("Nível 1: B, C", font_size=28, color=TEAL),
            Text("Nível 2: D, E, F", font_size=28, color=TEAL),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.3).to_edge(LEFT).shift(DOWN*0.5)
        
        self.play(Write(level_info))
        self.wait(2)
        self.play(FadeOut(level_info))
        
        # --- FINALIZAÇÃO ---
        end_box = Rectangle(width=10, height=2, color=GREEN, fill_color=GREEN, fill_opacity=0.3)
        end_text = Text("BFS Completo!", font_size=48, color=GREEN, weight=BOLD)
        end_detail = Text("Ordem de visitação: A → B → C → D → E → F", 
                         font_size=28, color=WHITE)
        end_benefit = Text("Garantia: Menor caminho em grafos não ponderados", 
                          font_size=22, color=YELLOW)
        end_group = VGroup(end_text, end_detail, end_benefit).arrange(DOWN, buff=0.3)
        end_final = VGroup(end_box, end_group)
        
        self.play(
            FadeIn(end_box, scale=0.8),
            Write(end_text),
            run_time=1
        )
        self.wait(0.5)
        self.play(Write(end_detail))
        self.wait(0.5)
        self.play(Write(end_benefit))
        self.wait(3)
        
        # Fade out final
        self.play(
            *[FadeOut(mob) for mob in self.mobjects],
            run_time=1.5
        )
        self.wait(1)