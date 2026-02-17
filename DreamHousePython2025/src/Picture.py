import tkinter as tk
from tkinter import ttk
from Square import Square
from Triangle import Triangle
from Circle import Circle


class Picture:
    def __init__(self, root=None):
        self.root = root
        self.root.title("House Drawing Application")
        self.root.geometry("800x600")

        # Create main frame
        main_frame = ttk.Frame(root)
        main_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        # Create canvas for drawing
        self.canvas = tk.Canvas(main_frame, width=600, height=400, bg='lightblue')
        self.canvas.pack(side=tk.LEFT, padx=(0, 10))

        self.wall = None
        self.window = None
        self.roof = None
        self.sun = None

        self.draw()

    def draw(self):
        self.wall = Square(canvas=self.canvas, size=100, color="red", fill="red", line=2)
        self.wall.move_horizontal(50)
        self.wall.move_vertical(80)
        self.wall.make_visible()

        self.window = Square(canvas=self.canvas, size=30, color="black", fill="black", line=1)
        self.window.move_horizontal(70)
        self.window.move_vertical(100)
        self.window.make_visible()

        self.roof = Triangle(canvas=self.canvas, height=75, width=150, color="green", fill="green", line=2)
        self.roof.move_horizontal(35)
        self.roof.move_vertical(113)
        self.roof.make_visible()

        self.sun = Circle(canvas=self.canvas, diameter=60, color="yellow", fill="yellow", line=1)
        self.sun.move_horizontal(200)
        self.sun.move_vertical(-10)
        self.sun.make_visible()

    def set_black_and_white(self):
        if self.wall:
            self.wall.change_color("black")
            self.window.change_color("white")
            self.roof.change_color("black")
            self.sun.change_color("black")

    def set_color(self):
        if self.wall:
            self.wall.change_color("red")
            self.window.change_color("black")
            self.roof.change_color("green")
            self.sun.change_color("yellow")
