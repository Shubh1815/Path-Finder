import os
import threading
import tkinter as tk
import pygame
from grid import Grid
from utils import Button, Checkbutton, Label

class App(tk.Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.minsize(800, 501)
        self.resizable(0, 0)
        self.title("Path Finder")
        self.protocol('WM_DELETE_WINDOW', self.quit)
        self.running = True

        container = tk.Frame(self, width="800", height="501", bg="black")
        container.rowconfigure(0, weight=1)    # Expanding the 1st row
        container.columnconfigure(1, weight=1) # Expanding the 2nd column
        container.pack(fill=tk.X)

        embed = tk.Frame(container, width=501, height=501)
        embed.grid(row=0, column=0, padx=5, pady=5)

        self.toolkit = tk.Frame(container, bg="#212b44")
        self.toolkit.columnconfigure(0, weight=1)
        self.toolkit.columnconfigure(1, weight=1)
        self.toolkit.grid(
            row=0,
            column=1,
            sticky='NSEW',
            padx=5,
            pady=5
        )

        self.visualize_maze = tk.IntVar()
        self.perfect_maze = tk.IntVar()

        os.environ['SDL_WINDOWID'] = str(embed.winfo_id())
        self.update()

        pygame.display.init()
        win = pygame.display.set_mode((501, 501))

        self.grid = Grid(win, 50, 50)
        self.clear_maze_thread = None
        self.generate_maze_thread = None
        self.clear_maze()

        pygame.display.update()

        self.toolkit_section()

    def toolkit_section(self):

        title = tk.Frame(self.toolkit)
        title.grid(row=0, column=0, columnspan=2, pady=10)

        Label(
            title,
            text="PATH-FINDER",
            fontSize=24
        ).pack(fill=tk.X)

        Label(
            self.toolkit,
            text="Maze Generation",
            fontSize=14
        ).grid(row=1, column=0, padx=10, pady=5)

        Checkbutton(
            self.toolkit,
            variable=self.visualize_maze,
            text="Visualize",
        ).grid(row=2, column=0, padx=10, pady=5, sticky='WE')

        Checkbutton(
            self.toolkit,
            text="Perfect Maze\n(Only 1 soultion)",
            variable=self.perfect_maze,
        ).grid(row=2, column=1, padx=10, pady=5, sticky='WE')

        Button(
            self.toolkit,
            text="Generate Maze",
            command=self.generate_maze
        ).grid(row=3, column=0, columnspan=2, padx=10, pady=5, sticky='WE')

        Button(
            self.toolkit,
            text="Clear Maze",
            command=self.clear_maze
        ).grid(row=4, column=0, columnspan=2, padx=10,pady=5, sticky='WE')

    def clear_maze(self):
        if (not self.generate_maze_thread or \
           not self.generate_maze_thread.is_alive()) and \
           (not self.clear_maze_thread or not self.clear_maze_thread.is_alive()):

            self.clear_maze_thread = threading.Thread(
                target=self.grid.initialize
            )
            self.clear_maze_thread.start()

    def generate_maze(self):
        if (not self.generate_maze_thread or \
           not self.generate_maze_thread.is_alive()) and \
           (not self.clear_maze_thread or not self.clear_maze_thread.is_alive()):

            self.generate_maze_thread = threading.Thread(
                target=self.grid.generate_maze,
                args=(self.visualize_maze.get(), self.perfect_maze.get() + 1)
            )
            self.generate_maze_thread.start()

    def quit(self):
        if self.clear_maze_thread and self.clear_maze_thread.is_alive():
            self.clear_maze_thread.join()
        if self.generate_maze_thread and self.generate_maze_thread.is_alive():
            self.generate_maze_thread.join()

        self.running = False
        self.destroy()

        

if __name__ == '__main__':
    root = App()
    root.mainloop()
    
