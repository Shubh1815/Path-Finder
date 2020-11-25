import time
import random

class Cell:
    def __init__(self, canvas, x, y, length=20):
        self.pos_x = x * length
        self.pos_y = y * length
        self.length = length
        self.canvas = canvas

        self.wall = {
            'up': [True, self.canvas.create_line(
                self.pos_x, self.pos_y,
                self.pos_x + self.length, self.pos_y,
                fill="#000000"
            )],
            'right': [True, self.canvas.create_line(
                self.pos_x + self.length, self.pos_y,
                self.pos_x + self.length, self.pos_y + self.length,
                fill="#000000"
            )],
            'down': [True, self.canvas.create_line(
                self.pos_x, self.pos_y + self.length,
                self.pos_x + self.length, self.pos_y + self.length,
                fill="#000000"
            )],
            'left': [True, self.canvas.create_line(
                self.pos_x, self.pos_y,
                self.pos_x, self.pos_y + self.length,
                fill="#000000"
            )]
        }

        self.cell = self.canvas.create_rectangle(
                        self.pos_x + 1,
                        self.pos_y + 1,
                        self.pos_x + self.length - 1,
                        self.pos_y + self.length - 1,
                        width=0
                    )

    def fill(self, color="#ffffff"):
        self.canvas.itemconfig(self.cell, fill=color, outline=color, width=1)

    def reset(self):
        self.canvas.itemconfig(
            self.cell,
            fill="#14274e",
            outline="#14274e"
        )
        for _, wall in self.wall.values():
            self.canvas.itemconfig(wall, fill="#000000")

    def destroy_wall(self, side):
        self.wall[side][0] = False
        self.canvas.itemconfig(self.wall[side][1], fill="#52057b")

class Grid:
    def __init__(self, canvas, length, width):
        self.canvas = canvas
        self.length = length
        self.width = width
        self.grid = [[0 for i in range(width)] for j in range(length) ]

    def initialize(self):
        self.canvas.config(bg="#14274e")

        for i in range(self.length):
            for j in range(self.width):
                self.grid[i][j] = Cell(self.canvas, j, i)

    def reset(self):
        for i in range(self.length):
            for j in range(self.width):
                self.grid[i][j].reset()

    def generate_maze(self, visualize, perfect_maze):
        visited = [[ 0 for i in range(self.width)] for j in range(self.length)]
        opposite = {
            'up': 'down',
            'down': 'up',
            'left': 'right',
            'right': 'left'
        }

        stack = [(0, 0, -1, -1, None)]

        while stack:

            i, j, prev_i, prev_j, direction = stack.pop(-1)

            if not visited[i][j] or (visited[i][j] < 2 and random.random() <= 0.2):
                # if visited highlight the node
                visited[i][j] += perfect_maze

                if direction:
                    self.grid[prev_i][prev_j].destroy_wall(direction)
                    self.grid[i][j].destroy_wall(opposite[direction])

                neighbour = [
                    ((i - 1, j), 'up'),
                    ((i, j - 1), 'left'),
                    ((i + 1, j), 'down'),
                    ((i, j + 1), 'right')
                ]

                random.shuffle(neighbour)

                for (next_i, next_j), direction in neighbour:
                    if 0 <= next_i < self.length and 0 <= next_j < self.width:
                        stack.append((next_i, next_j, i, j, direction))

            else:
                # if visited highlight the parent node
                visited[i][j] += 1
                i, j = prev_i, prev_j

            self.grid[i][j].fill()
            if visualize:
                time.sleep(0.0125)
            self.grid[i][j].fill("#52057b")
