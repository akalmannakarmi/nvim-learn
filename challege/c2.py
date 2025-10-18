# Build a simple command-line todo list manager in Python.
# It should:
# Add tasks
# List tasks
# Mark tasks as done
# Save tasks to a JSON file

import sys
import json
from typing import Dict, List, Tuple

FILE_PATH="./challege/c2.json"


def add_task(task:str)->None:
    tasks = load_tasks()

    tasks.append((" ",task))

    save_tasks(tasks)


def list_tasks()->None:
    tasks = load_tasks()

    for i, task in enumerate(tasks):
        print(f"{i+1}. [{task[0]}] {task[1]}")

def mark_done(taskNo:int)->None:
    tasks = load_tasks()
    taskNo -= 1

    tasks[taskNo] = ("X",tasks[taskNo][1])

    save_tasks(tasks)


def load_tasks()->List[Tuple[str,str]]:
    try:
        with open(FILE_PATH,"r") as f:
            tasks = json.load(f)
        return tasks
    except FileNotFoundError:
        return []


def save_tasks(tasks:List[Tuple[str,str]])->None:
    with open(FILE_PATH,"w") as f:
        json.dump(tasks,f)



def run()->None:
    if sys.argv[1] == "add":
        add_task(sys.argv[2])
    elif sys.argv[1] == "list":
        list_tasks()
    elif sys.argv[1] == "done":
        mark_done(int(sys.argv[2]))
    else:
        print("Invalid Option")


if __name__ == "__main__":
    run()
