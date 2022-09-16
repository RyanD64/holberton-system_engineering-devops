#!/usr/bin/python3
"""script that returns information about a given employee"""
import requests
import sys
import csv

if __name__ == "__main__":
    id = sys.argv[1]
    user = requests.get(f"https://jsonplaceholder.typicode.com/users/{id}")
    todo = requests.get(f"https://jsonplaceholder.typicode.com/todos")
    name = user.json().get("username")
    file = id + ".csv"

    with open('file', 'w') as result:
        write = csv.writer(result,
                           delimiter=",",
                           quotechar='"',
                           quoting=csv.QUOTE_ALL,
                           lineterminator='\n')
        for task in todo.json():
            if task.get('userId') == int(id):
                write.writerow([id,
                                name,
                                str(task.get("completed")),
                                task.get("title")])
