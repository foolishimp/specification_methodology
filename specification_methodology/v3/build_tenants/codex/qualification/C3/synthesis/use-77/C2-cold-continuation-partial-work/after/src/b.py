from a import compute_total


def report(xs):
    return compute_total(xs)


def summary(xs):
    return compute_total(xs) / len(xs)
