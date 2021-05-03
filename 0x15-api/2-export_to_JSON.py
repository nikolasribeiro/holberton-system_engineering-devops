#!/usr/bin/python3
"""Export data in the JSON format"""

import json
import requests
from sys import argv


def search_and_export_json(user_id):
    """Export data in the JSON format"""

    url = 'https://jsonplaceholder.typicode.com/'
    user_request = "{}users/{}".format(url, user_id)
    employee_dict = requests.get(user_request).json()
    employee_name = employee_dict.get("name")

    tasks_dict = requests.get("{}todos?userId={}".format(url, user_id)).json()
    user_name = employee_dict.get("username")

    my_dict = {}
    my_list = []

    for info in tasks_dict:
        tasks_owned_by_emp = {}
        tasks_owned_by_emp["task"] = info.get('title')
        tasks_owned_by_emp["completed"] = info.get('completed')
        tasks_owned_by_emp["username"] = employee_dict.get('username')
        my_list.append(tasks_owned_by_emp)

    my_dict[user_id] = my_list

    file_name = "{}.json".format(user_id)
    with open(file_name, mode='w') as json_file:
        json.dump(my_dict, json_file)

if __name__ == "__main__":
    search_and_export_json(argv[1])
