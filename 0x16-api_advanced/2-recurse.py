#!/usr/bin/python3
"""Working with Reddit API
"""
import requests


def recurse(subreddit, hot_list=[]):
    """recursive function that queries the Reddit API
    """
    if type(subreddit) is list:
        url = "https://api.reddit.com/r/{}?sort=hot".format(subreddit[0])
        url = "{}&after={}".format(url, subreddit[1])
    else:
        url = "https://api.reddit.com/r/{}?sort=hot".format(subreddit)
        subreddit = [subreddit, ""]
    header = {'User-Agent': 'betty-hbtn'}
    req = requests.get(url, headers=header, allow_redirects=False)
    if req.status_code != 200:
        return (None)
    req = req.json()
    if "data" in req:
        data = req.get("data")
        if not data.get("children"):
            return (hot_list)
        for post in data.get("children"):
            hot_list += [post.get("data").get("title")]
        if not data.get("after"):
            return (hot_list)
        subreddit[1] = data.get("after")
        recurse(subreddit, hot_list)
        if hot_list[-1] is None:
            del hot_list[-1]
        return (hot_list)
    else:
        return (None)
