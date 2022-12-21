import base
fns = {
    "print":{
        "take_args": 1,
        "locate": base.Print
    },
    "println":{
        "take_args": 1,
        "locate": base.Println
    },
    "+":{
        "take_args": 2,
        "locate": base.Add
    },
    "-":{
        "take_args": 2,
        "locate": base.Minus
    },
    "*":{
        "take_args": 2,
        "locate": base.MulAdd
    },
    "/":{
        "take_args": 2,
        "locate": base.MulMinus
    },
    "input":{
        "take_args": 0,
        "locate": base.Input
    },
    "randint":{
        "take_args": 2,
        "locate": base.Randint
    },
    "int":{
        "take_args": 1,
        "locate": base.toInt
    },
    "string":{
        "take_args": 1,
        "locate": base.toString
    }
}