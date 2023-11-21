from manim import *
import numpy as np
from math import pi

class fn1(Scene):
    def construct(self):
        ax = Axes(
            x_range=[0, 1.5, 1],
            y_range=[-2, 2, 1],
            tips=False,
            axis_config={"include_numbers": True},
        )

        # x_min must be > 0 because log is undefined at 0.
        graph = ax.plot(lambda x: np.cos(6*pi*x), x_range=[0.001, 1.5, 0.0005], use_smoothing=False)

        sin_label = MathTex("cos(3\cdot2{\pi}x)").next_to(graph, UP).align_on_border(RIGHT, 1)
        self.play(Create(ax))
        self.play(Create(graph), Write(sin_label))
        graph1 = ax.plot(lambda x: np.cos(6*pi*x), x_range=[0, 0.335, 0.0005], use_smoothing=False, color=RED)
        self.play(Create(graph1))
        graph2 = ax.plot(lambda x: np.cos(6*pi*x), x_range=[0.335, 0.67, 0.0005], use_smoothing=False, color=GREEN)
        self.play(Create(graph2))
        graph3 = ax.plot(lambda x: np.cos(6*pi*x), x_range=[0.67, 1, 0.0005], use_smoothing=False, color=BLUE)
        self.play(Create(graph3))