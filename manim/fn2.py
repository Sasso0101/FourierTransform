from manim import *
import numpy as np
from math import pi

class fn2(Scene):
    def construct(self):
        ax = Axes(
            x_range=[0, 1.5, 1],
            y_range=[-2, 2, 1],
            tips=False,
            y_length = 3,
            axis_config={"include_numbers": True},
        ).align_on_border(UP, 0.5)

        # x_min must be > 0 because log is undefined at 0.
        graph = ax.plot(lambda x: np.cos(6*pi*x), x_range=[0, 1.5, 0.0005], use_smoothing=False, color= RED)

        sin_label = MathTex("cos(3\cdot2{\pi}x)").next_to(graph, UP).align_on_border(RIGHT, 1)

        ax1 = Axes(
            x_range=[0, 1.5, 1],
            y_range=[-2, 2, 1],
            tips=False,
            y_length = ax.height,
            axis_config={"include_numbers": True},
        ).align_on_border(DOWN, 0.5)

        # x_min must be > 0 because log is undefined at 0.
        graph1 = ax1.plot(lambda x: np.cos(10*pi*x), x_range=[0.001, 1.5, 0.0005], use_smoothing=False, color=BLUE)

        sin_label1 = MathTex("cos(5\cdot2{\pi}x)").next_to(graph1, UP).align_on_border(RIGHT, 1)
        self.play(Create(ax), Create(ax1))
        self.play(Create(graph), Write(sin_label), Create(graph1), Write(sin_label1))
