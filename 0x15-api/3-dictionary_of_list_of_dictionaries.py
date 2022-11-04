#!/usr/bin/python3
"""script that returns information about a given employee"""
import json
import requests

if __name__ == "__main__":
    user = (requests.get(
        "https://jsonplaceholder.typicode.com/users/" 
    )).json()
    todo = (requests.get(
        "https://jsonplaceholder.typicode.com/todos"
    )).json()

    file = "todo_all_employees" + ".json"
    users = {}

    for use in user:
        list = []
        for task in todo:
            if task.get('userId') == use.get('id'):
                Dict = {"username": use.get("username"),
                        "task": task.get("title"),
                        "completed": task.get("completed")}
                list.append(Dict)
        users[use.get('id')] = list

    with open(file, "w") as result:
        json.dump(users, result)