#!/usr/bin/python3
"""Working with Reddit API
"""
import requests


def number_of_subscribers(subreddit):
    """ Queries the Reddit API and returns the number of subscribers
    """
    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    header = {'user-agent': 'betty_hbtn'}
    r = requests.get(url, headers=header)

    if r.status_code is not 200:
        return 0
    else:
        return r.json().get('data').get('subscribers')
