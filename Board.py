import App
import move
import random


def on_board(index):
    return 0 <= index <= 29


# TODO: rewrite this
def count_matches(board_string):
    matches = 0
    already_matching = set()

    for i, color in enumerate(board_string):
        if i in already_matching:
            continue

        moves = move.get_available_moves(i)
        for amove in moves:
            count = 1
            crossed_indexes = [i]
            last_index = i
            while amove in move.get_available_moves(last_index):
                neighbor_color = board_string[last_index + amove.value]
                if neighbor_color != color:
                    break
                op_index = crossed_indexes[0] + (amove.value * -1)
                if on_board(op_index) and board_string[op_index] == color:
                    already_matching.update(crossed_indexes)
                    break
                last_index += amove.value
                crossed_indexes.append(last_index)
                count += 1
            if count >= 3:
                already_matching.update(crossed_indexes)
                matches += 1

    return matches


def generate_random_path(starting_index, number_of_moves):
    path = []
    last_move = random.choice(move.get_available_moves(starting_index))
    index = starting_index

    for i in range(number_of_moves):
        move_set = list(filter(lambda x: x.value != (last_move.value * -1),
                               move.get_available_moves(index)))
        amove = random.choice(move_set)
        path.append(amove)
        last_move = amove
        index += amove.value

    return starting_index, path


def follow_path(board_string, move_set):
    starting_index, moves = move_set

    last_index = starting_index
    pickup = board_string[starting_index]
    board_string = list(board_string)
    for amove in moves:
        board_string[last_index] = board_string[last_index + amove.value]
        board_string[last_index + amove.value] = pickup
        last_index += amove.value

    return board_string