#!/usr/bin/python3
"""Given a employee ID returns info about his/her ToDo list progress"""
import requests
from sys import argv


def to_do_list(user_id):
    """retireve the toDo list"""
    url = 'https://jsonplaceholder.typicode.com/'
    user_request = "{}users/{}".format(url, user_id)
    employee_dict = requests.get(user_request).json()
    employee_name = employee_dict.get("name")

    tasks_dict = requests.get("{}todos?userId={}".format(url, user_id)).json()
    total_num_of_tasks = len(tasks_dict)

    done_task_dict = requests.get("{}todos?userId={}&&completed=true"
                                  .format(url, user_id)).json()
    num_done_tasks = len(done_task_dict)

    print("Employee {} is done with tasks({}/{}):"
          .format(employee_name, num_done_tasks, total_num_of_tasks))
    for info_dict in done_task_dict:
        task_title = info_dict.get("title")
        print("\t " + task_title)

if __name__ == "__main__":
    to_do_list(argv[1])