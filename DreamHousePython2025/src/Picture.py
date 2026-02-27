import tkinter as tk
from tkinter import ttk
from Square import Square
from Triangle import Triangle
from Circle import Circle
from Rectangle import Rectangle


class Picture:
    def __init__(self, root=None):
        self.root = root
        self.root.title("House Drawing Application")
        self.root.geometry("800x600")

        # Create main frame
        main_frame = ttk.Frame(root)
        main_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        # Create canvas for drawing
        self.canvas = tk.Canvas(main_frame, width=600, height=600, bg='black')
        self.canvas.pack(side=tk.LEFT, padx=(0, 10))

        self.wall = None
        self.window = None
        self.roof = None
        self.sun = None

        self.draw()

    def draw(self):
        
        for i in range(10):
            self.smoke = Circle(canvas=self.canvas, diameter=20, color="grey68", fill="grey68", line=1)
            self.smoke.move_horizontal(290 + i * 5)
            self.smoke.move_vertical(55 - i * 10)
            self.smoke.make_visible()

        self.chim = Rectangle(canvas=self.canvas, width=20, height=40, color="brown", fill="brown", line=2)
        self.chim.move_horizontal(250)
        self.chim.move_vertical(80)
        self.chim.make_visible()
      
        self.roof = Triangle(canvas=self.canvas, height=75, width=370, color="white", fill="green", line=2)
        self.roof.move_horizontal(-20)
        self.roof.move_vertical(180)
        self.roof.make_visible()

        self.roof_below = Triangle(canvas=self.canvas, height=1, width=370, color="green", fill="green", line=2)
        self.roof_below.move_horizontal(-20)
        self.roof_below.move_vertical(180)
        self.roof_below.make_visible()

        self.wall = Rectangle(canvas=self.canvas, width=350, height=200, color="saddle brown", fill="saddle brown", line=2)
        self.wall.move_horizontal(-20)
        self.wall.move_vertical(148)
        self.wall.make_visible()

        for i in range(50):
            self.wall = Rectangle(canvas=self.canvas, width=350, height=10, color="black", fill="saddle brown", line=2)
            self.wall.move_horizontal(-20)
            self.wall.move_vertical(148 + i * 5)
            self.wall.make_visible()

        self.window = Circle(canvas=self.canvas, diameter=120, color="black", fill="sienna1", line=1)
        self.window.move_horizontal(220)
        self.window.move_vertical(180)
        self.window.make_visible()

        self.fireplace = Rectangle(canvas=self.canvas, width=50, height=60, color="brown", fill="brown", line=2)
        self.fireplace.move_horizontal(230)
        self.fireplace.move_vertical(235)
        self.fireplace.make_visible()

        self.fireplace_pit = Rectangle(canvas=self.canvas, width=35, height=40, color="black", fill="black", line=2)
        self.fireplace_pit.move_horizontal(238)
        self.fireplace_pit.move_vertical(240)
        self.fireplace_pit.make_visible()

        self.fireplace_fire = Triangle(canvas=self.canvas, height=10, width=20, color="dark orange", fill="gold2", line=2)
        self.fireplace_fire.move_horizontal(255)
        self.fireplace_fire.move_vertical(295)
        self.fireplace_fire.make_visible()

        self.fireplace_log = Rectangle(canvas=self.canvas, width=20, height=40, color="saddle brown", fill="saddle brown", line=2)
        self.fireplace_log.move_horizontal(245)
        self.fireplace_log.move_vertical(260)
        self.fireplace_log.make_visible()

        self.chair_leg1 = Rectangle(canvas=self.canvas, width=2, height=30, color="DeepPink2", fill="DeepPink2", line=2)
        self.chair_leg1.move_horizontal(195)
        self.chair_leg1.move_vertical(245)
        self.chair_leg1.make_visible()

        self.chair_leg2 = Rectangle(canvas=self.canvas, width=2, height=10, color="DeepPink2", fill="DeepPink2", line=2)
        self.chair_leg2.move_horizontal(210)
        self.chair_leg2.move_vertical(265)
        self.chair_leg2.make_visible()

        self.chair_seat = Rectangle(canvas=self.canvas, width=20, height=2, color="DeepPink2", fill="DeepPink2", line=2)
        self.chair_seat.move_horizontal(195)
        self.chair_seat.move_vertical(265)
        self.chair_seat.make_visible()

        for i in range(20):
            self.floor = Rectangle(canvas=self.canvas, width=350, height=10, color="black", fill="saddle brown", line=2)
            self.floor.move_horizontal(-20)
            self.floor.move_vertical(273 + i * 5)
            self.floor.make_visible()

        self.window_fill = Circle(canvas=self.canvas, diameter=120, color="black", fill="", line=1)
        self.window_fill.move_horizontal(220)
        self.window_fill.move_vertical(180)
        self.window_fill.make_visible()

        self.beam1 = Rectangle(canvas=self.canvas, width=5, height=111, color="saddle brown", fill="saddle brown", line=2)
        self.beam1.move_horizontal(220)
        self.beam1.move_vertical(194)
        self.beam1.make_visible()

        self.beam1_2 = Rectangle(canvas=self.canvas, width=105, height=5, color="saddle brown", fill="saddle brown", line=2)
        self.beam1_2.move_horizontal(188)
        self.beam1_2.move_vertical(220)
        self.beam1_2.make_visible()

        self.window2 = Circle(canvas=self.canvas, diameter=60, color="black", fill="lightblue", line=1)
        self.window2.move_horizontal(50)
        self.window2.move_vertical(170)
        self.window2.make_visible()

        self.beam2 = Rectangle(canvas=self.canvas, width=5, height=60, color="saddle brown", fill="saddle brown", line=2)
        self.beam2.move_horizontal(38)
        self.beam2.move_vertical(180)
        self.beam2.make_visible()

        self.beam2_2 = Rectangle(canvas=self.canvas, width=60, height=5, color="saddle brown", fill="saddle brown", line=2)
        self.beam2_2.move_horizontal(10)
        self.beam2_2.move_vertical(208)
        self.beam2_2.make_visible()

        self.moon = Circle(canvas=self.canvas, diameter=140, color="grey", fill="grey", line=1)
        self.moon.move_horizontal(400)
        self.moon.move_vertical(-10)
        self.moon.make_visible()

        self.crater = Circle(canvas=self.canvas, diameter=20, color="black", fill="grey", line=1)
        self.crater.move_horizontal(430)
        self.crater.move_vertical(40)
        self.crater.make_visible()

        self.crater2 = Circle(canvas=self.canvas, diameter=35, color="black", fill="grey", line=1)
        self.crater2.move_horizontal(480)
        self.crater2.move_vertical(20)
        self.crater2.make_visible()

        self.crater3 = Circle(canvas=self.canvas, diameter=10, color="black", fill="grey", line=1)
        self.crater3.move_horizontal(460)
        self.crater3.move_vertical(70)
        self.crater3.make_visible()

        self.door = Rectangle(canvas=self.canvas, width=40, height=80, color="black", fill="salmon4", line=2)
        self.door.move_horizontal(95)
        self.door.move_vertical(270)
        self.door.make_visible()

        self.ground = Square(canvas=self.canvas, size=800, color="white", fill="white", line=2)
        self.ground.move_horizontal(-100)
        self.ground.move_vertical(350)
        self.ground.make_visible()

        self.door_knob = Circle(canvas=self.canvas, diameter=5, color="black", fill="yellow", line=1)
        self.door_knob.move_horizontal(165)
        self.door_knob.move_vertical(300)
        self.door_knob.make_visible()

        for i in range(50):
            for n in range(50):
                self.snow = Circle(canvas=self.canvas, diameter=5, color="snow", fill="snow", line=1)
                self.snow.move_horizontal(-10 + i * 20)
                if i % 2 == 0:
                    self.snow.move_vertical(-200 - (i * 5) + n * 50)
                else:
                    self.snow.move_vertical(-200 - (i * 8) + n * 50)
                self.snow.make_visible()

        self.path = Rectangle(canvas=self.canvas, width=30, height=200, color="black", fill="grey", line=2)
        self.path.move_horizontal(100)
        self.path.move_vertical(350)
        self.path.make_visible()

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
