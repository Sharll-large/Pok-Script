import easygui as core


def msgbox(a: list):
    core.msgbox(a[0])


def msgbox_with_title(a: list):
    core.msgbox(a[0], title=a[1])


def ynbox(a: list):
    return core.ynbox(a[0])


def ynbox_with_title(a: list):
    return core.ynbox(a[0], title=a[1])


def enterbox(a: list):
    return core.enterbox(a[0])


def enterbox_with_title(a: list):
    return core.enterbox(a[0], title=a[1])
