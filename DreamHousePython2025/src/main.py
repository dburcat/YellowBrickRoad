import tkinter as tk
from Picture import Picture

def main():
    root = tk.Tk()
    app = Picture(root)
    root.mainloop()

if __name__ == "__main__":
    main()