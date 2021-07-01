def make_matrix():
    size = int(input())
    matrix = []
    for s in range(size):
        rows = input()
        rows_to_append = []
        for r in rows:
            rows_to_append.append(r)
        matrix.append(rows_to_append)
    return matrix


def is_valid(row, col):
    if 0 <= row < len(matrix) and 0 <= col < len(matrix):
        return True
    return False


food_quantity = 0
matrix = make_matrix()
snake_row = None
snake_column = None
snake_found = False

for j in range(len(matrix)):
    if not snake_found:
        for i in range(len(matrix)):
            if matrix[j][i] == "S":
                snake_row = j
                snake_column = i
                snake_found = True
                break


snake_out_of_boundary = False
while True:
    if food_quantity == 10:
        print("You won! You fed the snake.")
        break
    if snake_out_of_boundary:
        print("Game over!")
        break

    command = input()

    if command == "left":
        if is_valid(snake_row, snake_column - 1):
            current_position = matrix[snake_row][snake_column - 1]
            if current_position == "B":
                for j in range(len(matrix)):
                    for i in range(len(matrix)):
                        if matrix[j][i] == "B":
                            if j == snake_row and i == snake_column - 1:
                                continue
                            matrix[snake_row][snake_column] = "."
                            matrix[snake_row][snake_column - 1] = "."
                            snake_row = j
                            snake_column = i
                            matrix[snake_row][snake_column] = "S"
            elif current_position == "*":
                food_quantity += 1
                matrix[snake_row][snake_column] = "."
                snake_column = snake_column - 1
                matrix[snake_row][snake_column] = "S"
            else:
                matrix[snake_row][snake_column] = "."
                snake_column = snake_column - 1
                matrix[snake_row][snake_column] = "S"
        else:
            matrix[snake_row][snake_column] = "."
            snake_out_of_boundary = True

    elif command == "right":
        if is_valid(snake_row, snake_column + 1):
            current_position = matrix[snake_row][snake_column + 1]
            if current_position == "B":
                for j in range(len(matrix)):
                    for i in range(len(matrix)):
                        if matrix[j][i] == "B":
                            if j == snake_row and i == snake_column + 1:
                                continue
                            matrix[snake_row][snake_column] = "."
                            matrix[snake_row][snake_column + 1] = "."
                            snake_row = j
                            snake_column = i
                            matrix[snake_row][snake_column] = "S"
            elif current_position == "*":
                food_quantity += 1
                matrix[snake_row][snake_column] = "."
                snake_column = snake_column + 1
                matrix[snake_row][snake_column] = "S"
            else:
                matrix[snake_row][snake_column] = "."
                snake_column = snake_column + 1
                matrix[snake_row][snake_column] = "S"
        else:
            matrix[snake_row][snake_column] = "."
            snake_out_of_boundary = True

    elif command == "up":
        if is_valid(snake_row - 1, snake_column):
            current_position = matrix[snake_row - 1][snake_column]
            if current_position == "B":
                for j in range(len(matrix)):
                    for i in range(len(matrix)):
                        if matrix[j][i] == "B":
                            if j == snake_row - 1 and i == snake_column:
                                continue
                            matrix[snake_row][snake_column] = "."
                            matrix[snake_row - 1][snake_column] = "."
                            snake_row = j
                            snake_column = i
                            matrix[snake_row][snake_column] = "S"
            elif current_position == "*":
                food_quantity += 1
                matrix[snake_row][snake_column] = "."
                snake_row = snake_row - 1
                matrix[snake_row][snake_column] = "S"
            else:
                matrix[snake_row][snake_column] = "."
                snake_row = snake_row - 1
                matrix[snake_row][snake_column] = "S"
        else:
            matrix[snake_row][snake_column] = "."
            snake_out_of_boundary = True

    elif command == "down":
        if is_valid(snake_row + 1, snake_column):
            current_position = matrix[snake_row + 1][snake_column]
            if current_position == "B":
                for j in range(len(matrix)):
                    for i in range(len(matrix)):
                        if matrix[j][i] == "B":
                            if j == snake_row + 1 and i == snake_column:
                                continue
                            matrix[snake_row][snake_column] = "."
                            matrix[snake_row + 1][snake_column] = "."
                            snake_row = j
                            snake_column = i
                            matrix[snake_row][snake_column] = "S"
            elif current_position == "*":
                food_quantity += 1
                matrix[snake_row][snake_column] = "."
                snake_row = snake_row + 1
                matrix[snake_row][snake_column] = "S"
            else:
                matrix[snake_row][snake_column] = "."
                snake_row = snake_row + 1
                matrix[snake_row][snake_column] = "S"
        else:
            matrix[snake_row][snake_column] = "."
            snake_out_of_boundary = True

print(f"Food eaten: {food_quantity}")

print(*[''.join(map(str, m)) for m in matrix], sep="\n")
