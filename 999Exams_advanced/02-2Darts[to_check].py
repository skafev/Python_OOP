player_one, player_two = input().strip().split(", ")



def make_matrix():
    matrix = []
    for s in range(7):
        rows = input().strip().split()
        rows_to_append = []
        for r in rows:
            rows_to_append.append(r)
        matrix.append(rows_to_append)
    return matrix


def is_valid(row, col):
    if 0 <= row < len(matrix) and 0 <= col < len(matrix):
        return True
    return False


throws_turns = 0
score_player_one = 501
score_player_two = 501
matrix = make_matrix()
game_ends = False
while True:
    if score_player_one <= 0 or score_player_two <= 0:
        break
    throw = input().strip().replace("(", "").replace(")", "").split(", ")
    throws_turns += 1
    current_row = int(throw[0])
    current_column = int(throw[1])
    if not is_valid(current_row, current_column):
        continue
    if matrix[current_row][current_column] == "D":
        total = 0
        # TO MAKE IT search fo the number!!!
        total += int(matrix[current_row][0])
        total += int(matrix[current_row][6])
        total += int(matrix[0][current_column])
        total += int(matrix[6][current_column])
        total = total * 2
        if throws_turns % 2 == 0:
            score_player_two -= total
        else:
            score_player_one -= total
    elif matrix[current_row][current_column] == "T":
        total = 0
        total += int(matrix[current_row][0])
        total += int(matrix[current_row][6])
        total += int(matrix[0][current_column])
        total += int(matrix[6][current_column])
        total = total * 3
        if throws_turns % 2 == 0:
            score_player_two -= total
        else:
            score_player_one -= total
    elif matrix[current_row][current_column] == "B":
        if throws_turns % 2 == 0:
            print(f"{player_two} won the game with {throws_turns // 2} throws!")
            game_ends = True
            break
        else:
            print(f"{player_one} won the game with {throws_turns} throws!")
            game_ends = True
            break
    else:
        try:
            if int(matrix[current_row][current_column]) <= 24:
                if throws_turns % 2 == 0:
                    score_player_two -= int(matrix[current_row][current_column])
                else:
                    score_player_one -= int(matrix[current_row][current_column])
        except ValueError:
            continue

if not game_ends:
    if score_player_one <= 0:
        print(f"{player_one} won the game with {throws_turns} throws!")
    else:
        print(f"{player_two} won the game with {throws_turns // 2} throws!")
