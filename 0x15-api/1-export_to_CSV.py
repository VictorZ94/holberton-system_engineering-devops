#!/usr/bin/python3
"""Using and API and work in Json
"""
import csv
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
    username = list(get_user)[2]

    new_reponse = requests.get('https://jsonplaceholder.typicode.com/todos/\
?userId={}'.format(sys.argv[1]))
    get_task = new_reponse.json()

    with open('{}.csv'.format(sys.argv[1]), mode="w") as File_csv:
        Api_writer = csv.writer(File_csv, quotechar='"', quoting=csv.QUOTE_ALL)
        for item in get_task:
            Api_writer.writerow((sys.argv[1], username,
                                 item.get('completed'),
                                 item.get('title')))
