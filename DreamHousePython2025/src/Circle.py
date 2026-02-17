import tkinter as tk
from tkinter import Canvas
from Shape import Shape


class Circle(Shape):
    def __init__(self, canvas: Canvas, x: int = 20, y: int = 60, diameter: int = 30, color: str = "blue", fill: str = None, line: int = 2, tag: str = None):
        super().__init__(canvas=canvas, x=x, y=y, color=color, fill=fill, line=line)
        self.diameter = diameter

    def draw(self):
        if self.is_visible:
            print(f"Drawing circle at ({self.x_position},{self.y_position}) diameter {self.diameter} color {self.color} fill {self.fill} line {self.line}")
            self.shape_id = self.canvas.create_oval(
                self.x_position, self.y_position,
                self.x_position + self.diameter, self.y_position + self.diameter,
                outline=self.color, fill=self.fill, width=self.line
            )

    def erase(self):
        if self.is_visible:
            print("Erasing circle")
            super().erase()
