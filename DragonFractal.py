from turtle import width
from manim import *

class Pruebas(MovingCameraScene):
    def construct(self):
        
        colors = [PURPLE, BLUE, DARK_BLUE, GREEN_B, ORANGE, RED]

        self.camera.frame.save_state()

        def rotating_point(r):
            
            return [r[0] + r[1], r[1] - r[0], 0]  #function that returns the rotation point for next iteration

        r_point = [0, 1, 0]
        
        start = Line(ORIGIN, r_point, color=colors[0],stroke_width=13)

        self.play(
            Create(start),
            self.camera.frame.animate.set(height=start.get_height() * 2).move_to(start.get_center())
        )

        line = start.copy()

        self.add(line)

        self.play(line.animate.set_color(colors[1]))
        self.play(Rotate(line, PI/2, about_point=r_point))

        self.wait(0.3)

        for i in range(2,14):

            start = VGroup(start, line).copy()
            line = start.copy()

            r_point = rotating_point(r_point)

            #zoom
            z_center = VGroup(start.copy(), line.copy().rotate(PI/2, about_point=r_point)).get_center()
            z_width = VGroup(start.copy(), line.copy().rotate(PI/2, about_point=r_point)).get_width()
            z_height = VGroup(start.copy(), line.copy().rotate(PI/2, about_point=r_point)).get_height()

            self.add(line)

            self.play(line.animate.set_color(colors[i%6]))

            if z_width >= z_height:
                self.play(
                    Rotate(line, PI/2, about_point=r_point),
                    self.camera.frame.animate.move_to(z_center).set_width(z_width*2)
                )
            
            else:
                self.play(
                    Rotate(line, PI/2, about_point=r_point),
                    self.camera.frame.animate.move_to(z_center).set_width(z_height*2)
                )

            self.wait(0.4)

        self.wait(2)