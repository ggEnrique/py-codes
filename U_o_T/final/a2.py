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
        () -> str
        Return a string representation of this Rat.

        >>> rat1 = Rat('P',3,4)
        >>> rat1.set_location(6,7)
        >>> rat1.eat_sprout()
        >>> rat1.eat_sprout()
        >>> rat1.__str__()
        'P at (6, 7) ate 2 sprouts.'
        """

        return "{0} at ({1}, {2}) ate {3} sprouts.".format(
            self.symbol, self.row, self.col, self.num_sprouts_eaten
        )


class Maze:
    """A 2D maze."""

    def __init__(self, maze, f1, f2, num_of_sprouts_left=0):
        """
        Initialize the maze with the given parameters.
    
        __init__(list of list of str, Rat, Rat, int) -> None

        >>> my_maze = Maze([['#', '#', '#', '#', '#', '#', '#'],\
        ['#', '.', '.', '.', '.', '.', '#'],\
        ['#', '.', '#', '#', '#', '.', '#'],\
        ['#', '.', '.', '@', '#', '.', '#'],\
        ['#', '@', '#', '.', '@', '.', '#'],\
        ['#', '#', '#', '#', '#', '#', '#']],\
        Rat('J', 1, 1),\
        Rat('P', 1, 4))
        >>> my_maze.num_of_sprouts_left
        3
        """
        self.maze = maze
        self.rat_1 = f1
        self.rat_2 = f2
        self.num_of_sprouts_left = num_of_sprouts_left

        self.maze[self.rat_1.row][self.rat_1.col] = self.rat_1.symbol

        self.maze[self.rat_2.row][self.rat_2.col] = self.rat_2.symbol

        for item in maze:
            for i in item:
                if i == SPROUT:
                    self.num_of_sprouts_left += 1

    def is_wall(self, row, col):
        """
        Determine if the given location in the maze contains a wall.
    
        is_wall(int, int) -> bool
        
        >>> my_maze = Maze([['#', '#', '#', '#', '#', '#', '#'],\
        ['#', '.', '.', '.', '.', '.', '#'],\
        ['#', '.', '#', '#', '#', '.', '#'],\
        ['#', '.', '.', '@', '#', '.', '#'],\
        ['#', '@', '#', '.', '@', '.', '#'],\
        ['#', '#', '#', '#', '#', '#', '#']],\
        Rat('J', 1, 1),\
        Rat('P', 1, 4))
        >>> my_maze.is_wall(0,0)
        True
        >>> my_maze.is_wall(1,1)
        False
        >>> my_maze.is_wall(4,1)
        False
        >>> my_maze.is_wall(4,2)
        True
        """
        if self.maze[row][col] == WALL:
            return True
        return False

    def get_character(self, row, col):
        """
        Return the character at the specified location in the maze.
    
        get_character(int, int) -> str
        
        >>> my_maze = Maze([['#', '#', '#', '#', '#', '#', '#'],\
        ['#', '.', '.', '.', '.', '.', '#'],\
        ['#', '.', '#', '#', '#', '.', '#'],\
        ['#', '.', '.', '@', '#', '.', '#'],\
        ['#', '@', '#', '.', '@', '.', '#'],\
        ['#', '#', '#', '#', '#', '#', '#']],\
        Rat('J', 1, 1),\
        Rat('P', 1, 4))
        >>> my_maze.get_character(0,0)
        '#'
        >>> my_maze.get_character(1,1)
        'J'
        >>> my_maze.get_character(1,4)
        'P'
        >>> my_maze.get_character(4,1)
        '@'
        >>> my_maze.get_character(4,5)
        '.'
        """
        # chars = [WALL, HALL, SPROUT, rat_1_CHAR, RAT_2_CHAR]
        # for ch in chars:
        #     if self.maze[row][col] == ch:
        #         return ch
        return self.maze[row][col]

    def move(self, rat, vertical_up_down_no_row, horizontal_left_right_no_col):
        """
        >>> my_maze = Maze([['#', '#', '#', '#', '#', '#', '#'],\
        ['#', '.', '.', '.', '.', '.', '#'],\
        ['#', '.', '#', '#', '#', '.', '#'],\
        ['#', '.', '.', '@', '#', '.', '#'],\
        ['#', '@', '#', '.', '@', '.', '#'],\
        ['#', '#', '#', '#', '#', '#', '#']],\
        Rat('J', 1, 1),\
        Rat('P', 1, 4))
        >>> my_maze.move(my_maze.rat_1, UP, NO_CHANGE)
        False
        >>> my_maze.move(my_maze.rat_1, DOWN, NO_CHANGE)
        True
        >>> my_maze.rat_1.row
        2
        >>> my_maze.rat_1.col
        1
        >>> my_maze.get_character(1,1)
        '.'
        >>> my_maze.get_character(1,2)
        'J'
        >>> my_maze.move(my_maze.rat_1, NO_CHANGE, LEFT)
        False
        """
        if self.is_wall(
            rat.row + vertical_up_down_no_row, rat.col + horizontal_left_right_no_col
        ):
            return False
        else:
            self.maze[rat.row][rat.col] = HALL
            if (
                self.get_character(
                    rat.row + vertical_up_down_no_row,
                    rat.col + horizontal_left_right_no_col,
                )
                == SPROUT
            ):
                rat.eat_sprout()
                self.num_of_sprouts_left -= 1
            self.maze[rat.row + vertical_up_down_no_row][
                rat.col + horizontal_left_right_no_col
            ] = rat.symbol
            rat.set_location(
                rat.row + vertical_up_down_no_row,
                rat.col + horizontal_left_right_no_col,
            )
            return True

    def __str__(self):
        """ >>> my_maze = Maze([['#', '#', '#', '#', '#', '#', '#'],\
        ['#', '.', '.', '.', '.', '.', '#'],\
        ['#', '.', '#', '#', '#', '.', '#'],\
        ['#', '.', '.', '@', '#', '.', '#'],\
        ['#', '@', '#', '.', '@', '.', '#'],\
        ['#', '#', '#', '#', '#', '#', '#']],\
        Rat('J', 1, 1),\
        Rat('P', 1, 4))
        >>> print(my_maze.__str__())
        #######
        #J..P.#
        #.###.#
        #..@#.#
        #@#.@.#
        #######
        J at (1, 1) ate 0 sprouts.
        P at (1, 4) ate 0 sprouts.
        """

        out_maze = ""
        for row in self.maze:
            for ch in row:
                out_maze += ch
            out_maze += "\n"
        return out_maze + self.rat_1.__str__() + "\n" + self.rat_2.__str__()


if __name__ == "__main__":
    import doctest

    doctest.testmod()
