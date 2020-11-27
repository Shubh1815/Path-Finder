import heapq
import time

def manhattan_distance(cor_x1, cor_y1, cor_x2, cor_y2):
    return abs(cor_x1 - cor_x2) + abs(cor_y1 - cor_y2)

def mark_visited(cell, color):
    cell.fill(color)
    time.sleep(0.005)

def construct_path(grid, came_from, end, start, color="#00587a"):
    node = end
    while node != start and came_from[node] != start:
        node = came_from[node]
        pos_x, pos_y = node
        grid[pos_x][pos_y].fill(color)
        time.sleep(0.0125)

def a_star(grid):
    if len(grid.nodes) < 2 or grid.solved:
        return
    start, end = grid.nodes

    start_x, start_y = start
    end_x, end_y = end

    came_from = {}

    length = len(grid.grid)
    width = len(grid.grid[0])

    visited = [[0 for i in range(width)] for j in range(length)]
    visited[start_x][start_y] = 1

    g_score = [[float('inf') for i in range(width)] for j in range(length)]
    g_score[start_x][start_y] = 0

    f_score = [[float('inf') for i in range(width)] for j in range(length)]
    f_score[start_x][start_y] = manhattan_distance(start_x, start_y, end_x, end_y)

    open_set = [(f_score[start_x][start_y], start_x, start_y)]

    while open_set:

        current = heapq.heappop(open_set)

        if current[1:] == end:
            construct_path(grid.grid, came_from, current[1:], start)
            break

        current_x, current_y = current[1:]
        neighbours = grid.grid[current_x][current_y].get_neighbour()

        for neighbour in neighbours:
            next_node_x = current_x + neighbour[0]
            next_node_y = current_y + neighbour[1]

            if 0 <= next_node_x < length and 0 <= next_node_y < width:
                tentative_g_score = g_score[current_x][current_y] + 1
                if tentative_g_score < g_score[next_node_x][next_node_y]:

                    if (next_node_x, next_node_y) not in (start, end):
                        # Still could be explored further
                        mark_visited(grid.grid[next_node_x][next_node_y], '#61b15a')

                    came_from[(next_node_x, next_node_y)] = current[1:]
                    g_score[next_node_x][next_node_y] = tentative_g_score

                    heuristic = manhattan_distance(next_node_x, next_node_y, end_x, end_y)

                    f_score[next_node_x][next_node_y] = tentative_g_score + heuristic

                    heapq.heappush(
                        open_set,
                        (f_score[next_node_x][next_node_y], next_node_x, next_node_y)
                    )
                else:
                    # Explored Node
                    if (next_node_x, next_node_y) not in (start, end):
                        mark_visited(grid.grid[next_node_x][next_node_y], '#9a1f40')
    grid.solved = True
