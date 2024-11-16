# Task Tracker CLI

Task tracker is a project used to track and manage your tasks. It's a simple command line 
interface (CLI) to track what you  need to do, what you have done, and what you are currently working on.
Tasks are stored in JSON file.

View project in [roadmap.sh](https://www.roadmap.sh).

## Installation

1. Clone this repository
2. Navigate to the project directory
3. Execute main.py. Make sure you have Python installed. 

## Usage

### Task Properties

- id: A unique identifier for the task.
- description: A short description of the task.
- status: The status of the task(todo,in-progress,done).
- createdAt: The date and time when the task was created.
- updatedAt: The date and time when the task was last updated.


### Features

- Add, Update, and Delete tasks.
- Mark a task as in progress or done.
- List all tasks.
- List all tasks that are donde.
- List all tasks that are not done.
- List all tasks that are in progress.

### Commands

#### add

Add a new task to the list tasks.

-m : Description of the task.

-s : Status of the task: todo, in-progress or done. 

Example:

    add -m Hi, this is a new task -s in-pgogress

> [!NOTE]
> When the status is not provided or is an incorrect value, todo is assigned

#### update

Update a task.

id : The id of the task to update.

-m : Description of the task.

-s : Status of the task: todo, in-progress or done. Is not required.



Example:

    update 1 -m Hello, this is an updated task

#### delete
id: The id of the task to delete.

Example:
    delete 1

#### progress

Mark a task as in-progress

id: The id of the task to mark as in-progress

Example:

    progress 1

#### done

Mark a task as done

id: The id of the task to mark as done

Example:

    done

#### list

Show the list of tasks

Example:

    list

#### list-todo

Show the list of tasks with status: todo

Example:

    list-todo

#### list-in-progress

Show the list of tasks with status: in-progress.

Example:

    list-in-progress

#### list-done

Show the list of tasks with status: done.

Example:

    list-done

#### exit

Close the console.
