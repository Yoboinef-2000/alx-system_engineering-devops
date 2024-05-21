#!/usr/bin/python3

"""
Using what went on task 0,
extend the Python Script to export data
in the JSON format.
"""

import json
import requests

if __name__ == "__main__":

    theAPI = 'https://jsonplaceholder.typicode.com/'

    usersResponse = requests.get(f'{theAPI}users')
    users = usersResponse.json()

    all_tasks = {}

    for user in users:
        userId = user.get('id')
        employeeName = user.get('name')

        todosResponse = requests.get(f'{theAPI}todos?userId={userId}')
        todos = todosResponse.json()

        tasks_list = [{"username": employeeName,
                       "task": todo.get('title'),
                       "completed": todo.get('completed')} for todo in todos]

        all_tasks[userId] = tasks_list

    jsonFileName = "todo_all_employees.json"
    with open(jsonFileName, mode='w') as jsonFile:
        json.dump(all_tasks, jsonFile)
