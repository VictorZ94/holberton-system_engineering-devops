#!/usr/bin/python3
"""Using and API and work in Json
"""
import json
import requests


if __name__ == "__main__":
    """working on an API
    """
    dict_to_json = {}
    url = 'https://jsonplaceholder.typicode.com'

    # get user and extrac his/her username
    response = requests.get('{}/users'.format(url))
    get_user = response.json()
    for user in get_user:
        new_list = []
        id = user.get('id')
        username = user.get('username')

        # get Completed and title
        new_reponse = requests.get('{}/todos/?userId={}'.format(url, id))
        get_task = new_reponse.json()

        for item in get_task:
            new_dict = {}
            new_dict['username'] = username
            new_dict['task'] = item.get('title')
            new_dict['completed'] = item.get('completed')
            new_list.append(new_dict)
        dict_to_json["{}".format(id)] = new_list

    with open('todo_all_employees.json', mode="w") as File_json:
        json.dump(dict_to_json, File_json)
