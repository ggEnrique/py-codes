import unittest
import a2

maze_map = [
            ["#", "#", "#", "#", "#", "#", "#"],
            ["#", ".", ".", ".", ".", ".", "#"],
            ["#", ".", "#", "#", "#", ".", "#"],
            ["#", ".", ".", "@", "#", ".", "#"],
            ["#", "@", "#", ".", "@", ".", "#"],
            ["#", "#", "#", "#", "#", "#", "#"],
        ]

rat1 = a2.Rat("J", 1, 1)

rat2 = a2.Rat("P", 1, 4)

class Test_move_up(unittest.TestCase):
    def test_move_down(self):

        my_maze_game = a2.Maze(maze_map,rat1,rat2)

        my_maze_game.move(rat1,a2.UP,a2.NO_CHANGE)

        actual_1_1 = my_maze_game.get_character(1,1)
        actual_0_1 = my_maze_game.get_character(0,1)

        self.assertEqual(actual_1_1,"J")
        self.assertEqual(actual_0_1,"#")


    def test_move_down(self):

        my_maze_game = a2.Maze(maze_map,rat1,rat2)

        my_maze_game.move(rat1,a2.DOWN,a2.NO_CHANGE)

        actual_1_1 = my_maze_game.get_character(1,1)
        actual_2_1 = my_maze_game.get_character(2,1)

        self.assertEqual(actual_1_1,".")
        self.assertEqual(actual_2_1,"J")

if __name__ == "__main__":
    unittest.main(exit=False)
    