import random
import sys

target_file = sys.argv[1]

main_stack = []

var = {"pok:about:version": "1.0"}

import functions

def Compile(code: str):
    ed = [""]
    in_str = False
    for k in range(len(code) - 1, -1, -1):
        char = code[k]
        if in_str:
            ed.append(char + ed.pop())
            if char == "\"":
                in_str = False
        else:
            if char == " ":
                ed.append("")
            else:
                ed.append(char + ed.pop())
                if char == "\"":
                    in_str = True
    return ed


def is_string(Object: str):
    if Object[0] == Object[-1] == "\"":
        return True
    return False

def is_num(Object: str):
    try:
        float(Object)
        return True
    except:
        return False

def is_int(Object: str):
    try:
        int(Object)
        return True
    except:
        return False

# coding:utf-8

def run(codes):
    code = codes[:]
    global var, main_stack
    com = Compile(code)
    for n in range(len(com)):
        # print(main_stack)
        now_command = com[n]
        if not is_string(now_command) and not is_num(now_command) and now_command in var:
            main_stack.append(var[now_command])
        elif is_string(now_command):
            main_stack.append(now_command[1:-1])
        elif is_int(now_command):
            main_stack.append(int(now_command))
        elif is_num(now_command):
            main_stack.append(float(now_command))
        elif now_command in functions.fns:
            args = []
            for i in range(functions.fns[now_command]["take_args"]):
                args.append(main_stack.pop())
            result = functions.fns[now_command]["locate"](args)
            if result is not None:
                main_stack.append(result)
        elif now_command == "set":
            a, b = main_stack.pop(), main_stack.pop()
            var[a] = b
        else:
            main_stack.append(now_command)


command = (open(target_file, "r").read()).split("\n")
for i in command:
    run(i)
input("\nThe program was completed. Press enter to exit...")
sys.exit(0)
