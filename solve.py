import random
import app
import board


def get_best_moveset(board_string, iterations, min, max):
    best_path = None
    max_combo = 0
    min_moves = 100

    for i in range(iterations):
        rand_path = board.generate_random_path(
            random.randint(0, 29), random.randint(min, max))
        followed_path = board.follow_path(board_string, rand_path)

        combo = board.count_matches(followed_path)
        moves = len(followed_path[1])
        if combo >= max_combo:
            print(f"Moves: {moves}, Combos: {combo}")
            max_combo = combo
            min_moves = moves
            best_path = rand_path

    return best_path


def solve():
    board_string = app.generate_board_string()
    move_set = get_best_moveset(board_string, 1000, 5, 40)

    print(move_set)


if __name__ == "__main__":
    solve()
