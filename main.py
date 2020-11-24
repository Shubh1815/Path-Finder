import os
import threading
import tkinter as tk
import pygame
from grid import Grid

class App(tk.Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.minsize(800, 501)
        self.resizable(0, 0)
        self.title("Path Finder")

        container = tk.Frame(self, width="800", height="501", bg="black")
        container.rowconfigure(0, weight=1)    # Expanding the 1st row
        container.columnconfigure(1, weight=1) # Expanding the 2nd column
        container.pack(fill=tk.X)

        embed = tk.Frame(container, width=501, height=501)
        embed.grid(row=0, column=0, padx=5, pady=5)

        self.toolkit = tk.Frame(container, bg="#30475e")
        self.toolkit.grid(
            row=0,
            column=1,
            sticky='NSEW',
            padx=5,
            pady=5
        )

        os.environ['SDL_WINDOWID'] = str(embed.winfo_id())
        self.update()

        pygame.display.init()
        win = pygame.display.set_mode((501, 501))
        win.fill((20, 39, 78))

        grid = Grid(win, 50, 50)
        grid.initialize()
        pygame.display.update()

        self.toolkit_section()


    def toolkit_section(self):

        label = tk.Label(
                    self.toolkit,
                    text="PATH-FINDER",
                    bg="#30475e",
                    fg="#ffffff"
                )
        label.config(font=("Helvetica", 24))
        label.pack(fill=tk.X)

if __name__ == '__main__':
    root = App()
    root.mainloop()
