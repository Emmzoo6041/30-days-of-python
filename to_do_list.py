import sys
import os
import json

TODO_FILE = 'todo.json'

def load_tasks():
    if os.path.exists(TODO_FILE):
        with open(TODO_FILE, 'r') as f:
            return json.load(f)
    return []

def save_tasks(tasks):
    with open(TODO_FILE, 'w') as f:
        json.dump(tasks, f, indent=4)

def add_task(task):
    tasks = load_tasks()
    tasks.append({'task': task, 'completed': False})
    save_tasks(tasks)
    print(f'Added task: "{task}"')

def list_tasks():
    tasks = load_tasks()
    if not tasks:
        print('No tasks found.')
    else:
        for idx, task in enumerate(tasks, start=1):
            status = '✓' if task['completed'] else '✗'
            print(f'{idx}. [{status}] {task["task"]}')

def complete_task(task_number):
    tasks = load_tasks()
    if 0 < task_number <= len(tasks):
        tasks[task_number-1]['completed'] = True
        save_tasks(tasks)
        print(f'Task {task_number} marked as completed.')
    else:
        print('Invalid task number.')

def delete_task(task_number):
    tasks = load_tasks()
    if 0 < task_number <= len(tasks):
        task = tasks.pop(task_number-1)
        save_tasks(tasks)
        print(f'Deleted task: "{task["task"]}"')
    else:
        print('Invalid task number.')

def show_help():
    print('To-do List Application')
    print('Usage:')
    print('  python todo.py add "task"      Add a new task')
    print('  python todo.py list            List all tasks')
    print('  python todo.py complete n      Mark task n as completed')
    print('  python todo.py delete n        Delete task n')

def main():
    if len(sys.argv) < 2:
        show_help()
    else:
        command = sys.argv[1].lower()
        if command == 'add' and len(sys.argv) > 2:
            add_task(' '.join(sys.argv[2:]))
        elif command == 'list':
            list_tasks()
        elif command == 'complete' and len(sys.argv) == 3:
            try:
                complete_task(int(sys.argv[2]))
            except ValueError:
                print('Task number must be an integer.')
        elif command == 'delete' and len(sys.argv) == 3:
            try:
                delete_task(int(sys.argv[2]))
            except ValueError:
                print('Task number must be an integer.')
        else:
            show_help()

if __name__ == '__main__':
    main()

