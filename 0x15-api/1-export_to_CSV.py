#!/usr/bin/python3

"""
Using what went on task 0,
extend the Python Script to export data
in the CSV format.
"""


import sys
import requests
import csv

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

    print(f"Employee {employeeName} is done with tasks(\
          {numberOfDoneTasks}/{totalTasks}):")
    for task in doneTasks:
        print(f"\t {task.get('title')}")

    csvFileName = f"{employeeId}.csv"
    with open(csvFileName, mode='w', newline='') as csvFile:
        csvWriter = csv.writer(csvFile, quoting=csv.QUOTE_ALL)
        for todo in todos:
            csvWriter.writerow([employeeId, employeeName,
                                todo.get('completed'), todo.get('title')])
