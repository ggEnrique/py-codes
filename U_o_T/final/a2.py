# Do not import any modules. If you do, the tester may reject your submission.

# Constants for the contents of the maze.

# The visual representation of a wall.
WALL = "#"

# The visual representation of a hallway.
HALL = "."

# The visual representation of a brussels sprout.
SPROUT = "@"

# Constants for the directions. Use these to make Rats move.

# The left direction.
LEFT = -1

# The right direction.
RIGHT = 1

# No change in direction.
NO_CHANGE = 0

# The up direction.
UP = -1

# The down direction.
DOWN = 1

# The letters for rat_1 and rat_2 in the maze.
RAT_1_CHAR = "J"
RAT_2_CHAR = "P"


class Rat:
    """A rat caught in a maze."""

    # Write your Rat methods here.
    def __init__(self, symbol, row, col, num_sprouts_eaten=0):
        """
        (Rat, str, int, int, int) -> None

        Initializes a new Rat instance with specified attributes.

        >>> rat1 = Rat('P',3,4)
        >>> rat1.symbol
        'P'
        >>> rat1.row
        3
        >>> rat1.col
        4
        """
        self.symbol = symbol
        self.row = row
        self.col = col
        self.num_sprouts_eaten = num_sprouts_eaten

    def set_location(self, row, col):
        """
        (Rat, int, int) -> None

        Sets a new location for the rat.

        >>> rat1 = Rat('P',3,4)
        >>> rat1.set_location(6,7)
        >>> rat1.row
        6
        >>> rat1.col
        7
        """
        self.row = row
        self.col = col

    def eat_sprout(self):
        """
        (Rat) -> None

        Increases the count of sprouts eaten by the rat by 1.

        >>> rat1 = Rat('P',3,4)
        >>> rat1.eat_sprout()
        >>> rat1.num_sprouts_eaten
        1
        >>> rat1.eat_sprout()
        >>> rat1.num_sprouts_eaten
        2
        """
        self.num_sprouts_eaten += 1

    def __str__(self):
        """
        >>> rat1 = Rat('P',3,4)
        >>> rat1.set_location(6,7)
        >>> rat1.eat_sprout()
        >>> rat1.eat_sprout()
        >>> rat1.__str__()
        'P at (6, 7) ate 2 sprouts.'
        """

        return "{0} at ({1}, {2}) ate {3} sprouts.".format(self.symbol, self.row, self.col, self.num_sprouts_eaten)


class Maze:
    """A 2D maze."""

    # Write your Maze methods here.
    def __init__(self, maze, Rat1, Rat2):
        

if __name__ == "__main__":
    import doctest

    doctest.testmod()
