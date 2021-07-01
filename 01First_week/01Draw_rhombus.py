def content(count, symbol, line=0):
    line = line * " "
    stars = f"{symbol} " * count
    print(f"{line}{stars}".rstrip())


def draw_rhombus(n):
    for i in range(n):
        content(i + 1, "*", n - i - 1)
    for i in range(n - 2, -1, -1):
        content(i + 1, "*", n - i - 1)


draw_rhombus(int(input()))
