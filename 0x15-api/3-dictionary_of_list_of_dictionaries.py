#!/usr/bin/python3
"""
This module uses a REST API to get information about a given employee's TODO
"""
import json
import requests


def fetch_all_employees_todo():
    todos_url = "https://jsonplaceholder.typicode.com/todos"
    users_url = "https://jsonplaceholder.typicode.com/users"

    try:
        # Fetch todos data
        todos_response = requests.get(todos_url)
        todos = todos_response.json()

        # Fetch user data
        users_response = requests.get(users_url)
        users = users_response.json()

        all_employees_tasks = {}

        for user in users:
            user_id = user['id']
            username = user['username']

            user_tasks = []
            for task in todos:
                if task['userId'] == user_id:
                    task_completed = task['completed']
                    task_title = task['title']
                    user_tasks.append({"username": username,
                                       "task": task_title,
                                       "completed": task_completed})

            all_employees_tasks[str(user_id)] = user_tasks

        filename = "todo_all_employees.json"
        with open(filename, 'w') as jsonfile:
            json.dump(all_employees_tasks, jsonfile, indent=4)
    except requests.RequestException as e:
        print(f"Request failed: {e}")


if __name__ == "__main__":
    fetch_all_employees_todo()
