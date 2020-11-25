import time
import random
import pygame

class Cell:
    def __init__(self, win, x, y, length=10):
        self.pos_x = x * length
        self.pos_y = y * length
        self.length = length
        self.win = win

        self.wall = {
            'up': True,
            'right': True,
            'down': True,
            'left': True
        }

        self.generate_boundary()

    def fill(self, color=(255, 255, 255)):

        pygame.draw.rect(
            self.win,
            color,
            pygame.Rect(
                self.pos_x + 1,
                self.pos_y + 1,
                self.length - 1,
                self.length - 1
            )
        )

        pygame.display.update()

    def generate_boundary(self):

        wall_color = (0, 0, 0)
        no_wall = (82, 5, 123)

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

    def destroy_wall(self, side):
        self.wall[side] = False
        self.generate_boundary()

class Grid:
    def __init__(self, win, length, width):
        self.win = win
        self.length = length
        self.width = width
        self.grid = [[0 for i in range(width)] for j in range(length) ]

    def initialize(self):
        self.win.fill((20, 39, 78))

        for i in range(self.length):
            for j in range(self.width):
                self.grid[i][j] = Cell(self.win, j, i)

        pygame.display.update()

    def generate_maze(self, visualize, perfect_maze):
        self.initialize()
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

            if not visited[i][j] or (visited[i][j] < 2 and random.random() <= 0.3):
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
                time.sleep(0.005)
            self.grid[i][j].fill((82, 5, 123))
