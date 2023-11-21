from manim import *
import numpy as np
from math import pi

class fn3(Scene):
    def construct(self):
        ax = Axes(
            x_range=[0, 1.5, 1],
            y_range=[-2, 2, 1],
            tips=False,
            axis_config={"include_numbers": True},
        )

        # x_min must be > 0 because log is undefined at 0.
        graph = ax.plot(lambda x: np.cos(6*pi*x)+np.cos(10*pi*x), x_range=[0.001, 1.5, 0.0005], use_smoothing=False, stroke_color= (BLUE, RED))

        sin_label = MathTex("cos(3\cdot2{\pi}x)+cos(5\cdot2{\pi}x)").next_to(graph, UP).align_on_border(RIGHT, 1)
        self.play(Create(ax))
        self.play(Create(graph), Write(sin_label))