"""
Play bingo until the last board wins.  Display the final score of that board.
"""
import numpy as np


class Board:
    """
    A matrix of 5x5 items.
    """

    def __init__(self, lines):
        self.items = np.array([line.split() for line in lines], dtype=int)
        self.marked = np.zeros((5, 5), dtype=np.bool)

    def mark(self, draw):
        self.marked[self.items == int(draw)] = True

    def won(self):
        winning_row = np.any(np.all(self.marked, axis=0))
        winning_col = np.any(np.all(self.marked, axis=1))
        return winning_row or winning_col

    def score(self, lastdraw):
        return np.sum(self.items[self.marked == False]) * int(lastdraw)


def main(filename):
    # parse input file
    with open(filename) as txt:
        lines = txt.readlines()
    draws = lines[0].split(",")
    boards = [Board(lines[idx : idx + 5]) for idx in range(2, len(lines), 6)]
    # play
    for draw in draws:
        for board in boards[:]:
            board.mark(draw)
            if board.won():
                if len(boards) == 1:
                    return board.score(draw)
                else:
                    boards.remove(board)


if __name__ == "__main__":
    print(main("input.txt"))
