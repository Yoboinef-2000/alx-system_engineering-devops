#!/usr/bin/python3

"""
QUery the Reddit API and return
the number of subscirbers for a given
subreddit.
"""

import requests
# import sys


def number_of_subscribers(subreddit):
    """Refer to the commented out lines at the top."""

    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)

    response = requests.get(url, allow_redirects=False)

    if response.status_code == 200:
        data = response.json().get('data', {})
        print('OK')
        return data.get('subscribers', 0)
    else:
        print('OK')
        return 0
