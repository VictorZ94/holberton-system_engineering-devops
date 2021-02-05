#!/usr/bin/python3
"""Working with Reddit API
"""
import requests


def top_ten(subreddit):
    """ Query the Reddit API and print the titles of the top 10 hot posts
    """
    url = "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit)
    header = {'user-agent': 'betty_hbtn'}
    r = requests.get(url, headers=header)

    if r.status_code >= 300:
        print('None')
    else:
        r = r.json()
        for post in r['data']['children']:
            print(post['data']['title'])
