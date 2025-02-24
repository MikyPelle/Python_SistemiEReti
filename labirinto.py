import random
import csv

def generate_maze(rows, cols):
    maze = []
    for i in range(rows):
        maze.append([1] * cols)

    for i in range(1, rows - 1, 2):
        for j in range(1, cols - 1, 2):
            maze[i][j] = 0

    for i in range(1, rows - 1, 2):
        for j in range(1, cols - 1, 2):
            direction = random.choice([(0, 1), (0, -1), (1, 0), (-1, 0)])
            neighbor_i = i + direction[0]
            neighbor_j = j + direction[1]
            if maze[neighbor_i][neighbor_j] == 1:
                maze[neighbor_i][neighbor_j] = 0
            else:
                continue
            wall_i = i + direction[0] // 2
            wall_j = j + direction[1] // 2
            maze[wall_i][wall_j] = 0

    return maze

def save_maze_to_csv(maze, filename):
    with open(filename, 'w', newline='') as csvfile:
        maze_writer = csv.writer(csvfile)
        for row in maze:
            maze_writer.writerow(row)

def main():
    rows = 11
    cols = 11
    maze = generate_maze(rows, cols)
    save_maze_to_csv(maze, 'maze.csv')

if __name__ == "__main__":
    main()
