#!/usr/bin/python3
"""Using and API and work in Json
"""
import json
import requests
import sys


if __name__ == "__main__":
    """working on an API
    """
    dict_to_json = {}
    new_list = []
    # get user and extrac his/her username
    response = requests.get('https://jsonplaceholder.typicode.com/users/{}'
                            .format(sys.argv[1]))
    get_user = response.json()
    username = get_user.get('username')

    # get Completed and title
    new_reponse = requests.get('https://jsonplaceholder.typicode.com/todos/\
?userId={}'.format(sys.argv[1]))
    get_task = new_reponse.json()

    with open('{}.json'.format(sys.argv[1]), mode="w") as File_json:
        for item in get_task:
            new_dict = {}
            new_dict['task'] = item.get('title')
            new_dict['completed'] = item.get('completed')
            new_dict['username'] = username
            new_list.append(new_dict)

        dict_to_json["{}".format(sys.argv[1])] = new_list
        json.dump(dict_to_json, File_json)
