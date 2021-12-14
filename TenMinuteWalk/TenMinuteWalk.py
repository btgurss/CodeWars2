# Determining if random walk created by app will take person back to start and last exactly 10 minutes if
# each move is one minute

def is_valid_walk(walk):
    # Setting variables equal to counters
    north_south = 0
    east_west = 0
    minutes = 0

    # Using for loops to add or subtract to each counter
    for letter in walk:
        if letter == 'n':
            north_south += 1
        elif letter == 's':
            north_south -= 1
        elif letter == 'e':
            east_west += 1
        elif letter == 'w':
            east_west -= 1
        minutes += 1
        print(minutes)
    # Using if statement to return true or false
    if minutes <= 10 and north_south == 0 and east_west == 0:
        return True
    else:
        return False

test = ['n', 's', 'n', 's', 'n', 's', 'n', 'e', 'w', 's']
print(is_valid_walk(test))