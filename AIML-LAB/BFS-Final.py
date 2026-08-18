#!/usr/bin/env python3
from collections import deque


# ----------------------------------------------------
# MAZE
# 0 = Path
# 1 = Obstacle
# ----------------------------------------------------

print("Welcome to the BFS:")
rows = int(input("Enter rows: "))
cols = int(input("Enter columns: "))


maze = []
print("Enter the maze values note 0=path and 1=obstacle ")
for i in range(rows):
	row = []
	for j in range(cols):
		value = input(f"Enter value at ({i},{j}):")
		row.append(value)
	maze.append(row)


# ----------------------------------------------------
# User GIVING START AND END POSITIONS
# * = Start
# # = End
# ----------------------------------------------------
i1 = int(input("Enter starting row: "))
j1 = int(input("Enter starting column: "))

maze[i1][j1] = "*"

i2 = int(input("Enter Ending row: "))
j2 = int(input("Enter Ending column: "))

maze[i2][j2] = "#"

print("\nFollowing is your Entered Maze:")
for row in maze:
	print(" ".join(row))


start = (i1,j1)
end =(i2,j2)
rows = len(maze)
cols = len(maze[0])


# ----------------------------------------------------
# VISITED ARRAY
# ----------------------------------------------------

visited = [[False for _ in range(cols)] for _ in range(rows)]           


# ----------------------------------------------------
# PARENT ARRAY
#
# parent[row][col] stores the previous cell from
# which we reached the current cell.
# ----------------------------------------------------

parent = [[None for _ in range(cols)] for _ in range(rows)]                
# ----------------------------------------------------
# DIRECTIONS
#
# Up    = (-1,From (0,0):
# Down  = (1, 0)
# Left  = (0, -1)
# Right = (0, 1)
# ----------------------------------------------------

directions = [
    (-1, 0),
    (1, 0),
    (0, -1),
    (0, 1)
]


# ----------------------------------------------------
# BFS QUEUE
# ----------------------------------------------------

queue = deque()

queue.append(start)
visited[start[0]][start[1]] = True

found = False


# ----------------------------------------------------
# BFS ALGORITHM
# ----------------------------------------------------

while queue:

    current_row, current_col = queue.popleft()

    # If we reached the destination
    if (current_row, current_col) == end:
        found = True
        break

    # Check all four directions
    for dr, dc in directions:

        new_row = current_row + dr
        new_col = current_col + dc

        # Check whether the new position is inside the maze
        if (0 <= new_row < rows and
                0 <= new_col < cols):

            # Check whether:
            # 1. The cell has not been visited
            # 2. The cell is not an obstacle
            if (not visited[new_row][new_col] and
                    maze[new_row][new_col] != '1'):

                # Mark as visited
                visited[new_row][new_col] = True

                # Store the previous cell
                parent[new_row][new_col] = (
                    current_row,
                    current_col
                )

                # Add the cell to the queue
                queue.append((new_row, new_col))


# ----------------------------------------------------
# CHECK WHETHER A PATH EXISTS
# ----------------------------------------------------

if not found:

    print("No path exists from Start (*) to End (#).")

else:

    # ------------------------------------------------
    # RECONSTRUCT THE SHORTEST PATH
    # ------------------------------------------------

    current = end

    while current != start:

        row, col = current

        # Mark shortest path
        maze[row][col] = '.'

        # Move to the previous cell
        current = parent[row][col]


    # Keep start and end symbols
    maze[start[0]][start[1]] = '*'
    maze[end[0]][end[1]] = '#'


    # ------------------------------------------------
    # PRINT THE SOLVED MAZE
    # ------------------------------------------------

    print("\nSolved Maze:\n")

    for row in maze:
        print(" ".join(row))
