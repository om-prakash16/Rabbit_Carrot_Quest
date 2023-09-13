import random

# Initialize game parameters
grid_size = 25
num_carrots = 5
num_rabbit_holes = 3

# Define game symbols
rabbit = 'r'
carrot = 'c'
rabbit_hole = 'O'
pathway_stone = '-'

# Initialize the 2D grid
grid = [[pathway_stone] * grid_size for _ in range(grid_size)]

# Place rabbit, carrots, and rabbit holes on the grid
rabbit_x = random.randint(0, grid_size - 1)
rabbit_y = random.randint(0, grid_size - 1)
grid[rabbit_y][rabbit_x] = rabbit

carrot_positions = random.sample([(x, y) for x in range(grid_size) for y in range(grid_size)], num_carrots)
for x, y in carrot_positions:
    grid[y][x] = carrot

hole_positions = random.sample([(x, y) for x in range(grid_size) for y in range(grid_size)], num_rabbit_holes)
for x, y in hole_positions:
    grid[y][x] = rabbit_hole

# Initialize game state
carrot_held = False

# Function to display the grid
def display_grid():
    for row in grid:
        print("".join(row))

# Game loop
while True:
    # Display the grid
    display_grid()

    # Check for victory condition
    if carrot_held and (rabbit_x, rabbit_y) in hole_positions:
        print("Congratulations! You won the game!")
        break

    # Get user input
    move = input("Enter move (a/d/w/s/p/j/q to quit): ").lower()

    # Handle user input
    if move == 'q':
        print("Quitting the game.")
        break
    elif move in ['a', 'd', 'w', 's']:
        # Calculate the new rabbit position
        new_x, new_y = rabbit_x, rabbit_y
        if move == 'a' and rabbit_x > 0:
            new_x -= 1
        elif move == 'd' and rabbit_x < grid_size - 1:
            new_x += 1
        elif move == 'w' and rabbit_y > 0:
            new_y -= 1
        elif move == 's' and rabbit_y < grid_size - 1:
            new_y += 1

        # Check for obstacles (carrots and rabbit holes)
        if grid[new_y][new_x] == carrot:
            if carrot_held:
                print("You can only hold one carrot at a time.")
            else:
                grid[rabbit_y][rabbit_x] = pathway_stone
                grid[new_y][new_x] = rabbit.upper()
                rabbit_x, rabbit_y = new_x, new_y
                carrot_held = True
        elif grid[new_y][new_x] == rabbit_hole:
            print("You cannot jump into a rabbit hole directly.")
        elif grid[new_y][new_x] == pathway_stone:
            grid[rabbit_y][rabbit_x] = pathway_stone
            grid[new_y][new_x] = rabbit
            rabbit_x, rabbit_y = new_x, new_y
    elif move == 'p':
        if carrot_held:
            adjacent_positions = [(rabbit_x - 1, rabbit_y), (rabbit_x + 1, rabbit_y),
                                  (rabbit_x, rabbit_y - 1), (rabbit_x, rabbit_y + 1)]
            for x, y in adjacent_positions:
                if (x, y) in hole_positions:
                    grid[rabbit_y][rabbit_x] = pathway_stone
                    grid[y][x] = pathway_stone
                    carrot_held = False
                    break
        else:
            print("You need to pick up a carrot first.")
    elif move == 'j':
        hole_above = (rabbit_x, rabbit_y - 1)
        hole_below = (rabbit_x, rabbit_y + 1)
        hole_left = (rabbit_x - 1, rabbit_y)
        hole_right = (rabbit_x + 1, rabbit_y)

        if hole_above in hole_positions:
            grid[rabbit_y][rabbit_x] = pathway_stone
            grid[hole_above[1]][hole_above[0]] = rabbit
            rabbit_x, rabbit_y = hole_above
        elif hole_below in hole_positions:
            grid[rabbit_y][rabbit_x] = pathway_stone
            grid[hole_below[1]][hole_below[0]] = rabbit
            rabbit_x, rabbit_y = hole_below
        elif hole_left in hole_positions:
            grid[rabbit_y][rabbit_x] = pathway_stone
            grid[hole_left[1]][hole_left[0]] = rabbit
            rabbit_x, rabbit_y = hole_left
        elif hole_right in hole_positions:
            grid[rabbit_y][rabbit_x] = pathway_stone
            grid[hole_right[1]][hole_right[0]] = rabbit
            rabbit_x, rabbit_y = hole_right
        else:
            print("No rabbit hole to jump to.")
    else:
        print("Invalid move. Use a/d/w/s/p/j/q.")
