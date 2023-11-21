from manim import *
import numpy as np
from math import pi
import builtins

class frequencies(Scene):
    def construct(self):
        width = ValueTracker(1.5)

        def always_redraw_axes(axes_maker_func):
            mob = axes_maker_func()
        
            def become_ax(m):
                old_ax = mob
                new_ax = make_ax()
                old_ax.become(new_ax)
                old_ax.x_axis.x_range = new_ax.x_axis.x_range
                old_ax.x_axis.scaling = new_ax.x_axis.scaling
                old_ax.y_axis.x_range = new_ax.y_axis.x_range
                old_ax.y_axis.scaling = new_ax.y_axis.scaling
            mob.add_updater(become_ax)
            return mob
        def make_ax():
            return Axes(
                x_range=[0, width.get_value(), 1],
                y_range=[-2, 2, 1],
                tips=False,
                axis_config={"include_numbers": True},
            )
        ax = always_redraw_axes(make_ax)
        
        # x_min must be > 0 because log is undefined at 0.
        graph_old = ax.plot(lambda x: np.cos(6*pi*x), x_range=[0, 1.5, 0.005], use_smoothing=False)

        sin_label = MathTex("cos(3\cdot2{\pi}x)").next_to(graph_old, UP).align_on_border(RIGHT, 1)
        self.play(Create(ax))
        self.play(Create(graph_old), Write(sin_label))
        self.next_section()
        tracker = ValueTracker(6)
        graph = always_redraw(lambda: ax.plot(lambda x: np.cos(6*pi*x)*np.cos(-2*tracker.get_value()*pi*x), x_range=[0, width.get_value(), 0.005], use_smoothing=False))

        sin_label_new = MathTex("cos(3\cdot2{\pi}x)cos(-f\cdot2{\pi}x)").next_to(graph, UP).align_on_border(RIGHT, 1)
        text = always_redraw(lambda: Text("f: {:.2f} Hz".format(tracker.get_value(), 2), font_size=40).align_on_border(DOWN, 1).align_on_border(RIGHT, 1))
        self.play(Transform(sin_label, sin_label_new), Transform(graph_old, graph, replace_mobject_with_target_in_scene=True), Write(text))

        self.next_section()

        graph_pos = always_redraw(
            lambda: ax.plot(lambda x: max(0, np.cos(6*pi*x)*np.cos(-2*tracker.get_value()*pi*x)),
            x_range=[0, width.get_value(), 0.005],
            use_smoothing=False)
        )
        graph_neg = always_redraw(
            lambda: ax.plot(lambda x: min(0, np.cos(6*pi*x)*np.cos(-2*tracker.get_value()*pi*x)), 
            x_range=[0, width.get_value(), 0.005], 
            use_smoothing=False)
        )

        area_pos = always_redraw(lambda: ax.get_area(
            graph_pos,
            x_range=(0, width.get_value()),
            color=GREEN,
            opacity=1,
        ))
        area_neg = always_redraw(lambda: ax.get_area(
            graph_neg,
            x_range=(0, width.get_value()),
            color=RED,
            opacity=1,
        ))
        self.replace(graph, graph_pos)
        self.add(graph_neg)

        integral = always_redraw(lambda: MathTex("\int_{-\infty}^{+\infty}", "cos(3\cdot2{{\pi}}x)cos(-{:.2f}\cdot2{{\pi}}x)".format(tracker.get_value(), 2), "dt=", "0").align_on_border(LEFT, 2).align_on_border(DOWN, 1.2))
        self.play(FadeIn(area_pos), FadeIn(area_neg), FadeIn(integral))

        self.next_section()
        self.play(tracker.animate(run_time=10).set_value(4))

        self.next_section()
        self.play(tracker.animate(run_time=8).set_value(3))
        self.next_section()
        integral_new = MathTex("\int_{-\infty}^{+\infty}", "cos^2(3\cdot2{\pi}x)", "dt=", "+\infty").align_on_border(LEFT, 2).align_on_border(DOWN, 1.2)
        self.play(TransformMatchingTex(integral, integral_new))
