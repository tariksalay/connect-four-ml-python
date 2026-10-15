# Connect Four — Python Minimax Game

**Python · Pygame · NumPy · Minimax Search · Heuristic Evaluation**

An interactive Connect Four game built with Pygame, featuring a computer opponent that selects moves using depth-limited **minimax search** and a hand-designed board-scoring heuristic.

## How it works

- Models a traditional 7-column × 6-row Connect Four board with NumPy.
- Checks horizontal, vertical, and diagonal four-in-a-row winning conditions.
- Evaluates candidate moves using center-column preference, possible four-piece windows, and opponent threats.
- Searches alternating moves with a minimax depth of **3** in the current game loop.
- Draws the board and handles player input through Pygame.

## Key code

| Function | Responsibility |
| --- | --- |
| `create_board` / `drop_piece` | Store board state and make moves |
| `winning_move` | Detect a winning four-piece alignment |
| `evaluate_window` / `score_position` | Score board positions |
| `minmax` | Explore possible turns and choose the best available move |
| `draw_board` | Render the current game state |

## Original demonstration

[Watch the original video on Vimeo](https://vimeo.com/373323901)

## Running locally

The single-file program is [connect_4.py](connect_4.py). A typical exploratory setup would require Python, NumPy, and Pygame. The file also imports `mcts`, but **no `mcts.py` module is included in this repository**, which may cause an import failure even though the game loop uses `minmax`.

```bash
pip install numpy pygame
python connect_4.py
```

These commands describe the intended execution path, **not a currently verified working installation**. To run successfully, resolve the missing `mcts` dependency or remove its unused import as a separate code change.

## Limitations

This is a learning project and not a benchmarked competitive game AI. The current minimax implementation has a fixed search depth and does not implement alpha-beta pruning. The name "ML" in the repository name refers to game-search AI; **there is no trained machine-learning model** in the current code.

[GitHub profile](https://github.com/tariksalay)
