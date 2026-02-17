import tkinter as tk
from tkinter import Canvas
from Shape import Shape


class Triangle(Shape):
    def __init__(self, canvas: Canvas, x: int = 50, y: int = 15, height: int = 30, width: int = 40, color: str = "green", fill: str = None, line: int = 2):
        super().__init__(canvas=canvas, x=x, y=y, color=color, fill=fill, line=line)
        self.height = height
        self.width = width

    def draw(self):
        if self.is_visible:
            print(f"Drawing triangle at ({self.x_position},{self.y_position}) size ({self.height},{self.width}) color {self.color} fill {self.fill} line {self.line}")
            self.shape_id = self.canvas.create_polygon(
                self.x_position, self.y_position,
                self.x_position + self.width / 2, self.y_position - self.height,
                self.x_position + self.width, self.y_position,
                outline=self.color, fill=self.fill, width=self.line
            )

    def erase(self):
        if self.is_visible:
            print("Erasing triangle")
            super().erase()
