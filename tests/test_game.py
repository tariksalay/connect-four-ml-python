import sys
from pathlib import Path
import unittest
import numpy as np
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import connect_4 as game


class GameTests(unittest.TestCase):
    def test_all_win_directions(self):
        for cells in [[(0, i) for i in range(4)], [(i, 0) for i in range(4)],
                      [(i, i) for i in range(4)], [(3 - i, i) for i in range(4)]]:
            board = game.create_board()
            for r, c in cells:
                game.drop_piece(board, r, c, game.PLAYER_PIECE)
            self.assertTrue(game.winning_move(board, game.PLAYER_PIECE))
            self.assertFalse(game.winning_move(board, game.AI_PIECE))

    def test_ai_wins_and_blocks(self):
        for piece in (game.PLAYER_PIECE, game.AI_PIECE):
            board = game.create_board()
            board[0, :3] = piece
            original = board.copy()
            col, _ = game.minmax(board, 2, True)
            self.assertEqual(col, 3)
            np.testing.assert_array_equal(board, original)

    def test_full_column_and_invalid_columns(self):
        board = game.create_board()
        board[:, 0] = game.PLAYER_PIECE
        for col in (0, -1, 7, None):
            self.assertFalse(game.is_valid_location(board, col))
        self.assertIsNone(game.get_next_open_row(board, 0))

    def test_draw_board(self):
        board = np.array([[1, 1, 2, 2, 1, 1, 2], [2, 2, 1, 1, 2, 2, 1]] * 3)
        self.assertFalse(game.winning_move(board, 1))
        self.assertFalse(game.winning_move(board, 2))
        self.assertEqual(game.minmax(board, 3, True), (None, 0))
        self.assertIsNone(game.pick_best_move(board, 2))

    def test_depth_validation(self):
        with self.assertRaises(ValueError):
            game.minmax(game.create_board(), -1, True)


if __name__ == '__main__':
    unittest.main()
