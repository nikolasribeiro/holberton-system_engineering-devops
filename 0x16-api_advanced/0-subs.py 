#!/usr/bin/python3
"""
    Function that queries the Reddit API and returns the number
    of subscribers for a given subreddit. Function returns 0
    if invalid subreddit given
"""
import requests


def number_of_subscribers(subreddit):
    """
        Method to return number of subscribers per subreddit
        subreddit: argument being passed in
        return: number of subscribers in the subreddit
    """
    reddit_url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {"User-Agent": "Holberton API access v0.1 (by /u/holbie)"}
    reddit_response = requests.get(reddit_url, headers=headers)
    if not reddit_response:
        return 0
    reddit_resp_json = reddit_response.json()
    data = reddit_resp_json.get("data")
    sub_count = data.get("subscribers")
    if not sub_count:
        return 0
    return sub_count