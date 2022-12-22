import rand.base as base

fns = {
    "random.seed": {
        "take_args": 1,
        "locate": base.seed
    },
    "random.random": {
        "take_args": 0,
        "locate": base.random
    },
    "random.randrange": {
        "take_args": 2,
        "locate": base.randrange
    },
    "random.randint": {
        "take_args": 2,
        "locate": base.randint
    }
}
