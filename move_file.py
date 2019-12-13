from termcolor import colored
from enum import Enum
import os
import shutil

class op(Enum):
    MOVE = "m"
    DELETE = "d"

def do_something(source, destination, operation):
    '''For "operation" argument use value od op enum'''
    try:
        for f in os.listdir(source):
            print(colored(f, "green"))
            src_file = os.path.join(source, f)
            dst_file = os.path.join(destination, f)
            if operation=="d":
                os.remove(src_file)
            elif operation=="m":
                shutil.move(src_file,dst_file)
            else:
                pass
    except Exception as e:
        print(colored(e,"red"))

