class Task:
    def __init__(self, name):
        self.name = name

tasks = []

def create_task(name):
    tasks.append(Task(name))

def read_tasks():
    for task in tasks:
        print(task.name)

def update_task(index, new_name):
    if 0 <= index < len(tasks):
        tasks[index].name = new_name

def delete_task(index):
    if 0 <= index < len(tasks):
        tasks.pop(index)

create_task("Task 1")
create_task("Task 2")
read_tasks()
update_task(0, "Updated Task 1")
read_tasks()
delete_task(1)
read_tasks()
