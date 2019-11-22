from enum import Enum
import math


class Move(Enum):
    up = -6
    left = -1
    right = 1
    down = 6

    def can_move(self, index):
        row = math.floor(index / 6)

        if index < 0 or index > 29:
            return False

        if self == Move.right and index == 0:
            return True
        if self == Move.left and index % 6 == 0:
            return False
        if self == Move.right and ((index - (0 if index % 6 == 0 else row)) % 5 == 0):
            return False
        if self == Move.up and index <= 5:
            return False
        if self == Move.down and index >= 24:
            return False

        return True


def get_available_moves(index):
    moves = []

    for move in Move:
        if move.can_move(index):
            moves.append(move)

    return moves


if __name__ == "__main__":
    print(get_available_moves(0))
