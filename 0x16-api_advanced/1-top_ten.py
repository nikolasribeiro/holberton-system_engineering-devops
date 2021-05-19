#!/usr/bin/python3
"""
    A Function that queries the Reddit API and prints the titles of
    the first 10 hot posts listed for a given subreddit
"""
import requests


def top_ten(subreddit):
    """
        Method that prints the title of the first 10 hop posts for a subreddit
    """
    reddit_url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {"User-Agent": "Holberton API access v0.1 (by /u/holbie)"}
    reddit_response = requests.get(reddit_url, headers=headers)
    if not reddit_response:
        print("None")
    else:
        reddit_resp_json = reddit_response.json()
        data_list = reddit_resp_json.get("data").get("children")
        if not data_list:
            print("None")
        ten_list = data_list[:10]
        for item in ten_list:
            print(item.get("data").get("title"))