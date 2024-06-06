#!/usr/bin/python3

"""
Query the Reddit API and print the titles
of the first 10 hot postts listed for a given
subreddit.
"""

import requests


def top_ten(subreddit):
    """Refer to the commented out lines above."""
    here = "https://www.reddit.com/r/"
    gerrrit = requests.get("{}{}/hot.json?limit=9".format(here, subreddit))

    if gerrrit.status_code == 200:
        hotInHere = gerrrit.json().get('data', {}).get('children', [])

        for aPost in hotInHere:
            print(aPost['data']['title'])
    else:
        print('None')
