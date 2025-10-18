# build a simple command-line todo list manager in python.
# it should:
# add tasks
# list tasks
# mark tasks as done
# save tasks to a json file

import sys
import json
from typing import List, Tuple

file_path = "./challege/c2.json"


def add_task(task: str) -> None:
    tasks = load_tasks()

    tasks.append((" ", task))

    save_tasks(tasks)


def list_tasks() -> None:
    tasks = load_tasks()

    for i, task in enumerate(tasks):
        print(f"{i + 1}. [{task[0]}] {task[1]}")


def mark_done(taskno: int) -> None:
    tasks = load_tasks()
    taskno -= 1

    tasks[taskno] = ("x", tasks[taskno][1])

    save_tasks(tasks)


def load_tasks() -> List[Tuple[str, str]]:
    try:
        with open(file_path, "r") as f:
            tasks = json.load(f)
        return tasks
    except FileNotFoundError:
        return []


def save_tasks(tasks: List[Tuple[str, str]]) -> None:
    with open(file_path, "w") as f:
        json.dump(tasks, f)


def run() -> None:
    if sys.argv[1] == "add":
        add_task(sys.argv[2])
    elif sys.argv[1] == "list":
        list_tasks()
    elif sys.argv[1] == "done":
        mark_done(int(sys.argv[2]))
    else:
        print("invalid option")


if __name__ == "__main__":
    run()
