# Connect Four with a Minimax Opponent

**Python · NumPy · Pygame · Minimax · Alpha-beta pruning**

A local Connect Four game with a computer opponent. A NumPy board stores the position, a heuristic scores candidate windows, and a depth-three minimax search chooses the computer’s move.

## What this project demonstrates

- Board modeling and detection of horizontal, vertical, and diagonal wins.
- Alternating game-tree search with alpha-beta pruning.
- A Pygame interface separated from importable, testable game logic.

## Start here

| Read | Use it for |
| --- | --- |
| [Project walkthrough](docs/PROJECT_GUIDE.md) | Purpose, workflow, repository map, and a concrete example |
| [Code and artifact reference](docs/CODE_REFERENCE.md) | Important files, functions, classes, and their responsibilities |
| [Development guide](docs/DEVELOPMENT.md) | Setup, configuration, commands, tests, and remaining limitations |

## Explore locally

Use Python 3.11 or 3.12 in a virtual environment.

```sh
python -m pip install -r requirements.txt
python connect_4.py
python -m unittest discover -s tests -v
```

## Validation and scope

Five unit tests pass for game rules, tactical choices, draws, invalid columns, and board nonmutation. The Pygame interface also launched and closed using an SDL dummy display. Human interaction on a desktop and competitive AI strength have not been benchmarked. This is search-based game AI, not a trained model.

[Original demonstration](https://vimeo.com/373323901) is retained for historical context.

---

[GitHub profile](https://github.com/tariksalay) · [Portfolio](https://tariksalay.github.io/) · [Earlier README](README_HISTORY.md)

The earlier README is preserved as historical context; the guides above describe this branch's implementation.
