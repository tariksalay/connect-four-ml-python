# Development and validation

Use Python 3.11 or 3.12:

```sh
python -m venv .venv
# Activate the virtual environment for your shell.
python -m pip install -r requirements.txt
python connect_4.py
python -m unittest discover -s tests -v
```

The optional Pygame UI now starts only from `main()`. Importing `connect_4` exposes the NumPy game logic without opening a display or requiring the missing `mcts` package. The minimax search uses alpha-beta pruning and center-first ordering. Full boards, invalid columns, and terminal moves are handled explicitly; the event loop is capped at 60 frames per second.

Tests cover all four winning directions, winning/blocking choices, nonmutation of the input board, and draws. Display/interaction checks require a desktop or SDL dummy driver.
