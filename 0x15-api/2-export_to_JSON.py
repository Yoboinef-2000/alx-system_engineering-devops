#!/usr/bin/python3

"""
Using what went on task 0,
extend the Python Script to export data
in the JSON format.
"""

import json
import requests
import sys

if __name__ == "__main__":

    employeeId = int(sys.argv[1])
    theAPI = 'https://jsonplaceholder.typicode.com/'

    userResponse = requests.get(f'{theAPI}users/{employeeId}')
    userData = userResponse.json()
    employeeName = userData.get('username')

    todosResponse = requests.get(f'{theAPI}todos?userId={employeeId}')
    todos = todosResponse.json()

    totalTasks = len(todos)
    doneTasks = [todo for todo in todos if todo.get('completed')]
    numberOfDoneTasks = len(doneTasks)

    tasks_list = [{"task": todo.get('title'),
                   "completed": todo.get('completed'),
                   "username": employeeName} for todo in todos]

    user_tasks = {str(employeeId): tasks_list}

    jsonFileName = f"{employeeId}.json"
    with open(jsonFileName, mode='w') as jsonFile:
        json.dump(user_tasks, jsonFile)
