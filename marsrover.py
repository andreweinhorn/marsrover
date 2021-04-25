import sys

## A class to record the coordinates and direction of a rover
class Rover:
    def __init__(self, x, y, dir):
        self.x = x
        self.y = y
        self.dir = dir

    def position(self):
        print(str(self.x) + ' ' + str(self.y) + ' ' + self.dir)

    ## Moves the rover forward one position
    def move(self):
        if self.dir == 'N': self.y += 1
        if self.dir == 'E': self.x += 1
        if self.dir == 'S': self.y -= 1
        if self.dir == 'W': self.x -= 1

    ## Turns rover 90 degrees to the right
    def turn_right(self):
        turn_right = {'N': 'E', 'E': 'S', 'S': 'W', 'W': 'N'}
        self.dir = turn_right[self.dir]

    ## Turns rover 90 degrees to the left
    def turn_left(self):
        turn_left = {'N': 'W', 'W': 'S', 'S': 'E', 'E': 'N'}
        self.dir = turn_left[self.dir]

## A function to test the validity of the location input
def valid_location(location):

    # Check that there are exactly three arguments in the location
    if(len(location) != 3):
        print("Invalid Location: Location input should contain three arguments separated by spaces")
        return False
    location_x = location[0]
    location_y = location[1]
    direction = location[2]

    # Check that the first two arguments are digits
    if not (location_x.isdigit() and location_y.isdigit()):
        print("Invalid Location: Location x and y values should be integers")
        return False

    # Check that the final argument is a cardinal direction
    if direction not in ['N', 'E', 'S', 'W']:
        print("Invalid Location: Location does not contain a valid direction")
        return False

    return True

## A function to test the validity of the instructions input
def valid_instructions(instructions):
    for instruction in instructions:
        if instruction not in ['L', 'R', 'M']:
            print("Invalid Instruction: Instruction should be L, R or M.  {} received.".format(instruction))
            return False
    return True

## Computes the destination of the rover given its location, instructions, and the extent of the plateau
def destination(location, instructions, plateau):
    plateau_x = int(plateau[0])
    plateau_y = int(plateau[1])

    ## Create rover object with given coordinates
    rover = Rover(int(location[0]), int(location[1]), location[2])

    # Execute each instruction in sequence
    for instruction in instructions:
        if instruction == 'M': rover.move()
        if instruction == 'L': rover.turn_left()
        if instruction == 'R': rover.turn_right()

        # If at any time the rover coordinates fall outside of the plateau, print error message
        if rover.x < 0 or rover.x > plateau_x or rover.y < 0 or rover.y > plateau_y:
            print("Oh no, your rover fell off the plateau!")
            return False

    # Print the rover's final position
    rover.position()

    # Return the rover's final position
    return [rover.x, rover.y, rover.dir]

def handle_input(textfile):

    ## Open the input file
    with open(textfile, 'r') as f:

        ## Get the maximum x and y values for the plateau
        plateau = f.readline().rstrip('\n').split(' ')

        ## Get the location and instructions for the rovers and check they are valid
        while True:

            # Check if we have reached the end of the file
            location = f.readline()
            if(len(location) == 0): break

            # Grab the location of the rover
            location = location.rstrip('\n').split(' ')

            # Grab the instructions for that rover
            instructions = list(f.readline().rstrip('\n'))

            # If location and instructions are valid, compute the destination
            if valid_location(location) and valid_instructions(instructions):
                result = destination(location, instructions, plateau)


if __name__ == "__main__":
    if(len(sys.argv) != 2):
        print("Input Error: marsrover.py requires you to specify an input text file")
    else:
        textfile = sys.argv[1]
        handle_input(textfile)

