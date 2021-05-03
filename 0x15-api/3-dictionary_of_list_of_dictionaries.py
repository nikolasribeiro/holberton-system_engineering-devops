#!/usr/bin/python3
"""Export data in the JSON format"""

import json
import requests


def search_and_export_json():
    """Export data in the JSON format"""

    url = 'https://jsonplaceholder.typicode.com/'

    users_dict = requests.get("{}users".format(url)).json()
    tasks_dict = requests.get("{}todos".format(url)).json()

    my_dict = {}
    usernames_dict = {}

    for info in users_dict:
        user_id = info.get('id')
        my_dict[user_id] = []
        usernames_dict[user_id] = info.get('username')

    for info in tasks_dict:
        tasks_all_emp = {}
        user_id = info.get('userId')
        tasks_all_emp["task"] = info.get('title')
        tasks_all_emp["completed"] = info.get('completed')
        tasks_all_emp["username"] = usernames_dict.get(user_id)
        my_dict.get(user_id).append(tasks_all_emp)

    file_name = "todo_all_employees.json"
    with open(file_name, mode='w') as json_file:
        json.dump(my_dict, json_file)

if __name__ == "__main__":
    search_and_export_json()