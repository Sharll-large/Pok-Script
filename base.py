import random


def Print(a: list):
    print(a[0], end='')

def Println(a: list):
    print(a[0])

def Add(a: list):
    return a[0] + a[1]

def Minus(a: list):
    return a[0] - a[1]

def MulAdd(a: list):
    return a[0] * a[1]

def MulMinus(a: list):
    return a[0] / a[1]

def Input():
    return input()

def Randint(a: list):
    return random.randint(a[0], a[1])

def toInt(a:list):
    return int(a[list])

def toString(a: list):
    return str(a[list])
