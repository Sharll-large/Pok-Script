import queue
import sys

import functions


def Compile(code: str):
    ed = [""]
    in_str = False
    for k in range(len(code)):
        char = code[k]
        if in_str:
            ed.append(ed.pop() + char)
            if char == "\"":
                in_str = False
        else:
            if char == " ":
                ed.append("")
            else:
                ed.append(ed.pop() + char)
                if char == "\"":
                    in_str = True
    return ed


vars_list = {}

def Run(code: str):
    def call(func: str):
        args = []
        if functions.fns[func]["take_args"] != 0:
            for j in range(functions.fns[func]["take_args"]):
                args.append(solve(main_queue.get()))
            result = functions.fns[func]["locate"](args)
        else:
            result = functions.fns[func]["locate"]()
        return result

    main_queue = queue.Queue()
    for i in Compile(code):
        main_queue.put(i)

    def solve(obj: str) -> any:
        if obj == "": return None
        elif obj[0] == obj[-1] == "\"": return obj[1:-1]
        elif obj in vars_list: return vars_list[obj]
        elif obj in functions.fns:
            result = call(obj)
            if result is not None:
                return result
        else:
            try: return int(obj)
            except:
                try: return float(obj)
                except:
                    print("I don't know what is", obj)
                    exit(1)

    while not main_queue.empty():
        one = main_queue.get()
        if one == "set":
            a, b = main_queue.get(), main_queue.get()
            vars_list[a] = solve(b)
        elif one in functions.fns: call(one)

target_file = sys.argv[1]
command = (open(target_file, "r").read()).split("\n")
for i in command:
    Run(i)
input("\nThe program was completed. Press enter to exit...")
