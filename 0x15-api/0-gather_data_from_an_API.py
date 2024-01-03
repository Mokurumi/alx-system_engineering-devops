#!/usr/bin/python3
"""
This module uses a REST API to get information about a given employee's TODO
"""
import re
import requests
import sys


def fetch_employee_todo_progress(employee_id):
    """
    Fetches employee TODO progress from a REST API
    """
    todos_url = "https://jsonplaceholder.typicode.com/todos?userId={}".format(
        employee_id)

    # Fetch todos data
    todos_response = requests.get(todos_url)
    todos = todos_response.json()

    # Fetch user data for the specific employee ID
    user_url = "https://jsonplaceholder.typicode.com/users/{}".format(
        employee_id)
    user_response = requests.get(user_url)
    user = user_response.json()

    if 'id' in user:
        employee_name = user['name']

        completed_tasks = [task for task in todos if task['completed']]
        total_tasks = len(todos)
        num_completed_tasks = len(completed_tasks)

        print("Employee {} is done with tasks({}/{}):".format(
            employee_name, num_completed_tasks, total_tasks))
        for task in completed_tasks:
            print(f"\t {task['title']}")


if __name__ == "__main__":
    if len(sys.argv) > 1:
        if re.fullmatch(r'\d+', sys.argv[1]):
            fetch_employee_todo_progress(sys.argv[1])
