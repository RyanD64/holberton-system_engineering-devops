#!/usr/bin/python3
"""function that queries the Reddit API and return the number of subs"""
import requests


def number_of_subscribers(subreddit):
    req = requests.get("https://www.reddit.com/r/{}/about.json"
                       .format(subreddit),
                       headers={"User-Agent": "holberton"},
                       allow_redirects=False)

    if req.status_code == 200:
        return req.json()["data"]["subscribers"]

    return 0
