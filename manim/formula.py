from manim import *
import numpy as np
from math import pi

class formula(Scene):
    def construct(self):
        x_contrib = MathTex("X_x(f)=\int_{-\infty}^{+\infty}x(t)cos(-2{\pi}ft)dt")
        y_contrib = MathTex("X_y(f)=\int_{-\infty}^{+\infty}x(t)sin(-2{\pi}ft)dt")
        g = VGroup(x_contrib)
        g.arrange(DOWN)
        self.play(Write(g))
        x_old = x_contrib.copy()
        g.add(y_contrib)
        self.play(g.animate.arrange(DOWN))
        self.next_section()
        final = MathTex("X(f)=\int_{-\infty}^{+\infty}x(t)e^{-2{\pi}ift}dt")
        self.play(ReplacementTransform(x_contrib,final), ReplacementTransform(y_contrib, final))
