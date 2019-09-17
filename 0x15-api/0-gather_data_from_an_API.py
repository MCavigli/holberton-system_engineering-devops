#!/usr/bin/python3
# Module that calls RESTful API
import requests
from sys import argv


if __name__ == "__main__":
    '''Gives name of employee and completed tasks'''
    if len(argv) is not 2:
        print("Command takes 2 arguments")
        exit
    _id = argv[1]
    url = "https://jsonplaceholder.typicode.com/users/{}".format(_id)
    req = requests.get(url)
    jreq = req.json()
    name = jreq['name']
    url = "https://jsonplaceholder.typicode.com/todos"
    req = requests.get(url)
    jreq = req.json()
    tasks = []
    completed_tasks = []
    for i in jreq:
        if i['userId'] == int(_id):
            tasks.append(i)
    total_tasks = len(tasks)
    for i in tasks:
        if i['completed'] is True:
            completed_tasks.append(i)
    print("Employee {} is done with tasks({}/{}):".format(name,
                                                          len(completed_tasks),
                                                          total_tasks))
    for i in completed_tasks:
        print("\t {}".format(i['title']))
