from manim import *
import numpy as np
from math import pi

class transform1(Scene):
    def construct(self):
        ax = Axes(
            x_range=[0, 1.5, 1],
            y_range=[-2, 2, 1],
            tips=True,
            y_length=2,
            axis_config={"include_numbers": True},
        ).align_on_border(UP, 1)
        label = ax.get_x_axis_label("t [s]").next_to(ax, RIGHT, 0, UP)

        # x_min must be > 0 because log is undefined at 0.
        graph = ax.plot(lambda x: np.cos(6*pi*x)+np.cos(10*pi*x), x_range=[0.001, 1.5, 0.0005], use_smoothing=False, stroke_color= (BLUE, RED))

        sin_label = MathTex("cos(3\cdot2{\pi}x)+cos(5\cdot2{\pi}x)").next_to(graph, UP).align_on_border(RIGHT, 1)

        ax1 = Axes(
            x_range=[0, 6, 1],
            y_range=[0, 5, 1],
            y_length=2,
            tips=True,
            axis_config={"include_numbers": True},
        ).align_on_border(DOWN, 1)
        label1 = ax1.get_x_axis_label("f [Hz]").next_to(ax1, RIGHT, 0, RIGHT)

        # x_min must be > 0 because log is undefined at 0.
        dirac = Arrow(start=ax1.c2p(3,0), end=ax1.c2p(3,5), buff=0)
        dirac1 = Arrow(start=ax1.c2p(5,0), end=ax1.c2p(5,5), buff=0)

        to = Arrow(start=ax.get_edge_center(DOWN), end=np.array((ax.get_x(), -0.3, 0)), buff=0)
        myTemplate = TexTemplate()
        myTemplate.add_to_preamble(r"\usepackage{amssymb}")
        f = MathTex("\mathcal{F}(\cdot)",
            tex_template=myTemplate).next_to(to, RIGHT)
        
        self.play(Create(ax), FadeIn(sin_label), FadeIn(label))
        self.play(Create(graph))
        self.play(Create(ax1), FadeIn(label1))
        self.play(Write(dirac), Write(dirac1))
        self.play(Create(to), Write(f))