from manim import *
import numpy as np
from math import pi

class freq4(Scene):
    def construct(self):
        ax = Axes(
            x_range=[0, 10, 1],
            y_range=[-2, 2, 1],
            tips=False,
            axis_config={"include_numbers": True},
        )
        tracker = ValueTracker(3)
        text = Text("f: {:.2f} Hz".format(tracker.get_value(), 2), font_size=40).align_on_border(DOWN, 1).align_on_border(RIGHT, 1)
        
        # x_min must be > 0 because log is undefined at 0.
        graph = always_redraw(lambda: ax.plot(lambda x: np.cos(6*pi*x)*np.cos(2*tracker.get_value()*pi*x), x_range=[0.001, 10, 0.005], use_smoothing=False))

        

        sin_label = MathTex("cos(3\cdot2{\pi}x)cos(-f\cdot2{\pi}x)").next_to(graph, UP).align_on_border(RIGHT, 1)
        area_pos = always_redraw(lambda: ax.get_area(
            graph,
            x_range=(0, 10),
            color=color_gradient((RED, GREEN), 2),
            opacity=1,
        ))
        self.add(ax, graph, text, sin_label)