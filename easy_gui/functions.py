import easy_gui.base as base

fns = {
    "easygui.msgbox": {
        "take_args": 1,
        "locate": base.msgbox
    },
    "easygui.t_msgbox": {
        "take_args": 2,
        "locate": base.msgbox_with_title
    },
    "easygui.ynbox": {
        "take_args": 1,
        "locate": base.ynbox
    },
    "easygui.t_ynbox": {
        "take_args": 2,
        "locate": base.ynbox_with_title
    },
    "easygui.enterbox": {
        "take_args": 1,
        "locate": base.enterbox
    },
    "easygui.t_enterbox": {
        "take_args": 2,
        "locate": base.enterbox_with_title
    }
}
