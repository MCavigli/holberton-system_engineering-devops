#!/usr/bin/python3
# Module that calls RESTful API and exports to JSON file
import json
import requests
from sys import argv


if __name__ == "__main__":
    '''Gives name of employee and completed tasks and exports as JSON file'''
    if len(argv) is not 2:
        print("Command takes 2 arguments")
        exit
    _id = argv[1]
    url = "https://jsonplaceholder.typicode.com/users/{}".format(_id)
    req = requests.get(url)
    jreq = req.json()
    name = jreq['username']
    url = "https://jsonplaceholder.typicode.com/todos"
    req = requests.get(url)
    jreq = req.json()
    tasks = []
    id_dict = {}
    tasks_dict = []
    for i in jreq:
        if i['userId'] == int(_id):
            tasks.append(i)
    for i in tasks:
        tasks_dict.append({'task': i['title'],
                           'completed': i['completed'],
                           'username': name
                           })
    id_dict = {_id: tasks_dict}
    with open('{}.json'.format(_id), mode='w') as json_file:
        json.dump(id_dict, json_file)
