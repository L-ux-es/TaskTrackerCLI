from datetime import datetime

import jsonHandling

DESCRIPTION = 'description'
STATUS = 'status'
TODO = 'todo'
IN_PROGRESS = 'in-progress'
Done = 'done'


def add_task(description: str, status=TODO):
    tasks = read_tasks_from_json()
    last_task: dict[int, str, str, str, str] = tasks[-1]
    next_id = 1
    if last_task != {}:
        next_id = last_task['id'] + 1
    if status != TODO and status != IN_PROGRESS and status != Done:
        status = TODO
    task = {"id": next_id, DESCRIPTION: description, STATUS: status,
            'created': datetime.now().strftime("%Y-%m-%d %H:%M"), 'updated': '-'}
    tasks.append(task)
    jsonHandling.write_json(tasks)
    print(f"Task added: {task['id']} {task[DESCRIPTION]}  {task['status']}")


def update_task(identification: int, description: str, status: str):
    tasks = read_tasks_from_json()
    task = get_task_by_id(tasks, identification)
    if task is not None:
        task[DESCRIPTION] = description
        task[STATUS] = status
        task['updated'] = datetime.now().strftime("%Y-%m-%d %H:%M")
        jsonHandling.write_json(tasks)
        print("Task updated.")
    else:
        print(f"The task with id {id} don't exist.")


def delete_task(identification: int):
    tasks = read_tasks_from_json()
    task = get_task_by_id(tasks, identification)
    if task is not None:
        tasks.remove(task)
        jsonHandling.write_json(tasks)
        print("delete")
    else:
        print(f"The task with id {identification} don't exist.")


def get_task_by_id(tasks: list, identification: int) -> dict | None:
    for task in tasks:
        if task['id'] == identification:
            return task
    return None


def mark_in_progress(identification: int):
    change_type_of_task(identification, IN_PROGRESS)


def mark_done(identification: int):
    change_type_of_task(identification, Done)


def mark_todo(identification: int):
    change_type_of_task(identification, TODO)


def change_type_of_task(identification: int, type_task: str):
    tasks = read_tasks_from_json()
    task = get_task_by_id(tasks, identification)
    if task is not None:
        task[STATUS] = type_task
        print(f"Task marked as {type_task}.")
    else:
        print(f"The task with id {identification} don't exist.")


def list_todo_task():
    list_task(TODO)


def list_in_progress_task():
    list_task(IN_PROGRESS)


def list_done_task():
    list_task(Done)


def list_task(status="all"):
    tasks_list = read_tasks_from_json()
    count = 0
    if len(tasks_list) != 0:
        for task in tasks_list:
            if status == "all" or task[STATUS] == status:
                count += 1
                print(
                    'ID: ' + str(task['id']) + ' DESCRIPTION: ' + task[DESCRIPTION] + ' STATUS: ' + task[STATUS] + ' CREATED: ' +
                    task['created'] + ' UPDATED: ' + task['updated'])
        if count == 0:
            print(f"There are no tasks with type:{status}.")
    else:
        print("There are no tasks.")


def read_tasks_from_json():
    try:
        data_json = jsonHandling.read_json()
        if data_json is not None:
            return data_json
        return []
    except ValueError:
        raise ValueError("Failed to read te json file.")
