import tkinter as tk
from grid import Grid
from algorithms.a_star import a_star
from utils import Button, Checkbutton, Label

class App(tk.Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.minsize(800, 501)
        self.resizable(0, 0)
        self.title("Path Finder")

        self.visualize_maze = tk.IntVar()
        self.perfect_maze = tk.IntVar()

        container = tk.Frame(self, width="800", height="501", bg="black")
        container.rowconfigure(0, weight=1)    # Expanding the 1st row
        container.columnconfigure(1, weight=1) # Expanding the 2nd column
        container.pack(fill=tk.X)

        self.canvas = tk.Canvas(
            container,
            width=501,
            height=501,
            bg="#14274e",
            highlightthickness=0,
        )
        self.canvas.grid(row=0, column=0, padx=5, pady=5)

        self.toolkit = tk.Frame(container, bg="#334062")
        self.toolkit.columnconfigure(0, weight=1)
        self.toolkit.columnconfigure(1, weight=1)
        self.toolkit.grid(
            row=0,
            column=1,
            sticky='NSEW',
            padx=5,
            pady=5
        )

        self.grid = Grid(self.canvas, 25, 25)
        self.grid.initialize()

        self.canvas.bind('<Button-1>', self.grid.mark_cell)

        self.toolkit_section()

    def toolkit_section(self):

        title = tk.Frame(self.toolkit)
        title.grid(row=0, column=0, columnspan=2, pady=10)

        Label(
            title,
            text="PATH-FINDER",
            size=24
        ).pack(fill=tk.X)

        Label(
            self.toolkit,
            text="Maze Generation",
            size=14
        ).grid(row=1, column=0, padx=10, pady=10, sticky='W')

        Button(
            self.toolkit,
            text="Generate Maze",
            command=lambda: self.grid.generate_maze(
                self.visualize_maze.get(), 
                self.perfect_maze.get() + 1
            )
        ).grid(row=2, column=0, padx=10, pady=5, sticky='WE')

        Checkbutton(
            self.toolkit,
            variable=self.visualize_maze,
            text="Visualize",
        ).grid(row=2, column=1, padx=10, pady=5, sticky='W')

        Button(
            self.toolkit,
            text="Clear Maze",
            command=self.grid.reset
        ).grid(row=3, column=0, padx=10,pady=5, sticky='WE')

        Checkbutton(
            self.toolkit,
            text="Perfect Maze\n(Only 1 soultion)",
            variable=self.perfect_maze,
        ).grid(row=3, column=1, padx=10, pady=5, sticky='W')

        Label(
            self.toolkit,
            text="Path Finding",
            size=14
        ).grid(row=5, column=0, padx=10, pady=10, sticky='W')

        Button(
            self.toolkit,
            text="Find Path",
            command=lambda: a_star(self.grid),
        ).grid(row=6, column=0, columnspan=2, padx=10,pady=5, sticky='WE')

if __name__ == '__main__':
    root = App()
    root.mainloop()
