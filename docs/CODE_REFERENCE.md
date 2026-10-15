# Code and artifact reference

[Overview](../README.md) · [Walkthrough](PROJECT_GUIDE.md) · [Development guide](DEVELOPMENT.md)

This reference describes the files on this branch. Function names are navigation aids; the walkthrough explains how their inputs, state, and outputs fit together.

## Python modules

### [connect_4.py](../connect_4.py)

Board rules, scoring, alpha-beta minimax, and the optional Pygame event loop.

- `create_board()`
- `drop_piece(board, row, col, piece)`
- `is_valid_location(board, col)`
- `get_next_open_row(board, col)`
- `print_board(board)`
- `winning_move(board, piece)`
- `evaluate_window(window, piece)`
- `score_position(board, piece)`
- `is_terminal_node(board)`
- `minmax(board, depth, maximizingPlayer, alpha=-math.inf, beta=math.inf)`
- `get_valid_locations(board)`
- `pick_best_move(board, piece)`
- `draw_board(board)`
- `main()`

## Checks and setup

[Tests](../tests/) contains the focused checks described in the [development guide](DEVELOPMENT.md). Consult that guide for dependencies, commands, and the boundary between automated validation and untested integrations.
