#!/usr/bin/python3
"""
This module uses a REST API to get information about a given employee's TODO
"""
import csv
import requests
import sys


def fetch_employee_todo_progress(employee_id):
    """
    Fetches employee TODO progress from a REST API
    """
    todos_url = "https://jsonplaceholder.typicode.com/todos?userId={}".format(
        employee_id)
    users_url = "https://jsonplaceholder.typicode.com/users"

    try:
        # Fetch todos data
        todos_response = requests.get(todos_url)
        todos = todos_response.json()

        # Fetch user data
        users_response = requests.get(users_url)
        users = users_response.json()

        # Find the user by ID
        user = None
        for user in users:
            if user["id"] == int(employee_id):
                break

        if user:
            user_id = user['id']
            username = user['username']

            filename = f"{user_id}.csv"
            with open(filename, 'w', newline='') as csvfile:
                csv_writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)

                for task in todos:
                    task_completed = "True" if task['completed'] else "False"
                    csv_writer.writerow([user_id, username, task_completed,
                                         task['title']])
        else:
            print("Employee ID not found")
    except requests.RequestException as e:
        print(f"Request failed: {e}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script_name.py <employee_id>")
        sys.exit(1)

    employee_id = sys.argv[1]
    fetch_employee_todo_progress(employee_id)
