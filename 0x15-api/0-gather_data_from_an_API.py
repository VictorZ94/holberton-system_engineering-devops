#!/usr/bin/python3
"""Using and API and work in Json
"""
import requests
import sys


if __name__ == "__main__":
    """working on an API
    """
    number_of_task_done = 0
    total_number_of_task = 0
    # get user and extrac his/her name
    response = requests.get('https://jsonplaceholder.typicode.com/users/{}'
                            .format(sys.argv[1]))
    get_user = response.json().values()
    user = list(get_user)[1]
    # get task
    new_reponse = requests.get('https://jsonplaceholder.typicode.com/todos/\
?userId={}'.format(sys.argv[1]))
    get_task = new_reponse.json()
    # for to count number of task
    for item in get_task:
        if item.get('completed') is True:
            number_of_task_done += 1
        total_number_of_task += 1

    print("Employee {} is done with tasks({}/{}):"
          .format(user, number_of_task_done, total_number_of_task))
    for item in get_task:
        if item.get('completed') is True:
            print("\t{}".format(item.get('title')))
