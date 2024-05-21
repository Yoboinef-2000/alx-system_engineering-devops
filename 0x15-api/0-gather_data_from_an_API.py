#!/usr/bin/python3

"""
This python script, using the provided REST API
for a given employee ID, returns information about
his/her TODO list progress.
"""

import requests
import sys

if __name__ == "__main__":

    employeeId = int(sys.argv[1])

    theAPI = 'https://jsonplaceholder.typicode.com/'

    userResponse = requests.get(f'{theAPI}users/{employeeId}')
    userData = userResponse.json()
    employeeName = userData.get('name')

    todosResponse = requests.get(f'{theAPI}todos?userId={employeeId}')
    todos = todosResponse.json()

    totalTasks = len(todos)
    doneTasks = [todo for todo in todos if todo.get('completed')]
    numberOfDoneTasks = len(doneTasks)

    print(f"Employee {employeeName} is done with tasks("
          f"{numberOfDoneTasks}/{totalTasks}):")
    for task in doneTasks:
        print(f"\t {task.get('title')}")
