import random as rand


def seed(a: list):
    rand.seed(a[0])


def random():
    return rand.random()


def randrange(a: list):
    return rand.randrange(a[0], a[1])


def randint(a: list):
    return rand.randint(a[0], a[1])
