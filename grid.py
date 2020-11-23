import random
import pygame

class Cell:
    def __init__(self, win, x, y, length=10):
        self.pos_x = x * length
        self.pos_y = y * length
        self.length = length
        self.wall = {
            'up': True,
            'down': True,
            'left': True,
            'right': True,
        }
        self.win = win
        self.generate_boundary()

    def generate_boundary(self):

        wall_color = (0, 0, 0)
        no_wall = (20, 39, 78)

        # LEFT
        pygame.draw.line(
            self.win,
            wall_color if self.wall['left'] else no_wall,
            (self.pos_x, self.pos_y),
            (self.pos_x, self.pos_y + self.length)
        )

        # RIGHT
        pygame.draw.line(
            self.win,
            wall_color if self.wall['right'] else no_wall,
            (self.pos_x + self.length, self.pos_y),
            (self.pos_x + self.length, self.pos_y + self.length)
        )

        # UP
        pygame.draw.line(
            self.win,
            wall_color if self.wall['up'] else no_wall,
            (self.pos_x, self.pos_y),
            (self.pos_x + self.length, self.pos_y)
        )

        # DOWN
        pygame.draw.line(
            self.win,
            wall_color if self.wall['down'] else no_wall,
            (self.pos_x, self.pos_y + self.length),
            (self.pos_x + self.length, self.pos_y + self.length)
        )

class Grid:
    def __init__(self, win, length, width):
        self.win = win
        self.length = length
        self.width = width
        self.grid = [[0 for i in range(width)] for j in range(length) ]

    def initialize(self):
        for i in range(self.length):
            for j in range(self.width):
                self.grid[i][j] = Cell(self.win, i, j)

    def generate_maze(self):
        visited = [[False for i in range(self.width)] for j in range(self.length)]
        stack = [(0, 0)]

        while stack:

            i, j = stack.pop(-1)

            if visited[i][j]:
                continue

            visited[i][j] = True

            neighbours = [
                ((i - 1, j), 'up'),
                ((i, j + 1), 'right'),
                ((i + 1, j), 'down'),
                ((i, j - 1), 'left')
            ]

            random.shuffle(neighbours)

            for ( x, y ), direction in neighbours:

                if 0 <= x < self.length and 0 <= y < self.width:
                    if not visited[x][y]:

                        self.grid[x][y].wall[direction] = False
                        self.grid[x][y].generate_boundary()

                        stack.append((x, y))

            pygame.display.update()
