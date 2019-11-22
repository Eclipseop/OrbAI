import App
import move


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


def generate_random_path(starting_index, moves):
    return "yeet", 123


if __name__ == "__main__":
    #print(count_matches("HHHHHLLLBDHLRLRDGBRLDGDHGLRHLG"))
    word, num = generate_random_path(1, 1)
    print(word)
    print(num)
