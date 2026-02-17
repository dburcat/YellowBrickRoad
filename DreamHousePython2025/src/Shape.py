import tkinter as tk
from tkinter import Canvas


class Shape:
    def __init__(self, canvas: Canvas, x: int = 60, y: int = 50, color = "black", fill = None, line = 2):
        self.canvas = canvas
        self.color = color
        self.fill = fill
        self.line = line
        self.x_position = x
        self.y_position = y
        self.is_visible = False

    def draw(self):
        pass

    def erase(self):
        if self.is_visible:
            self.canvas.delete(self.shape_id)
            self.shape_id = None
            self.is_visible = False

    def make_visible(self):
        self.is_visible = True
        self.draw()

    def make_invisible(self):
        self.is_visible = False
        self.erase()

    def change_size(self, new_size):
        self.erase()
        self.size = new_size
        self.draw()

    def change_color(self, new_color):
        self.color = new_color
        self.draw()

    def move_right(self):
        self.move_horizontal(20)

    def move_left(self):
        self.move_horizontal(-20)

    def move_up(self):
        self.move_vertical(-20)

    def move_down(self):
        self.move_vertical(20)

    def move_horizontal(self, distance):
        self.erase()
        self.x_position += distance
        self.draw()

    def move_vertical(self, distance):
        self.erase()
        self.y_position += distance
        self.draw()
