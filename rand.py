import random


def rand(l: list) -> int:
    return random.choice(l)


def lucky() -> bool:
    l = [i for i in range(1, 1000000 + 1)]

    if random.choice(l) == 1:
        return True
    return False

