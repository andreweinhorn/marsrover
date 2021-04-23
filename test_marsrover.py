import unittest
import marsrover

class TestMarsRover(unittest.TestCase):

    def test_destination(self):

        ## Normal run from A to B using left turns
        location = [1, 2, 'N']
        instructions = list('LMLMLMLMM')
        plateau = [5,5]
        self.assertEqual(marsrover.destination(location, instructions, plateau), [1, 3, 'N'])

        ## Normal run from A to B using left turns
        location = [3, 3, 'E']
        instructions = list('MMRMMRMRRM')
        plateau = [5, 5]
        self.assertEqual(marsrover.destination(location, instructions, plateau), [5, 1, 'E'])

        ## Normal run from A to B using combination of turn directions
        location = [6, 6, 'E']
        instructions = list('MMRMMRMLMMLM')
        plateau = [15, 12]
        self.assertEqual(marsrover.destination(location, instructions, plateau), [8, 2, 'E'])

        ## Edge Case: List of instructions takes Mars Rover off the edge of the plateau
        location = [4, 4, 'N']
        instructions = list('MMMRMMRMMM')
        plateau = [5, 5]
        self.assertEqual(marsrover.destination(location, instructions, plateau), False)

        ## Edge Case: User input starts with rover outside of plateau
        location = [-2, 4, 'E']
        instructions = list('MMMMMMRMM')
        plateau = [5, 5]
        self.assertEqual(marsrover.destination(location, instructions, plateau), False)

        ## Edge Case: Plateau has only one square
        location = [0, 0, 'E']
        instructions = list('LLLLL')
        plateau = [0, 0]
        self.assertEqual(marsrover.destination(location, instructions, plateau), [0,0,'N'])

    def test_valid_instructions(self):
        self.assertEqual(marsrover.valid_instructions(list('MMLMRMMRLM')), True)
        self.assertEqual(marsrover.valid_instructions(list('MMLMRxMRLM')), False)
        self.assertEqual(marsrover.valid_instructions(list('')), True)
        self.assertEqual(marsrover.valid_instructions(list('L M M')), False)

    def test_valid_location(self):
        self.assertEqual(marsrover.valid_location(['0', '4', 'N']), True)
        self.assertEqual(marsrover.valid_location(['0', '4' ]), False)
        self.assertEqual(marsrover.valid_location(['0', '4', 'n']), False)
        self.assertEqual(marsrover.valid_location(['']), False)


if __name__ == '__main__':
    unittest.main()