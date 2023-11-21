from manim import *
import numpy as np
from math import pi, exp

class transform2(Scene):
    def construct(self):
        ax = Axes(
            x_range=[-2, 2, 1],
            y_range=[-2, 2, 1],
            tips=True,
            y_length=3,
            axis_config={"include_numbers": True},
        ).align_on_border(UP, 0.5)
        label = ax.get_x_axis_label("t [s]").next_to(ax, RIGHT, 0, UP)

        # x_min must be > 0 because log is undefined at 0.
        graph = ax.plot(lambda x: exp(-pi*x**2)*np.cos(6*pi*x), x_range=[-2, 2, 0.0005], use_smoothing=False, stroke_color= (BLUE, RED))

        ax1 = Axes(
            x_range=[0, 6, 1],
            y_range=[0, 1, 0.2],
            y_length=3,
            tips=True,
            axis_config={"include_numbers": True},
        ).align_on_border(DOWN, 0.5)
        label3 = ax1.get_x_axis_label("f [Hz]").next_to(ax1, RIGHT, 0, RIGHT)
        graph1 = ax1.plot(lambda x: (1/2)*exp(-((2*pi*x+6*pi)**2)/(4*pi))*(exp(12*pi*x)+1), x_range=[0, 6, 0.0005], use_smoothing=False, stroke_color= (BLUE, RED))

        to = Arrow(
            start=np.array((ax.get_center()[0], ax.get_edge_center(DOWN)[1]-0.2, 0)),
            end=np.array((ax.get_x(), -0.7, 0)), buff=0)
        myTemplate = TexTemplate()
        myTemplate.add_to_preamble(r"\usepackage{amssymb}")
        f = MathTex("\mathcal{F}(\cdot)",
            tex_template=myTemplate).next_to(to, RIGHT)
        
        self.play(Create(ax), FadeIn(label))
        self.play(Create(graph))
        self.play(Create(ax1), FadeIn(label3))
        self.play(Write(graph1))
        self.play(Create(to), Write(f))