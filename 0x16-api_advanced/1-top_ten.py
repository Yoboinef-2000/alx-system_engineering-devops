#!/usr/bin/python3

"""
Query the Reddit API and print the titles
of the first 10 hot posts listed for a given
subreddit.
"""

import requests


def top_ten(subreddit):
    """Refer to the commented out lines above."""
    # here = "https://www.reddit.com/r/"
    # headThatThang = {'User-Agent': 'Let_this_if_this_works'}
    # gerrrit = requests.get("{}{}/hot.json?limit=9".format(here, subreddit),
    #                        allow_redirects=False,
    #                        headers=headThatThang)

    # if gerrrit.status_code == 200:
    #     hotInHere = gerrrit.json().get('data', {}).get('children', [])

    #     for aPost in hotInHere:
    #         print(aPost['data']['title'])
    # else:
    #     print('None')
    sub_info = requests.get("https://www.reddit.com/r/{}/hot.json?limit=10"
                            .format(subreddit),
                            headers={"User-Agent": "My-User-Agent"},
                            allow_redirects=False)
    if sub_info.status_code >= 300:
        print('None')
    else:
        [print(child.get("data").get("title"))
         for child in sub_info.json().get("data").get("children")]

