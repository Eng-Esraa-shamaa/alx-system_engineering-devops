#!/usr/bin/python3
"""
function that queries the Reddit API and returns the number of subscribers
"""
import json
import requests


def number_of_subscribers(subreddit):
    user = {"User-Agent": "Esraa1993"}
    request = requests.get("https://www.reddit.com/r/{}/about.json"
                           .format(subreddit), headers=user)
    if request.status_code == 200:
        return request.json().get("data").get("subscribers")
    else:
        return 0
