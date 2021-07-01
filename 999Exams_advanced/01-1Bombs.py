from collections import deque

DATURA_BOMBS = 40
CHERRY_BOMBS = 60
SMOKE_DECOY_BOMBS = 120
datura_bombs_made = 0
cherry_bombs_made = 0
smoke_decoy_bombs_made = 0
successfully = False
bombs = deque([int(x) for x in input().split(", ")])
casings = [int(x) for x in input().split(", ")]


def sum_of_materials(value1, value2):
    return value1 + value2


def print_pouch():
    if not successfully:
        return print("You don't have enough materials to fill the bomb pouch.")
    return print("Bene! You have successfully filled the bomb pouch!")


def print_bombs():
    if not len(bombs):
        return print("Bomb Effects: empty")
    return print(f"Bomb Effects: {', '.join(map(str, bombs))}")


def print_casings():
    if not len(casings):
        return print("Bomb Casings: empty")
    return print(f"Bomb Casings: {', '.join(map(str, casings))}")


def print_created_bombs():
    return print(f"Cherry Bombs: {cherry_bombs_made}\n"
                 f"Datura Bombs: {datura_bombs_made}\n"
                 f"Smoke Decoy Bombs: {smoke_decoy_bombs_made}")


def check_if_enough_bombs_made():
    if datura_bombs_made >= 3 \
            and cherry_bombs_made >= 3 \
            and smoke_decoy_bombs_made >= 3:
        return True
    return False


def check_if_bombs_or_casings_equal_zero():
    if len(bombs) == 0 or len(casings) == 0:
        return True
    return False


while True:
    if check_if_bombs_or_casings_equal_zero():
        break

    if check_if_enough_bombs_made():
        successfully = True
        break

    current_bombs = bombs.popleft()
    current_casing = casings.pop()

    total = sum_of_materials(current_bombs, current_casing)
    if total == DATURA_BOMBS:
        datura_bombs_made += 1
    elif total == CHERRY_BOMBS:
        cherry_bombs_made += 1
    elif total == SMOKE_DECOY_BOMBS:
        smoke_decoy_bombs_made += 1
    else:
        current_casing -= 5
        bombs.insert(0, current_bombs)
        casings.append(current_casing)

print_pouch()
print_bombs()
print_casings()
print_created_bombs()
