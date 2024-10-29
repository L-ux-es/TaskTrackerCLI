import argparse

from taskHandling import (add_task, update_task, delete_task, mark_in_progress,
                          mark_done, list_task, list_done_task, list_in_progress_task, list_todo_task)

HELP_ID_MESSAGE = 'The id of the task'


def add_command(args):
    add_task(args.message, args.status)


def update_command(args):
    update_task(args.id, args.message, args.status)


def list_command(args):
    list_task()


def list_todo_command(args):
    list_todo_task()


def list_done_command(args):
    list_done_task()


def list_progress_command(args):
    list_in_progress_task()


def exit_command(args):
    print("Closing the console...")


def main():
    parser = argparse.ArgumentParser(description='Task Tracker')
    subparsers = parser.add_subparsers(dest='command')
    add_parser = subparsers.add_parser('add', help="Add a task")
    add_parser.add_argument('-m', '--message', required=True, help='The description of the task')
    add_parser.add_argument('-s', '--status', required=True, help='The state of task,it can be: todo,in '
                                                                  'progress or done')
    add_parser.set_defaults(func=add_command)
    update_parser = subparsers.add_parser('update', help='Update a task')
    update_parser.add_argument('id', help=HELP_ID_MESSAGE)
    update_parser.add_argument('-m', '--message', required=True, help='The new description of the task')
    update_parser.add_argument('-s', '--status',
                               help='The status of task,it can be todo,in progress or done')
    update_parser.set_defaults(func=update_command)
    mark_progress_parser = subparsers.add_parser('progress', help='Mark a task as in progress')
    mark_progress_parser.add_argument('id', help=HELP_ID_MESSAGE)
    mark_progress_parser.set_defaults(func=mark_in_progress)
    mark_done_parser = subparsers.add_parser('done', help='Mark a task as done')
    mark_done_parser.add_argument('id', help=HELP_ID_MESSAGE)
    mark_done_parser.set_defaults(func=mark_done)
    delete_parser = subparsers.add_parser('delete', help='Delete a task')
    delete_parser.add_argument('id', help=HELP_ID_MESSAGE)
    delete_parser.set_defaults(func=delete_task)
    list_parser = subparsers.add_parser('list', help='List all tasks')
    list_parser.set_defaults(func=list_command)
    list_todo_parser = subparsers.add_parser('list-todo', help='List tasks that are not done')
    list_todo_parser.set_defaults(func=list_todo_command)
    list_in_progress_parser = subparsers.add_parser('list-in-progress', help='List tasks that are  in progress')
    list_in_progress_parser.set_defaults(func=list_progress_command)
    list_done_parser = subparsers.add_parser('list-done', help='List tasks that are done')
    list_done_parser.set_defaults(func=list_done_command)
    exit_parser = subparsers.add_parser('exit', help='Close the console')
    exit_parser.set_defaults(func=exit_command)
    print("Task Tracker\n")
    while True:
        user_input = input("Enter a command:\n ").split()
        if not user_input:
            continue
        args = parser.parse_args(user_input)
        if args.command is not None:
            args.func(args)
            if args.command == 'exit':
                break
        else:
            parser.print_help()


if __name__ == '__main__':
    main()
