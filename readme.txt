1.  OVERVIEW

Given the extent of the martian plateau, the starting location and set of movement instructions for a set of rovers, marsrover.py computes the final destinations of these rovers.

Command Line Usage:

python marsrover.py test-input-1.txt

########################################################################################

2.  INSTALLATION

Clone the mars rover repository using the following command from the command line:

git clone https://github.com/andreweinhorn/marsrover.git .

To check that the correct files have been downloaded, you can run:

python marsrover.py test-input-1.txt

And you should receive the following output:

1 3 N
5 1 E

########################################################################################

3.  FILE MANIFEST

The following files should be present in the repository:

marsrover.py
readme.txt
test-input-1.txt
test-input-2.txt
test_marsrover.py

########################################################################################

4.  INPUT FILE

The marsrover script expects input in the form of a text file following a specific format.
NB.  There should be no empty lines in the input files!

Example Input File:
7 7
2 3 E
MMMRMLMRMM
6 6 W
MMLMMLMMRM

The meaning of these inputs is contained in the Problem Statement provided below.

########################################################################################

5.  OUTPUT

marsrover.py prints a list of final locations of the rovers specified in the input file.  In the example above, the output is as follows:

6 0 S
6 3 S

This indicates that the first rover ended up at coordinates (6,0) and was facing South, while the second rover ended up at coordinates (6,3) facing South.

########################################################################################

6.  TEST SUITE

Unit tests are compiled using Python's unittest module and are contained in  test_marsrover.py  The unit tests should be run from the command line as follows:

python test_marsrover.py -b

The -b flag suppresses print statements that usually occur with the calling of these functions.

These unit tests check various standard and edge cases for the following functions:

1.  destination(location, instructions, plateau)
2.  valid_instructions(instructions)
3.  valid_location(location)

The first function is the core function which converts the inputs into outputs.  The latter two functions check the user input and print descriptive messages should the input text file contain errors.

########################################################################################

7.  PROBLEM STATEMENT (courtesy of Google)

MARS ROVERS

A squad of robotic rovers are to be landed by NASA on a plateau on Mars.

This plateau, which is curiously rectangular, must be navigated by the rovers so that their on board cameras can get a complete view of the surrounding terrain to send back to Earth.

A rover's position is represented by a combination of an x and y co-ordinates and a letter representing one of the four cardinal compass points. The plateau is divided up into a grid to simplify navigation. An example position might be 0, 0, N, which means the rover is in the bottom left corner and facing North.

In order to control a rover, NASA sends a simple string of letters. The possible letters are 'L', 'R' and 'M'. 'L' and 'R' makes the rover spin 90 degrees left or right respectively, without moving from its current spot.

'M' means move forward one grid point, and maintain the same heading.

Assume that the square directly North from (x, y) is (x, y+1).

Input:

The first line of input is the upper-right coordinates of the plateau, the lower-left coordinates are assumed to be 0,0.

The rest of the input is information pertaining to the rovers that have been deployed. Each rover has two lines of input. The first line gives the rover's position, and the second line is a series of instructions telling the rover how to explore the plateau.

The position is made up of two integers and a letter separated by spaces, corresponding to the x and y co-ordinates and the rover's orientation.

Each rover will be finished sequentially, which means that the second rover won't start to move until the first one has finished moving.

Output:

The output for each rover should be its final co-ordinates and heading.

Test Input:

5 5
1 2 N
LMLMLMLMM
3 3 E
MMRMMRMRRM

Expected Output:

1 3 N
5 1 E
