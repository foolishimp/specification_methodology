def positive_square_total(values: tuple[int, ...]) -> int:
    total = 0
    for value in values:
        if value > 0:
            total += value * value
    return total
