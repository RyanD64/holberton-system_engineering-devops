#!/usr/bin/python3
"""print the first 10 hot posts listed for a given subreddit."""
import requests


def top_ten(subreddit):
    req = requests.get("https://www.reddit.com/r/{}/hot.json?limit=10"
                       .format(subreddit),
                       headers={"User-Agent": "holberton"},
                       allow_redirects=False)

    if req.status_code == 200:
        for a in req.json().get("data").get("children"):
            print(a.get("data").get("title"))
    else:
        print(None)
