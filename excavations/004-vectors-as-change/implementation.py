"""Treat vectors as displacements that can be composed and scaled."""


def add(left, right):
    if len(left) != len(right):
        raise ValueError("vectors must have the same dimensions")
    return [a + b for a, b in zip(left, right)]


def subtract(left, right):
    return add(left, [-value for value in right])


def scale(amount, vector):
    return [amount * value for value in vector]


if __name__ == "__main__":
    start = [2, 3]
    waypoint = [7, 1]
    finish = [8, 5]
    first_change = subtract(waypoint, start)
    second_change = subtract(finish, waypoint)
    total_change = add(first_change, second_change)
    print("first change:", first_change)
    print("second change:", second_change)
    print("composed change:", total_change)
    print("reconstructed finish:", add(start, total_change))
