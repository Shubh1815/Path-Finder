import time
import random

class Cell:
    def __init__(self, canvas, x, y, length=20):
        self.pos_x = x * length
        self.pos_y = y * length
        self.length = length
        self.canvas = canvas
        self.selected = 0

        self.wall = {
            'up': [True, self.canvas.create_line(
                self.pos_x, self.pos_y,
                self.pos_x + self.length, self.pos_y,
                fill="#000000",
                width=1.5,
            )],
            'right': [True, self.canvas.create_line(
                self.pos_x + self.length, self.pos_y,
                self.pos_x + self.length, self.pos_y + self.length,
                fill="#000000",
                width=1.5,
            )],
            'down': [True, self.canvas.create_line(
                self.pos_x, self.pos_y + self.length,
                self.pos_x + self.length, self.pos_y + self.length,
                fill="#000000",
                width=1.5,
            )],
            'left': [True, self.canvas.create_line(
                self.pos_x, self.pos_y,
                self.pos_x, self.pos_y + self.length,
                fill="#000000",
                width=1.5,
            )]
        }

        self.cell = self.canvas.create_rectangle(
                        self.pos_x + 1.5,
                        self.pos_y + 1.5,
                        self.pos_x + self.length - 1.5,
                        self.pos_y + self.length - 1.5,
                        width=0
                    )

    def get_neighbour(self):
        neighbours = []

        if not self.wall['left'][0]:
            neighbours.append((0, -1))
        if not self.wall['right'][0]:
            neighbours.append((0, 1))
        if not self.wall['up'][0]:
            neighbours.append((-1, 0))
        if not self.wall['down'][0]:
            neighbours.append((1, 0))

        return neighbours

    def fill(self, color="#ffffff"):
        self.canvas.itemconfig(self.cell, fill=color, outline=color, width=1)
        self.canvas.update_idletasks()

    def select(self):
        color = ("#52057b", "#03c4a1")
        self.selected ^= 1
        self.fill(color[self.selected])

    def reset(self):
        self.selected = 0
        self.canvas.itemconfig(
            self.cell,
            fill="#14274e",
            outline="#14274e"
        )
        for w in self.wall:
            self.wall[w][0] = True
            self.canvas.itemconfig(self.wall[w][1], fill="#000000")
            self.canvas.update_idletasks()

    def destroy_wall(self, *sides):
        for side in sides:
            self.wall[side][0] = False
            self.canvas.itemconfig(self.wall[side][1], fill="#52057b")
            self.canvas.update_idletasks()

class Grid:
    def __init__(self, canvas, length, width):
        self.canvas = canvas
        self.length = length
        self.width = width
        self.grid = [[0 for i in range(width)] for j in range(length) ]
        self.is_maze = False
        self.solved = False

        self.nodes = []

    def initialize(self):
        self.canvas.config(bg="#14274e")

        for i in range(self.length):
            for j in range(self.width):
                self.grid[i][j] = Cell(self.canvas, j, i)

    def reset(self):
        self.is_maze = False
        self.solved = False
        self.nodes = []
        for i in range(self.length):
            for j in range(self.width):
                self.grid[i][j].reset()

    def generate_maze(self, visualize, perfect_maze):

        if self.is_maze:
            self.reset()

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

            if not visited[i][j] or (visited[i][j] < 2 and random.random() <= 0.6):
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

        self.is_maze = True

    def mark_cell(self, pos):
        if self.is_maze:
            pos_x, pos_y = pos.x, pos.y
            cell = self.grid[pos_y // 20][pos_x // 20]
            if not cell.selected and len(self.nodes) < 2:
                cell.select()
                self.nodes.append((pos_y // 20, pos_x // 20))
            elif cell.selected:
                cell.select()
                self.nodes.remove((pos_y // 20, pos_x // 20))
